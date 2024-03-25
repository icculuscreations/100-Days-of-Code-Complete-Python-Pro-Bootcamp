# # dumb way
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# read the file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write to the file "w" = write (this will replace everything in file if present)
with open("my_file.txt", "w") as file:
    file.write("My name is Bob")

# add to the file "a" = append (this will add to anything already in the file)
with open("my_file.txt", "a") as file:
    file.write("\n I am 33 years old")



