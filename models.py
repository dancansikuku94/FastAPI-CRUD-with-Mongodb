# File to create models
from mongoengine import StringField ,IntField ,ListField,Document

# Defining model schema
class Employee(Document):
    emp_id  = IntField(max_value=10)
    name = StringField(max_length=255)
    dept = StringField(max_length=255)
    age = IntField(max_value=10)




