import os

#reading the whole file
f = open("day-1/demo.txt", "r")
# print(f.read())

#reading only the parts of the file

f = open("day-1/demo.txt", "r")
# print(f.read(5))#returns the first 5 characters

#reading a line
f = open("day-1/demo.txt", "r")
# print(f.readline())#returns the first line
# print(f.readline())#returns the first 2 line

#loop through the file line by line

f = open("day-1/demo.txt", "r")
for line in f:
    # print(line)
    pass

#closing the file
f.close()

#writing to the file

f = open("day-1/demo2.txt", "w")
f.write("lets add some new content to the file by overriding the existing content")
f.close()

#open the new file
newFile = open("day-1/demo2.txt", "r")
# print(newFile.read()) 

#lets append some new content to the demo2
f = open("day-1/demo2.txt", "a")
f.write("\nthis is a new line")
f.close()

#read the appended file contents

newFile = open("day-1/demo2.txt", "r")
# print(newFile.read())

#delete a file
# os.remove("day-1/deleted.txt")

newFile = open("day-1/deleted.txt", "r")
#check if the file exists
if os.path.exists("day-1/deleted.txt"):
    os.remove("day-1/deleted.txt")
    print("file deleted")
else:
    print("File does not exist")