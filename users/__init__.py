#  Copyright (c) 2023. This is the property of Vishnu Prakash
import json

from db import Mongo
from encryption import Password


class users:
    def __init__(self):
        self.user = Mongo(self.collection)

    def login(self, email, password):
        data = self.user.getone({"Status": 1, "Email": email})
        if data:
            if Password().verify(password, data.get("Password")):
                response = {
                    "Response": "Success",
                    "studentId": data.get("studentId")
                }
            else:
                response = json.dumps({
                    "Response": "Error",
                    "Msg": "Wrong Password"
                }), 401
        else:
            response = json.dumps({
                "Response": "Error",
                "Msg": "User Not Found"
            }), 401
        return response
