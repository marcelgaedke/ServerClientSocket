import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(socket.gethostname(),12345)
print(f"Binding {socket.gethostname()}")
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} established")
    clientsocket.send(bytes("Welcome","utf-8"))