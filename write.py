# opens and closes file, 'w' to open file in write mode, 'r' to open file in read mode
# read all the lines
# reverse the content
# write the list back to the file
with open('test.txt', 'r') as reader:
    # variable holds the list of all the content in the file
    content = reader.readlines()
    # reverse the list
    reversed(content)
    print(content)
    # open file in the write mode
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

print(content)