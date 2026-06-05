def collect_requirements():

    domain = input(
        "What system do you want to build? "
    )

    purpose = input(
        "Why do you need synthetic data? "
    )

    records = int(
        input(
            "How many records per table? "
        )
    )

    return {
        "domain": domain,
        "purpose": purpose,
        "records": records
    }