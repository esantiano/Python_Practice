fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    _messages = {}
    for line in fhandle:
        if line.startswith("From "):
            words = line.split()
            _email = words[1]
            _messages[_email] = _messages.get(_email, 0) + 1
    lst = list()
    for email, count in _messages.items():
        newtup = (count,email)
        lst.append(newtup)
    lst = sorted(lst, reverse=True)
    for count, email in lst[:1]:
        print(email, count)
except:
    print("File cannot be opened:", fileName)
    exit()