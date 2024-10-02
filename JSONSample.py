import json

#json_Str = '{"students": [{"name": "John", "age": 20, "grade": "A"}, {"name": "Alice", "age": 18, "grade": "B"}]}'

json_Str = input("Enter json string")

data = json.loads(json_Str)

for d in data["students"]:
    print(f"Name :", d["name"])
    print(f"Age :", d["age"])
    print(f"Grade :", d["grade"])