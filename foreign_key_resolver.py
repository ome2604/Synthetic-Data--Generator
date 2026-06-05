import random
import re


def get_foreign_key_value(datatype, generated_data):
    """
    Extract parent table and column from REFERENCES
    and return a random valid FK value.
    """

    match = re.search(
        r"REFERENCES\s+([a-zA-Z0-9_]+)\(([a-zA-Z0-9_]+)\)",
        datatype,
        re.IGNORECASE
    )

    if not match:
        return None

    parent_table = match.group(1)
    parent_column = match.group(2)

    if parent_table not in generated_data:
        return None

    parent_records = generated_data[parent_table]

    if parent_table not in generated_data:

        raise ValueError(
            f"{parent_table} must be generated before child tables."
    )

    if not parent_records:

        raise ValueError(
            f"No records found in {parent_table}"
    )

    return random.choice(parent_records)[parent_column]