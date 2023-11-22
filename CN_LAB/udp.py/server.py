import socket

def server_program():
    host = "127.0.0.1"  # Server's IP address
    port = 12345  # Port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server is waiting for a connection...")

    file_names = ["received_text_file.txt", "received_audio_file.mp3", "received_video_file.mp4"]

    for file_name in file_names:
        with open(file_name, 'wb') as file:
            while True:
                data, address = server_socket.recvfrom(65536)  # Use larger buffer size
                if not data:
                    break
                file.write(data)

        print(f"File received and saved as {file_name}")

    server_socket.close()

if __name__ == '__main__':
    server_program()
