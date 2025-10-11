import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
link = input('Enter link: ')
try:
    host = link.split('/')[2]
    mysock.connect((host, 80))
    cmd = f'GET {link} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    char_count = 0
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        words = data.decode().strip().split()
        for word in words:
            for char in word:
                if char_count < 3000:
                    print(char)
                    char_count += 1
    print(f'\nCharacter count: {char_count}')
except: 
    print('Invalid link')
mysock.close()
