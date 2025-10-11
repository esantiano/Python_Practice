import re
fileName = input("Enter a file name: ")
handle = open(fileName)
print("handle",handle)
total = 0
count = 0
regex = '^New.*Revision: ([0-9]+)'
for line in handle:
    line = line.rstrip()
    y = re.findall(regex, line)
    if (len(y)>0):
        count += 1
        total += int(y[0])
print (int(total/count))
exit()