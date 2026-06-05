from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def collect_requirements(user_input):
    """
    Collect and structure business requirements
    for synthetic data generation.
    """

    prompt = f"""
You are a Senior Data Architect.

Analyze the user's request and return ONLY valid JSON.

Extract:

1. domain
2. business_goal
3. entities
4. estimated_scale
5. data_requirements

For entities include:
- name
- count
- attributes
- relationships (if applicable)

User Request:

{user_input}

Return ONLY JSON.
"""

    try:

        response = client.responses.create(
            model="gpt-5",
            input=prompt
        )

        result = response.output_text.strip()

        # Remove markdown if model returns it
        result = result.replace(
            "```json",
            ""
        )

        result = result.replace(
            "```",
            ""
        )

        result = result.strip()

        # Convert JSON string → Python dict
        return json.loads(result)

    except json.JSONDecodeError as e:

        print(
            f"JSON Parsing Error: {e}"
        )

        print(
            "Raw Response:"
        )

        print(result)

        return None

    except Exception as e:

        print(
            f"Error: {e}"
        )

        return None