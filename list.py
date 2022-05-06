# list
values = [1, 2, "Subhan", 3.4, 4, 6]

# get value at first index
print(values[0])
# last index of the list
print(values[-1])
# print values from index of 1 to 3
print(values[1:3])
# insert in between list
values.insert(3, "Ihsan")
print(values)
# add value in the end of the list
values.append("end")
print(values)
# update the value at some index
values[2] = "subhan"
print(values)
# delete a value
del values[0]
print(values)
# tuple cannot be changed
a = (1, 2, 3, "Subhan")
print(a)
print(a[1])
# Dictionary
dict = {
    1: "First Name",
    2: "Second Name",
    "age": 27
}
print(dict["age"])
# pass values into a dictionary
dict_test = {

}
dict_test["First Name"] = "Subhan"
dict_test["Second Name"] = "Ihsan"
print(dict_test)
