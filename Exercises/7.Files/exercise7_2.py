fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName, 'r')
    count = 0
    num = 0
    for sequence in fhandle:
        sequence = sequence.strip()
        if sequence.startswith('X-DSPAM-Confidence:'):
            count +=1 
            num += float(sequence[20:])
    print ("Average spam confidence: ",float(num/count))
except:
    print("File cannot be opened:", fileName)
    exit()