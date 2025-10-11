fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    _days = {}
    for line in fhandle:
        if line.startswith("From "):
            words = line.split()
            _day = words[2]
            _days[_day] = _days.get(_day, 0) + 1
    print(_days)
except:
    print("File cannot be opened:", fileName)
    exit()
