from faker_mapper import generate_value
from foreign_key_resolver import get_foreign_key_value


def generate_table_data(
    table,
    generated_data,
    rows=10
):
    """
    Generate records for any table dynamically.
    """

    records = []

    table_name = table["name"]

    primary_key = None

    for column in table["columns"]:

        datatype = column["datatype"].lower()

        if "primary key" in datatype:
            primary_key = column["name"]
            break

    if not primary_key:

        if table_name.endswith("ies"):
            primary_key = (
            table_name[:-3] + "y_id"
        )

        elif table_name.endswith("s"):
            primary_key = (
            table_name[:-1] + "_id"
        )

        else:
            primary_key = (
            table_name + "_id"
        )

    for row_id in range(1, rows + 1):

        record = {}

        for column in table["columns"]:

            column_name = column["name"]
            datatype = column["datatype"]

            # Primary Key
            if column_name == primary_key:
                record[column_name] = row_id
                continue

            # Foreign Key
            if "references" in datatype.lower():

                fk_value = get_foreign_key_value(
                    datatype,
                    generated_data
                )

                record[column_name] = fk_value

                continue

            # Normal Field
            record[column_name] = generate_value(
                column_name
            )

        records.append(record)

    return records