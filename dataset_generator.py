import json

from relationship_mapper import (
    extract_foreign_keys,
    build_dependency_graph
)

from dependency_resolver import (
    topological_sort
)

from synthetic_data_generator import (
    generate_table_data
)

from csv_exporter import export_csv


ROWS_PER_TABLE = 50


with open("schema.json", "r") as f:
    schema = json.load(f)

relationships = extract_foreign_keys(
    schema
)

graph = build_dependency_graph(
    relationships
)

generation_order = topological_sort(
    graph
)

table_lookup = {
    table["name"]: table
    for table in schema["tables"]
}

generated_data = {}

print("\nGeneration Order:\n")

for table_name in generation_order:

    print(table_name)

    table = table_lookup.get(table_name)

    if not table:
        continue

    records = generate_table_data(
        table=table,
        generated_data=generated_data,
        rows=ROWS_PER_TABLE
    )

    generated_data[table_name] = records

    export_csv(
        records,
        table_name
    )

print("\nDataset Generation Complete!")