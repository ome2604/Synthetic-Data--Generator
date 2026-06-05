import re
from collections import defaultdict


def extract_foreign_keys(schema_dict):
    """
    Extract relationships from schema.

    Supports:

    1. Explicit:
       doctor_id BIGINT REFERENCES doctors(doctor_id)

    2. Inferred:
       doctor_id -> doctors.doctor_id
       patient_id -> patients.patient_id
       team_id -> teams.team_id
    """

    relationships = []

    table_names = {
        table["name"]
        for table in schema_dict["tables"]
    }

    for table in schema_dict["tables"]:

        table_name = table["name"]

        for column in table["columns"]:

            column_name = column["name"]

            datatype = str(
                column.get(
                    "datatype",
                    ""
                )
            )

            # -------------------------------------------------
            # CASE 1:
            # Explicit REFERENCES
            # -------------------------------------------------

            match = re.search(
                r"REFERENCES\s+([a-zA-Z0-9_]+)\(([a-zA-Z0-9_]+)\)",
                datatype,
                re.IGNORECASE
            )

            if match:

                relationships.append(
                    {
                        "table": table_name,
                        "column": column_name,
                        "references_table": match.group(1),
                        "references_column": match.group(2)
                    }
                )

                continue

            # -------------------------------------------------
            # CASE 2:
            # Infer from *_id naming
            # -------------------------------------------------

            if (
                column_name.endswith("_id")
                and column_name != f"{table_name[:-1]}_id"
            ):

                singular = (
                    column_name
                    .replace("_id", "")
                )

                plural = singular + "s"

                if plural in table_names:

                    relationships.append(
                        {
                            "table": table_name,
                            "column": column_name,
                            "references_table": plural,
                            "references_column": column_name
                        }
                    )

    return relationships


def build_dependency_graph(
    relationships
):

    graph = defaultdict(set)

    for rel in relationships:

        child = rel["table"]

        parent = rel[
            "references_table"
        ]

        graph[child].add(parent)

    return {
        table: list(parents)
        for table, parents
        in graph.items()
    }


def print_relationships(
    relationships
):

    print("\nRelationships Found:\n")

    for rel in relationships:

        print(
            f"{rel['table']}.{rel['column']} "
            f"-> "
            f"{rel['references_table']}."
            f"{rel['references_column']}"
        )