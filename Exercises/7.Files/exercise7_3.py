fileName = input("Enter a file name: ")
try:
   
    fhandle = open(fileName, 'r')
    count = 0
    for sequence in fhandle:
        sequence = sequence.lower()
        if sequence.startswith('subject:'):
            count +=1 
    print ('There were ',count, ' subject lines in ', fileName)
except:
    if (fileName == "na na boo boo"):
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    else:
        print("File cannot be opened:", fileName)
        exit()