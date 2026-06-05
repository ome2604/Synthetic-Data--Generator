class ConversationAgent:

    def collect_requirements(self):

        print("\n=== Requirement Collection Agent ===\n")

        domain = input(
            "What are you building?\n> "
        )

        purpose = input(
            "\nPurpose?\n> "
        )

        scale = input(
            "\nDataset Size (Small/Medium/Large)?\n> "
        )

        requirement = f"""
        Domain: {domain}

        Purpose: {purpose}

        Dataset Size: {scale}
        """

        return requirement