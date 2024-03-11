import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    while True:
        # Input message from user
        message = input("Enter message: ")
        
        # Send message to server
        client.send(message.encode('utf-8'))

        # Receive acknowledgment from server
        response = client.recv(1024).decode('utf-8')
        print("Server says:", response)

    client.close()

if __name__ == "__main__":
    start_client()
