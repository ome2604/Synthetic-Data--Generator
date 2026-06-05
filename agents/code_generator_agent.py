import os


class CodeGeneratorAgent:

    @staticmethod
    def generate_script(
        table_name,
        columns,
        rows=100
    ):

        code = f"""
from faker import Faker
import pandas as pd

fake = Faker()

records = []

for i in range(1, {rows + 1}):

    record = {{
"""

        for column in columns:

            column_name = column["name"]

            if column_name.endswith("_id"):

                code += f"""
        "{column_name}": i,
"""

            elif "first_name" in column_name:

                code += f"""
        "{column_name}": fake.first_name(),
"""

            elif "last_name" in column_name:

                code += f"""
        "{column_name}": fake.last_name(),
"""

            elif "email" in column_name:

                code += f"""
        "{column_name}": fake.email(),
"""

            elif "phone" in column_name:

                code += f"""
        "{column_name}": fake.phone_number(),
"""

            elif "date" in column_name:

                code += f"""
        "{column_name}": str(fake.date()),
"""

            else:

                code += f"""
        "{column_name}": fake.word(),
"""

        code += """
    }

    records.append(record)

df = pd.DataFrame(records)

df.to_csv(
"""

        code += f'"{table_name}.csv"'

        code += """
,
    index=False
)

print(
"""

        code += f'"Generated {table_name}.csv"'

        code += """
)
"""

        return code

    @staticmethod
    def save_script(
        script_code,
        filename
    ):

        os.makedirs(
            "generated_scripts",
            exist_ok=True
        )

        filepath = (
            f"generated_scripts/{filename}"
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(script_code)

        return filepath