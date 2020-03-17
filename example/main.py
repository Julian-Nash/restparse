from restparse.parser import Parser


parser = Parser(description="RESTful parameter parser")

parser.add_param(name="name", type=str, description="The users name", required=True)
parser.add_param(name="age", type=int, description="The users age", required=True)
parser.add_param(
    name="online", type=bool, description="Is the user online?", default=False
)
parser.add_param(
    name="height", type=float, description="The users height",
)
parser.add_param(
    name="tags", description="Tags",
)

payload = {
    "name": "John Doe",
    "age": "40",
    "online": False,
    "height": 6.2,
    "tags": ["python", "javascript"],
}

params = parser.parse_params(payload)

print(params.name)  # John Doe
print(params.tags)  # ['python', 'javascript']

print(
    params.to_dict()
)  # {'name': 'John Doe', 'age': 40, 'online': False, 'height': 6.2, 'tags': ['python', 'javascript']}
