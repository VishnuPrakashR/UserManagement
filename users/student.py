#  Copyright (c) 2023. This is the property of Vishnu Prakash
from . import users


class student(users):
    def __init__(self):
        self.collection = 'students'
        self.userType = 'Student'
        super().__init__()
