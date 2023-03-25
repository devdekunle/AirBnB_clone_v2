#!/usr/bin/python3
"""
This module contains the class that defines all common attributes/methods
for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This class creates the BaseModel class which acts as a super class for
    other classes to be used in the application
    """

    def __init__(self, *args, **kwargs):
        """Method for object instantiation of the BaseModel"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value


class Test(BaseModel):

    name = "samuel"
    size = 5
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)


inst_test = Test(name="olamide", size=7, height=23, weight=45)

print(inst_test.name)
print(inst_test.size)
print(inst_test.height)
print(inst_test.weight)

inst_test1 = Test()

print(inst_test1.name)
print(inst_test1.size)
