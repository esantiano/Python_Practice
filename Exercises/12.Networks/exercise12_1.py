import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
link = input('Enter link: ')
try:
    host = link.split('/')[2]
    mysock.connect((host, 80))
    cmd = f'GET {link} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
except: 
    print('Invalid link')
mysock.close()
