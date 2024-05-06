from faker import Faker

fake = Faker()


def first_name() -> str:
    return fake.first_name()


def last_name() -> str:
    return fake.last_name()


def phone() -> str:
    return fake.msisdn()


def email() -> str:
    return fake.email()
