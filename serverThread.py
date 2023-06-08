import socket
import threading

count = 0


def handle_client(conn, addr, server_name, server_number):
    print(f"New connection from {addr}")
    with conn:
        while True:
            global count
            data = conn.recv(2048).decode()
            if not data:
                break
            client_name, client_number = data.split(",")
            if int(client_number) > 100 or int(client_number) < 0:
                break
            client_name, client_number = data.split(",")
            print(f"# {count}  {client_name} connected to {server_name}")
            print(f"Client's Number: {client_number}")
            sum = int(client_number) + server_number
            print(f"{client_number} + {server_number} = {sum}")
            modifiedMessage = f"{server_name},{server_number}"
            conn.sendall(modifiedMessage.encode())
            count += 1


def start_server():
    HOST = "192.168.109.22"
    PORT = 8000
    server_name = "Server of Youssef Elharty"
    server_number = 42
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(
                target=handle_client, args=(conn, addr, server_name, server_number)
            )
            thread.start()


if __name__ == "__main__":
    start_server()
