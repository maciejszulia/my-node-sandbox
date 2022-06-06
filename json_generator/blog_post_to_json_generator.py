from genson import SchemaBuilder
from random_date import random_date_generator
from random_name import random_name_generator
from random_title import random_title_generator

builder = SchemaBuilder()
builder.add_schema({"Post title", "Author", "Added"})