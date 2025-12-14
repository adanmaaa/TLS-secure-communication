import os
os.chdir("C:/Users/Nzube_p5digzb/documents/saittt/project2")
print (os.getcwd())
import socket
import ssl

def start_tls_client():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # skip verification for self-signed certs

    with socket.create_connection(('127.0.0.1', 13000)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            message = input("Enter a number: ")
            ssock.send(message.encode())
            response = ssock.recv(1024).decode()
            print(f"Server response: {response}")

if __name__ == "__main__":
    start_tls_client()