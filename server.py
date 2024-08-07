import socket
port = 35685

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # IPv6 socket method 1:
# s1 = socket.socket(family=socket.AF_INET6, type=socket.SOCK_STREAM, proto=9999, fileno=None)
# # IPv6 socket method 2:
# s2 = socket.create_connection(("www.amirzhou.io",9999), timeout=10)
# # IPv6 socket method 3:
# s3 = socket.create_server(("www.amirzhou.io",9999), family=socket.AF_INET6, dualstack_ipv6=True)

addr = (socket.gethostname('localhost'))

s.bind((addr, port))

s.listen(5)

print("[+] Server listening...")

while True:
  conn, addr = s.accept()
  print(f'connection to {addr[0]} on {addr[1]}')
  conn.send(bytes("Socket Programming in Python", "utf-8"))

