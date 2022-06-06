import json
from genson import SchemaBuilder

builder = SchemaBuilder()
with open("blog_posts.json", 'r') as f:
    datastore = json.load(f)
    builder.add_object(datastore)

builder.to_schema()
