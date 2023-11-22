import socket

def client_program():
    host = "127.0.0.1"  # Server's IP address
    port = 12345  # Port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    file_names = ["text_file.txt", "audio_file.mp3", "video_file.mp4"]

    for file_name in file_names:
        try:
            with open(file_name, 'rb') as file:
                file_data = file.read()
                client_socket.sendto(file_data, (host, port))

            print(f"File '{file_name}' sent successfully")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")

    client_socket.close()

if __name__ == '__main__':
    client_program()
