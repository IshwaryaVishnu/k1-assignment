import json
keys =["Iswarya", "Anjali","Swetha","Sweety"]
values =["python", "Java","salesforce", "devops"]
data = dict(zip(keys,values))
print(data)
print("\nJSON data:")
print(json.dumps(data, sort_keys=True, indent=4))











