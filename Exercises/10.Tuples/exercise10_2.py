fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    _hours = {}
    for line in fhandle:
        if line.startswith("From "):
            words = line.split()
            _time = words[5]
            _hour = _time.split(":")[0]
            _hours[_hour] = _hours.get(_hour, 0) + 1
    lst = list()
    for hour, count in _hours.items():
        newtup = (hour, count)
        lst.append(newtup)
    lst = sorted(lst)
    for hour, count in lst:
        print(hour, count)
except:
    print("File cannot be opened:", fileName)
    exit()