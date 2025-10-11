fileName = input("Enter a file name: ")
try:
    fhandle = open(fileName)
    unique_words = list()
    for line in fhandle:
        words = line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    print(sorted(unique_words))
except:
    print("File cannot be opened:", fileName)
    exit()