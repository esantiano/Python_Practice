import urllib.request
link = input("Enter - ")
try:
    fhand = urllib.request.urlopen(link)
    char_count = 0
    for line in fhand:
        words = line.decode().strip().split()
        for word in words:
            for char in word:
                if char_count < 3000:
                    print(char)
                    char_count += 1
    print(f"\nCharacter count: {char_count}")
except:
    print("Invalid link")
    quit()