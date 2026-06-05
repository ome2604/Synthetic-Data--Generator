import json


def create_generation_plan(requirement_json):

    # Convert string JSON to dict
    if isinstance(requirement_json, str):

        try:
            requirement_json = json.loads(
                requirement_json
            )
        except Exception as e:

            print(
                f"JSON Parsing Error: {e}"
            )

            return None

    plan = {
        "domain": requirement_json.get(
            "domain"
        ),
        "generation_plan": []
    }

    entities = requirement_json.get(
        "entities",
        []
    )

    priority = 1

    for entity in entities:

        # Handle entity being dict
        if isinstance(entity, dict):

            entity_name = entity.get(
                "name",
                "unknown"
            )

            rows = entity.get(
                "count",
                100
            )

        # Handle entity being string
        else:

            entity_name = str(entity)

            rows = 100

        table_name = (
            entity_name.lower()
            + "s"
        )

        plan["generation_plan"].append(
            {
                "table": table_name,
                "rows": rows,
                "priority": priority
            }
        )

        priority += 1

    return plan