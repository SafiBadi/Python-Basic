fname = input("Enter file name : ")
fhand = open(fname)
counts = dict()
for line in fhand:
    if line.startswith("From "):
        hour = line.split()[5].split(':')[0]
        counts[hour] = 1 + counts.get(hour,0)
for k,v in sorted(counts.items()):
    print(k,v)
