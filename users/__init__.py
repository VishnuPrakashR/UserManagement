#  Copyright (c) 2023. This is the property of Vishnu Prakash
import json

from db import Mongo
from encryption import Password


class users:
    def __init__(self):
        self.user = Mongo(self.collection)
        self.email = None
        self.password = None
        self.data = {}

    def login(self, email, password):
        data = self.user.getone({"status": 1, "email": email, "userType": self.userType})
        if data:
            if Password().verify(password, data.get("password")):
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

    def register(self):
        self.data.update({
            "email": self.email,
            "password": Password().encrypt(self.password),
            "userType": self.userType,
            "status": 1
        })
        result = self.user.put(self.data)
        response = {
            "Id": format(result.inserted_id)
        }
        return response
