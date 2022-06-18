# Import required modules
from email import message
from pydoc import cli
import socket
import threading

HOST = '127.0.0.1'
PORT = 6543
MSG_MAX_LENGHT = 2048


def listen_for_messages_from_server(client):
    while True:
        message = client.recv(MSG_MAX_LENGHT).decode('utf-8')
        if message != "":
            username = message.split('~')[0]
            content = message.split('~')[1]
            print(f"[{username}]: {content}")
        else:
            print("Message recieved from clients empty")


def send_message_to_server(client):
    while True:
        message = input("Message: ")
        if message != "":
            client.sendall(message.encode())
        else:
            print("Empty message! Exiting...")
            exit(0)


def communicate_to_server(client):

    username = input("Enter username: ")
    if username != "":
        client.sendall(username.encode())
    else:
        print("Username cannot be empty!")
        exit(0)

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    send_message_to_server(client)



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

    communicate_to_server(client)


if __name__ == "__main__":
    main()
