fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName, 'r')
    for sequence in fhandle:
        sequence = sequence.strip()
        print(sequence.upper())
except:
    print("File cannot be opened:", fileName)
    exit()