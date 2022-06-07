import random
import string


# todo: make it spit out words not this random garbage


def random_title(title_len=25) -> str:
    letters = string.ascii_letters
    title = "".join(random.sample(letters, random.randint(1, title_len)))
    return title

# for i in range(10):
#     print(random_title_generator(10))
