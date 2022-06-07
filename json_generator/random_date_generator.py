import datetime

from faker import Faker

fake = Faker()


def random_date(how_old_post_can_be=5) -> datetime:
    how_old_post_can_be = "-" + str(how_old_post_can_be) + "y"
    return str(fake.date_time_between(start_date=how_old_post_can_be, end_date='now'))


# print(random_date_generator(10))
