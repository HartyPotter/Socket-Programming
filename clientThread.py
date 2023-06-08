import socket


def start_client():
    HOST = "192.168.43.166"
    PORT = 8000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            # Receive integer from user
            client_number = int(input("Enter an integer between 1 and 100: "))

            # Define client name
            client_name = "Client of Youssef Elharty"

            # Send client name and integer to server
            message = f"{client_name},{client_number}"
            print(message.split())
            s.send(message.encode())
            data = s.recv(1024).decode()
            server_name, server_number = data.split(",")
            print(f"{client_name} connected to {server_name}")
            sum = int(server_number) + client_number
            print(
                f"Client number: {client_number}\nServer number: {server_number}\nSum: {sum}"
            )

            # Close client connection
            s.close()
            break


if __name__ == "__main__":
    start_client()