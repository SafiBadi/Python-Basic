# find maximum mail recived
# dictonary

fname = input("Enter file name : ")
fhand = open(fname)

counts = dict()

for line in fhand:
    if line.startswith("From "):
        word = line.split()
        counts[word[1]] = counts.get(word[1],0) + 1

maxmail = None
maxcount = None

for mail,count in counts.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxmail = mail

print(maxmail,maxcount)
