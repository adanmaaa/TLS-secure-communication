import os
os.chdir("C:/Users/Nzube_p5digzb/documents/saittt/project2")
print (os.getcwd())
import socket
import ssl

def start_tls_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(('127.0.0.1', 13000))
        sock.listen(5)
        print("TLS server listening on port 13000...")

        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            print(f"Connection from {addr}")
            data = conn.recv(1024).decode()
            print(f"Received: {data}")
            response = "Even" if data.isdigit() and int(data) % 2 == 0 else "Odd"
            conn.send(response.encode())
            conn.close()

if __name__ == "__main__":
    start_tls_server()