fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    _domains = {}
    for line in fhandle:
        if line.startswith("From "):
            words = line.split()
            _email = words[1]
            _domain = _email.split('@')[1]
            _domains[_domain] = _domains.get(_domain, 0) + 1
    print(_domains)
except:
    print("File cannot be opened:", fileName)
    exit()