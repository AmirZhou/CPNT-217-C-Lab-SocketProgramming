import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 35685

s.connect(('localhost', port))
msg = s.recv(1024)

print(msg.decode("utf-8"))