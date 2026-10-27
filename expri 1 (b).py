import socket

s = socket.socket()

host = socket.gethostname()
print("Server will start on host:", host)

port = 8080
s.bind((host, port))

print()
print("Waiting for connection...")
print()

s.listen(1)

conn, addr = s.accept()

print(addr, "has connected to the server")
print()

while True:
    message = input(">> ")

    if message.lower() == "exit":
        conn.close()
        break

    conn.send(message.encode())
    print("Sent")
    print()

    incoming_message = conn.recv(1024).decode()

    if not incoming_message:
        print("Client disconnected.")
        break

    print("Client:", incoming_message)
    print()

s.close()