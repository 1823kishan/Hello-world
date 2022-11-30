import socket
name = socket.gethostname()
ip = socket.gethostbyname(name)
print(f"name : {name}")
print(f"ip : {ip}")
