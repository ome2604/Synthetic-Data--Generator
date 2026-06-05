import random
from faker import Faker

fake = Faker()


def generate_value(column_name):
    column_name = column_name.lower()

    # ==================================
    # IDs
    # ==================================
    if column_name == "id":
        return fake.uuid4()

    # ==================================
    # Names
    # ==================================
    elif "first_name" in column_name:
        return fake.first_name()

    elif "last_name" in column_name:
        return fake.last_name()

    elif "full_name" in column_name or column_name == "name":
        return fake.name()

    elif "username" in column_name:
        return fake.user_name()

    # ==================================
    # Authentication
    # ==================================
    elif "password_hash" in column_name:
        return fake.sha256()

    elif "token" in column_name:
        return fake.sha1()

    # ==================================
    # Contact
    # ==================================
    elif "email" in column_name:
        return fake.email()

    elif "phone" in column_name:
        return fake.phone_number()

    # ==================================
    # Address
    # ==================================
    elif "address" in column_name:
        return fake.street_address()

    elif "city" in column_name:
        return fake.city()

    elif "state" in column_name:
        return fake.state()

    elif "country" in column_name:
        return fake.country()

    elif "postal" in column_name:
        return fake.postcode()

    # ==================================
    # URLs
    # ==================================
    elif "url" in column_name:
        return fake.url()

    elif "avatar" in column_name or "image" in column_name:
        return fake.image_url()

    # ==================================
    # Status
    # ==================================
    elif "status" in column_name:
        return random.choice(["ACTIVE", "INACTIVE", "PENDING", "SUSPENDED"])

    # ==================================
    # Country / Currency
    # ==================================
    elif "iso_code" in column_name:
        return fake.country_code()

    elif "currency_code" in column_name:
        return random.choice(["USD", "EUR", "GBP", "INR", "CAD", "AUD"])

    elif "code" in column_name:
        return fake.bothify(text="???-####")

    # ==================================
    # OTT / Streaming
    # ==================================
    elif "subscription" in column_name or "plan" in column_name:
        return random.choice(["Basic", "Standard", "Premium"])

    elif "quality" in column_name:
        return random.choice(["SD", "HD", "Full HD", "4K"])

    elif "language" in column_name:
        return random.choice(["English", "Spanish", "French", "German", "Hindi"])

    # ==================================
    # Dates
    # ==================================
    elif "created_at" in column_name or "updated_at" in column_name:
        return str(fake.date_time())

    elif "date" in column_name:
        return str(fake.date())

    # ==================================
    # Financial
    # ==================================
    elif "price" in column_name:
        return round(random.uniform(10, 1000), 2)

    elif "amount" in column_name:
        return round(random.uniform(1, 50000), 2)

    # ==================================
    # Ratings
    # ==================================
    elif "rating" in column_name:
        return round(random.uniform(1, 5), 1)

    elif "score" in column_name:
        return random.randint(0, 100)

    # ==================================
    # Sports
    # ==================================
    elif "runs" in column_name:
        return random.randint(0, 300)

    elif "wickets" in column_name:
        return random.randint(0, 10)

    elif "overs" in column_name:
        return round(random.uniform(1, 50), 1)

    # ==================================
    # Boolean
    # ==================================
    elif (
        "active" in column_name
        or column_name.startswith("is_")
        or "enabled" in column_name
    ):
        return random.choice([True, False])

    # ==================================
    # Gender
    # ==================================
    elif "gender" in column_name:
        return random.choice(["Male", "Female"])

    # ==================================
    # Text
    # ==================================
    elif "description" in column_name:
        return fake.sentence()

    elif "notes" in column_name:
        return fake.paragraph()

    elif "title" in column_name:
        return fake.sentence(nb_words=4)

    # ==================================
    # Default
    # ==================================
    return fake.word()