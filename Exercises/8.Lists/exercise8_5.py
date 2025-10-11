fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    count = 0
    for line in fhandle:
        if line.startswith('From '):
            line = line.rstrip()
            count = count + 1
            words = line.split()
            print(words[1])
    print("There were ", count , "lines in the file with From as the first word")
except:
    print("File cannot be opened:", fileName)
    exit()