fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    templst = line.split()
    for i in range(len(templst)):
        if templst[i] in lst : continue
        lst.append(templst[i])
#lst.sort()
print(lst)
