import socket
import service

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            print(f"got {data}")
            output = bytes(service.crypt_service(data))
            if not data:
                break
            conn.sendall(output)
            print(f"sent {output}")
        conn.close()
