from fastapi import FastAPI , Path 
import uvicorn
from mongoengine import connect
from pydantic import BaseModel
import json
from models import Employee


app=FastAPI()

# Establishing connection
connect(db="hrm",host="localhost",port=27017)

# Serializer
class NewEmploee(BaseModel):
    emp_id : int
    name : str
    dept : str
    age : int

# Default route
@app.get("/")
def index():
    return {"message":"welcome to fastapi with mongodb"}

# Route to get all employee details
@app.get("/get_all_employees")
def get_all_employees():
    employee = json.loads(Employee.objects().to_json())
    return {"employees":employee } 

# Route to get employee by id
@app.get("/get_employee/{emp_id")
def get_employee(emp_id : int = Path(...,gt=0)):
    employee = Employee.objects.get(emp_id=emp_id)
    employee_dict = {
        "emp_id":employee.emp_id,
        "name":employee.name,
        "dept":employee.dept,
        "age":employee.age }
    return employee_dict

# Creating an employee
@app.post("/add_employee")
def add_employee(employee: NewEmploee):
    new_employee = Employee(emp_id=employee.emp_id,
                            name=employee.name,
                            dept=employee.dept,
                            age=employee.age)
    new_employee.save()
    return {"message":"Employee added succesfully"}



