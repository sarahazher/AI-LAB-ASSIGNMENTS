import socket
import os

def send_file(filename, target_host, target_port):
    try:
        udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        with open(filename, 'rb') as file:
            data = file.read(1024)
            while data:
                udp_client.sendto(data, (target_host, target_port))
                data = file.read(1024)

        print(f"File '{filename}' sent successfully.")
        udp_client.close()
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    target_host = "127.0.0.1"  # Replace with the receiver's IP address
    target_port = 12345  # Receiver's port number

    # Send script file
    send_file("script.py", target_host, target_port)

    # Send text file
    send_file("text_file.txt", target_host, target_port)

    # Send audio file (e.g., .wav)
    send_file("audio.wav", target_host, target_port)

    # Send video file (e.g., .mp4)
    send_file("video.mp4", target_host, target_port)

if __name__ == '__main__':
    main()
