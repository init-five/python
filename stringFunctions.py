str = "I am learning Automation"
str1 = "I'm hoping to learn it fast"
str2 = "Automation"
str3 = "RahulshettyAcademy.con"
# print first letter of string
print(str[0])
# print from 0 to 4 index (0-n-1)
print(str[0:5])
# concatenate 2 strings
print(str + " " +str1)
# check if str2 is present in str
print(str2 in str)
# split the string
var = str3.split(".")
print(var)
print(var[0])
# removing whitespaces at the beginning or end
str4 = " great "
print(str4.strip())
# only remove blank space from left
print(str4.lstrip())
# only remove blank space from right
print(str4.rstrip())