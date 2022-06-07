from json import dumps
from faker import Faker
import collections
import json
import random_date_generator
import random_name_generator
import random_title_generator


def blog_post_generator(how_much):
    for x in range(how_much):
        yield {'Post_Author:': random_name_generator.random_name(),
               'Added': random_date_generator.random_date(),
               'Post_Title': random_title_generator.random_title(),
               'index': x}


filename = 'blog_posts'
length = 10 #todo: make global var
blog_posts = blog_post_generator(length)
with open('%s.json' % filename, 'w') as output:
    output.write('[')  # to made json file valid according to JSON format
    for blog_post in blog_posts:
        json.dump(blog_post, output)
    output.write(']')  # to made json file valid according to JSON format
