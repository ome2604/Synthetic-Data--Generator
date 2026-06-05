from faker import Faker

fake = Faker()

for _ in range(5):
    print({
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email()
    })