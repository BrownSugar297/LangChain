from typing import TypedDict, Optional

class Person(TypedDict):
    name : str
    age : Optional[int]

new_person : Person = {"name" : "Ashik", "age" : 25}
new_person2 : Person = {"name" : "Ashik"}

print(new_person)
print(new_person2)

# TypeDict does not do data validation, so if you don't give exact data type there is no problem