import re
regex = input("Enter a regular expression: ")
handle = open("/Users/ericsantiano/Python_Practice/Exercises/Exercise_Files/mbox.txt")
count = 0
for line in handle:
    line = line.rstrip()
    if re.search(regex, line):
        count += 1
print(f'mbox.txt had {count} lines that matched {regex}')
exit()