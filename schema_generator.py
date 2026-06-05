import os

from dotenv import load_dotenv
from openai import OpenAI

from models import DatabaseSchema
from prompts import SCHEMA_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_schema(requirement: str):

    response = client.responses.parse(
        model="gpt-5",
        input=[
            {
                "role": "system",
                "content": SCHEMA_PROMPT
            },
            {
                "role": "user",
                "content": requirement
            }
        ],
        text_format=DatabaseSchema
    )

    return response.output_parsed