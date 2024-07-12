with open("fileToBeRead.txt", "r+") as f:
    fileToBeReadContents = f.read()
    print(fileToBeReadContents)

print()
print("Reading Done")
print()

f = open("fileToBeRead.txt", "r")
fileTBRC = f.read()
if fileTBRC == "Hello Logan!":
    f = open("fileToBeRead.txt", "w")
    f.write("Well Hello!")
else:
    f = open("fileToBeRead.txt", "w")
    f.write("Hello, Somebody.")

print("Processing and Writing Done")
