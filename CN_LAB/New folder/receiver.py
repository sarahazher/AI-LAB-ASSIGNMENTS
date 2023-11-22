import socket

def receive_file(filename, port):
    try:
        udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_server.bind(("0.0.0.0", port))

        with open(filename, 'wb') as file:
            print(f"Waiting to receive '{filename}'...")
            while True:
                data, addr = udp_server.recvfrom(1024)
                if not data:
                    break
                file.write(data)

        print(f"File '{filename}' received and saved.")
        udp_server.close()
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    port = 12346  # Use a different port number for the receiver

    # Receive script file
    receive_file("received_script.py", port)

    # Receive text file
    receive_file("received_text_file.txt", port)

    # Receive audio file
    receive_file("received_audio.wav", port)

    # Receive video file
    receive_file("received_video.mp4", port)

if __name__ == '__main__':
    main()
