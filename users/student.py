#  Copyright (c) 2023. This is the property of Vishnu Prakash
from . import users


class student(users):
    def __init__(self):
        self.collection = 'users'
        self.userType = 'STUDENT'
        super().__init__()

    def register(self, formData):
        studentId = formData.get('studentId')
        self.email = formData.get('email')
        self.password = formData.get('password')
        self.data.update({
            "studentId": studentId
        })
        response = super().register()
        response.update({
            'studentId': studentId
        })
        return response


