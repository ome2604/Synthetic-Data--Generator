
from faker import Faker
import pandas as pd

fake = Faker()

records = []

for i in range(1, 101):

    record = {

        "patient_id": i,

        "first_name": fake.first_name(),

        "last_name": fake.last_name(),

        "email": fake.email(),

    }

    records.append(record)

df = pd.DataFrame(records)

df.to_csv(
"patients.csv"
,
    index=False
)

print(
"Generated patients.csv"
)
