# Import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 6543

def main():
    # creating socket class object
    # AF_INET = ipv4
    # SOCK_STREAM = tcp 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    try:
        client.connect((HOST,PORT))
        print(f"Client connected to server {HOST} port {PORT}")
    except:
        print(f"Unable to connect to server {HOST} port {PORT}")


if __name__ == "__main__":
    main()
