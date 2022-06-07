import datetime

from faker import Faker

fake = Faker()


def random_date_generator(since: int) -> datetime:
    since = "-" + str(since) + "y"
    return fake.date_time_between(start_date=since, end_date='now')


print(random_date_generator(10))
