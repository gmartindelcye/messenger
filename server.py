# Import required modules
from concurrent.futures import thread
from email import message
from http import client
import socket
import threading
from urllib import response

HOST = '127.0.0.1'
PORT = 6543
LISTENER_LIMIT = 5
MSG_MAX_LENGHT = 2048

active_clients = [] # all connected users 


# Listen from upcoming messages from a client
def listen_for_messages(client, username):

    while True:
        response = client.recv(MSG_MAX_LENGHT).decode('utf-8')
        if response != "":
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print(f"The message sent from client {username} is empty!")


# send message to a specific client
def send_message_to_client(client, message):
    client.sendall(message.encode())           


# send message from user to all users connected
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)


# Client handler function
def client_handler(client):
    
    # Server listen for client message with username
    while True:
        username = client.recv(MSG_MAX_LENGHT).decode('utf-8')
        if username != "":
            active_clients.append((username, client))
            break
        else:
            print("Client username is empty!")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()


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

        threading.Thread(target=client_handler, args=(client, )).start()


if __name__ == "__main__":
    main()