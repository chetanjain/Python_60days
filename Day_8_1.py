# with open("files/doc.txt", 'r') as file:
#     data = file.read()

# with open("files/doc.txt") as file:  # by default mode is read.
#     print(file.read())

# ls = "Hello You"
# with open("file.txt",'w') as file:
#     file.write(ls)

with open('file.txt') as file:
    # print(file.read())
    # print(len(file.read())) # this will give 0 as output because file.read put the cursor at the end.
    # Since the cursor is at end so length will be 0
    data = file.read()

print(data)
print(len(data))
