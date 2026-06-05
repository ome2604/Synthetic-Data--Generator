import json

from agents.planning_agent import create_generation_plan
from agents.requirement_agent import collect_requirements
from csv_exporter import export_csv
from dependency_resolver import topological_sort
from relationship_mapper import build_dependency_graph, extract_foreign_keys
from schema_generator import generate_schema
from synthetic_data_generator import generate_table_data
from agents.validation_agent import (
    validate_primary_keys
)


class SyntheticDataOrchestrator:

    def __init__(self):
        self.generated_data = {}

    def run(self, user_request):

        # ==========================================
        # STEP 1 : REQUIREMENTS
        # ==========================================
        print("\n" + "=" * 60)
        print("STEP 1 : REQUIREMENT COLLECTION")
        print("=" * 60)

        requirements = collect_requirements(user_request)

        if not requirements:
            raise Exception("Failed to collect requirements.")

        print(f"Domain: {requirements.get('domain')}")

        # ==========================================
        # STEP 2 : PLAN
        # ==========================================
        print("\n" + "=" * 60)
        print("STEP 2 : GENERATION PLAN")
        print("=" * 60)

        plan = create_generation_plan(requirements)
        print(json.dumps(plan, indent=2))

        # ==========================================
        # STEP 3 : SCHEMA
        # ==========================================
        print("\n" + "=" * 60)
        print("STEP 3 : SCHEMA GENERATION")
        print("=" * 60)

        schema = generate_schema(user_request)
        schema_dict = schema.model_dump()

        with open("schema.json", "w", encoding="utf-8") as f:
            json.dump(schema_dict, f, indent=4)

        print("schema.json created")
        print("\nTables Found:\n")

        for table in schema_dict["tables"]:
            print(f"- {table['name']}")

        # ==========================================
        # STEP 4 : RELATIONSHIPS
        # ==========================================
        print("\n" + "=" * 60)
        print("STEP 4 : RELATIONSHIP ANALYSIS")
        print("=" * 60)

        relationships = extract_foreign_keys(schema_dict)

        print("\nRelationships Found:\n")
        for rel in relationships:
            print(
                f"{rel['table']}.{rel['column']} -> "
                f"{rel['references_table']}.{rel['references_column']}"
            )

        graph = build_dependency_graph(relationships)

        print("\nDependency Graph:\n")
        print(graph)

        generation_order = topological_sort(graph)

        print("\nGeneration Order:\n")
        for i, table in enumerate(generation_order, start=1):
            print(f"{i}. {table}")

        # ==========================================
        # STEP 5 : DATA GENERATION
        # ==========================================
        print("\n" + "=" * 60)
        print("STEP 5 : DATA GENERATION")
        print("=" * 60)

        generated_data = {}

        for table_name in generation_order:
            # Find the schema for the current table safely
            table_schema = next(
                (t for t in schema_dict["tables"] if t["name"] == table_name),
                None,
            )

            if not table_schema:
                continue

            print(f"\nGenerating {table_name}...")

            records = generate_table_data(
                table=table_schema, generated_data=generated_data, rows=10
            )

            generated_data[table_name] = records
            export_csv(records, table_name)

            print(f"Generated {len(records)} records")

        # ==========================================
        # STEP 6 : VALIDATION
        # ==========================================
        print("\n" + "=" * 60)
        print("STEP 6 : VALIDATION")
        print("=" * 60)

        validation_results = {}

        for table_name, records in generated_data.items():
            if not records:
                continue

            # Assuming the first key in the dict is the primary key
            primary_key = list(records[0].keys())[0]
            result = validate_primary_keys(records, primary_key)
            validation_results[table_name] = result

        print(json.dumps(validation_results, indent=2))

        # ==========================================
        # COMPLETE
        # ==========================================
        print("\n" + "=" * 60)
        print("PIPELINE COMPLETED")
        print("=" * 60)

        self.generated_data = generated_data

        return {
            "requirements": requirements,
            "plan": plan,
            "schema": schema_dict,
            "relationships": relationships,
            "generation_order": generation_order,
            "generated_data": generated_data,
            "validation": validation_results,
        }