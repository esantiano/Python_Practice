fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    _emails = {}
    for line in fhandle:
        if line.startswith("From "):
            words = line.split()
            _email = words[1]
            _emails[_email] = _emails.get(_email, 0) + 1
    print(_emails)
except:
    print("File cannot be opened:", fileName)
    exit()