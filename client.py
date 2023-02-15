import socket
import types

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"gAAAAABj7H5-YRWPrBAFvJ9NRJ0OhxnbGfsMUQqs9Rmxqz1K35MiHaIPlLQ-aB1wUMchqT-JqS0kQbmgsc2IjMB0AYBHnG4RLJNKijar4sHDVFIbDF3Qpb8=.decrypt")
    full_output = ''
    while True:
        output = s.recv(1024)
        if len(output) <= 0:
            break
        full_output += output.decode()
        print(f"got{full_output!r}")
