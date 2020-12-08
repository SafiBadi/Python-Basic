fname = input('Enter fname : ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("From "):
        email = line.split()
        print(email[1])
        count = count + 1
print("There were",count,"lines in the file with From as the first word")
