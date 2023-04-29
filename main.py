#  Copyright (c) 2023. This is the property of Vishnu Prakash

from flask import Flask, request
from flask_cors import CORS
from format import JSONEncoder as jsone

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.update(
    SECRET_KEY=b'\xa8G\x1c\x84@EQ\xdd\xa2\xf8\xe2\xed\x9e\x9ft\x8f'
)
CORS(app, expose_headers="content-disposition", supports_credentials=True)


@app.route("/")
def hello():
    return "UserManagement API"


@app.route('/<path:path>', methods=['GET', 'POST'])
def user(path):
    return jsone().encode({"Path": path})


def run():
    app.run(host="0.0.0.0", port=5002, debug=True, load_dotenv='development')


if __name__ == "__main__":
    run()
