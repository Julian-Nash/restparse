from flask import Flask, request, jsonify, redirect, url_for
from restparse.parser import Parser


app = Flask(__name__)


@app.route("/")
def index():
    """ Parsing query strings """

    parser = Parser(description="Parsing query strings")

    parser.add_param(
        "q_from",
        type=int,
        description="Query from"
    )
    parser.add_param(
        "q_to",
        type=int,
        description="Query to"
    )
    parser.add_param(
        "search",
        type=str,
        description="Search query"
    )
    params = parser.parse_params(request.args)

    print(params.q_from)
    print(params.q_to)
    print(params.search)

    return f"Params = from: {params.q_from}, to: {params.q_to}, search: {params.search}"


@app.route("/json", methods=["POST"])
def json_payload():
    """ Parsing request payloads """

    parser = Parser(description="Parsing a request payload")

    parser.add_param(
        "name",
        type=str,
        description="The users name",
        required=True
    )
    parser.add_param(
        "age",
        type=int,
        description="The users age",
        required=True
    )
    parser.add_param(
        "tags",
        type=list,
        description="Tags"
    )
    params = parser.parse_params(request.get_json())

    print(params.name)
    print(params.age)
    print(params.tags)

    return jsonify(params.to_dict())


@app.route("/form", methods=["POST"])
def form_payload():
    """ Parsing form data """

    parser = Parser(description="Parsing form data")

    parser.add_param(
        "name",
        type=str,
        description="The users name",
        required=True
    )
    parser.add_param(
        "age",
        type=int,
        description="The users age",
        required=True
    )
    params = parser.parse_params(request.form)

    print(params.name)
    print(params.age)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
