from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = f"{request.args['name']}"
    print(f"Name is {name}")
    return f"Hello World{name} <br/> TEST"


if __name__ == '__main__':
    app.run(port=3231)
