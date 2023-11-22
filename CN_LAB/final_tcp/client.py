import socket

def client_program():
    host = "127.0.0.1"  # Server's IP address
    port = 12345  # Port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive a welcome message from the server
    message = client_socket.recv(1024)
    print(message.decode())

    # Send a "Hello" message to the server
    hello_message = "Hello from the client!"
    client_socket.send(hello_message.encode())
    print("Sent 'Hello' message to server")

    file_name = "file_to_send.txt"
    try:
        with open(file_name, 'rb') as file:
            for data in file:
                client_socket.send(data)

        print("File sent successfully")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

    client_socket.close()

if __name__ == '__main__':
    client_program()
