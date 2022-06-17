# Import required modules
from http import client
import socket
import threading

HOST = '127.0.0.1'
PORT = 6543
LISTENER_LIMIT = 5

# main function
def main():
    # creating socket class object
    # AF_INET = ipv4
    # SOCK_STREAM = tcp 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST,PORT))
        print(f"Running server on {HOST} port {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # set server limit
    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        print(f"Succesfully conected to client {address[0]} {address[1]}")
if __name__ == "__main__":
    main()