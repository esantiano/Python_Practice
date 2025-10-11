fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    _letters = {}
    for line in fhandle:
        line = line.rstrip().lower()
        for letter in line:
            if letter.isalpha():
                _letters[letter] = _letters.get(letter, 0) + 1
    lst = list()
    for letter, count in _letters.items():
        newtup = (letter, count)
        lst.append(newtup)
    lst = sorted(lst)
    for letter, count in lst:
        print(letter, count)
except:
    print("File cannot be opened:", fileName)
    exit()