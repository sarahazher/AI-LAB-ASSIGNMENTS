import socket

def server_program():
    host = "127.0.0.1"  # Server's IP address
    port = 12345  # Port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for a single client

    print("Server is waiting for a connection...")
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    # Send a welcome message to the client
    conn.send("Hello from the server!".encode())

    # Receive a "Hello" message from the client
    message = conn.recv(1024)
    print(f"Received message from client: {message.decode()}")

    # Receive a file from the client
    file_name = "file_to_send.txt"
    with open(file_name, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

    print("File received and saved as", file_name)
    conn.close()

if __name__ == '__main__':
    server_program()
