from faker import Faker

fake = Faker('pl_PL')


# for i in range(5):
#     print(f'{fake.first_name()} {fake.last_name()}')


def random_name() -> str:
    full_name = fake.first_name() + " " + fake.last_name()
    return full_name


# print(random_name())
