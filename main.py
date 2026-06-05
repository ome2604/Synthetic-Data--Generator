from orchestrator import SyntheticDataOrchestrator


def run():
    print("\n=== AI Synthetic Data Generator ===\n")

    user_request = input("Describe your system:\n\n")

    orchestrator = SyntheticDataOrchestrator()
    result = orchestrator.run(user_request)

    print("\nGeneration Complete.")
    print("\nGenerated Tables:\n")

    for table in result["generation_order"]:
        print(f"- {table}")

    print("\nCSV files saved to outputs/")


if __name__ == "__main__":
    run()