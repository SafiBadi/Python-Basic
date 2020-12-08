# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = int(0)
ans = float(0)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count =count+1
    ans = ans + float(line[line.find(':')+1:])

print("Average spam confidence: {:.12f}".format(ans/count))
