import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive message from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print("Received message:", data)
        
        # Send acknowledgment message back to client
        client_socket.send("Message received".encode('utf-8'))

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(5)
    print("Server started, listening on port 5555")

    while True:
        client_socket, client_address = server.accept()
        print("Accepted connection from", client_address)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
