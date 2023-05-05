#  Copyright (c) 2023. This is the property of Vishnu Prakash
from datetime import timedelta

import redis
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from users.student import student
from API import verification

app = Flask(__name__)

jwt = JWTManager(app)

ACCESS_EXPIRES = timedelta(days=5)
REFRESH_EXPIRES = timedelta(days=30)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt_redis_blocklist = redis.StrictRedis(
    host="localhost", port=6379, db=0, decode_responses=True
)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.update(
    SECRET_KEY=b'\xa8G\x1c\x84@EQ\xdd\xa2\xf8\xe2\xed\x9e\x9ft\x8f'
)
CORS(app, expose_headers="content-disposition", supports_credentials=True)


@app.route("/")
def hello():
    return "UserManagement API"


@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    apiKey = request.headers.get("X-API-Key")
    referer = request.headers.get("Referer")
    apiResponse = verification().verify(apiKey, referer)
    if apiResponse.get("Verified"):
        email = request.form.get('email')
        password = request.form.get('password')
        response = student().login(email, password)
        if response.get("Response") == "Success":
            studentId = response.get("studentId")
            access_token = create_access_token(identity=studentId, expires_delta=ACCESS_EXPIRES)
            refresh_token = create_refresh_token(identity=studentId, expires_delta=REFRESH_EXPIRES)
            response.update({
                "AccessToken": access_token,
                "RefreshToken": refresh_token
            })
    else:
        response = jsonify({"Response": apiResponse.get("Msg")}), 401
    return response


@app.route('/student/current', methods=['GET', 'POST'])
@jwt_required()
def current_student():
    apiKey = request.headers.get("X-API-Key")
    referer = request.headers.get("Referer")
    apiResponse = verification().verify(apiKey, referer)
    if apiResponse.get("Verified"):
        user_id = get_jwt_identity()
        response = jsonify({"Response": "Success", "studentId": user_id})
    else:
        response = jsonify({"Response": apiResponse.get("Msg")}), 401
    return response


def run():
    app.run(host="0.0.0.0", port=5002, debug=True, load_dotenv='development')


if __name__ == "__main__":
    run()
