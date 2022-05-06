# open any text file
file = open('test.txt')
# read all the contents of the file
print(file.read())
# only read first 2 letters
print(file.read(2))
# read the file line by line
print(file.readline())
# print line by line read all the lines
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
# alternate way to read all the lines
for line in file.readlines():
    print(line)
# close file
file.close()