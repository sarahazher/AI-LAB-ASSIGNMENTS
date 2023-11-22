import socket

def ip_to_url(ip_address):
    try:
        return f"IP Address: {ip_address} resolves to URL: {socket.gethostbyaddr(ip_address)[0]}"
    except socket.herror:
        return f"Unable to resolve IP Address: {ip_address}"

def url_to_ip(url):
    try:
        return f"URL: {url} resolves to IP Address: {socket.gethostbyname(url)}"
    except socket.gaierror:
        return f"Unable to resolve URL: {url}"

def main():
    while True:
        print("DNS Lookup Options:")
        print("1. IP to URL")
        print("2. URL to IP")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            result = ip_to_url(input("Enter the IP address: "))
        elif choice == '2':
            result = url_to_ip(input("Enter the URL: "))
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        print(result)

if __name__ == '__main__':
    main()
