fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    _emails = {}
    most_messages = None
    most_messages_email = None
    for line in fhandle:
        if line.startswith("From "):
            words = line.split()
            _email = words[1]
            _emails[_email] = _emails.get(_email, 0) + 1
    for email, count in _emails.items():
        if most_messages is None or count > most_messages:
            most_messages = count
            most_messages_email = email
    print(most_messages_email, most_messages)
except:
    print("File cannot be opened:", fileName)
    exit()