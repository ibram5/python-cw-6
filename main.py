# write your code here
person = {
    "name": "ibram",
    "age" : 17,
    "hobbies":["football", "reading ", "gaming"]
    
}

print(person['name'])
print(person['age'])
 
 
person["age"] = 18
person["country"] = "Egypt"
print(person)
print(person.values())

person['hobbies'].append("basketball")

def check_hobbies(person):
    if len(person["hobbies"]) > 3:
        print("WOW YOU ARE AMAZING")
        
check_hobbies(person)
        
