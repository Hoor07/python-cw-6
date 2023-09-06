person = { 
         "name": "hoor",
         "age": "24",
        "hobbies":["playing piano" , 'shopping' ,'swimming']
}
print(person ["name"])
print(person["age"])

person["age"]=14
person["country"]=["russia"]
print(person)
print(len(person))
person["hobbies"].append('runing')
print(person)
def check_hobbies (person):
    if len(person["hobbies"]) > 3 :
        print("WOW YOU ARE AMAZING")   
    else: 
         print("add more hobbiess")    
check_hobbies (person)