def validate_primary_keys(
    records,
    primary_key
):

    values = [
        row[primary_key]
        for row in records
        if primary_key in row
    ]

    duplicates = []

    seen = set()

    for value in values:

        if value in seen:
            duplicates.append(value)

        seen.add(value)

    return {
        "check": "primary_key_uniqueness",
        "passed": len(duplicates) == 0,
        "duplicates": duplicates
    }