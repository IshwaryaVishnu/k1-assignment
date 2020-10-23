import json
para =  '{ "Name":"Iswarya", "Code":"9", "Age":28 }'
Emp_details = json.loads(para)
print("\nJSON data:")
print(Emp_details)
print("\nName: ",Emp_details["Name"])
print("Class: ",Emp_details["Code"])
print("Age: ",Emp_details["Age"])









