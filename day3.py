#Lists-Tuples-Sets
colors = ("red", "green", "blue")

print(colors[0])
print(colors[-1])
#colors[1] = "yellow"

print("                                   ")

numbers = {1,2,3,3,2,1}
print(numbers)

print("                                   ")

fruits_set = {"apple","banana","apple","banana"}
print(fruits_set)

print("                                   ")
print("                                   ")


#Dictionaries

student = {
    "name": "Kasun",
    "age": 17,
    "city": "Negombo"
}

print(student["name"])
print(student["age"])

student["age"] = 18
print(student["age"])

student["school"] = "ABC"
print(student["school"])

print("                                   ")
print("                                   ")

print(student.keys())
print(student.values())