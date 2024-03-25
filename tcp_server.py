import socket
import threading

# Define the IP address and port to listen on
# I tell IP to listen on all interfaces, that`s why 0.0.0.0
IP = '0.0.0.0'
# My TCP client is connecting in this same port
PORT = 9998

# Main function to start the server
def main():
    # Create a TCP socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the IP address and port
    server.bind((IP,PORT))
    # Listen for incoming connections for up to five connections simultaneously
    server.listen(5)

    print(f'[*] Listening on {IP}:{PORT}')

    # Loop to accept continuosly handle requests. Here is where important stuff happens
    while True:
        # Accept a new connection and get the client socket and address
        client, address = server.accept()

        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        # Create a thread object to handle comm with the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # Start the thread
        client_handler.start()

# Function to handle comm with a client
def handle_client(client_socket):
    # Use a context manager to ensure the socket is closed
    with client_socket as sock:
        # Receive data from the client
        request = sock.recv(1024)

        print(f'[*] Received: {request.decode("utf-8")}')

        # Send a simple acknowledgment back to the client
        sock.send(b'ACK')

# Check if the script is being run directly.
# If this python script here is running, then execute the main function
if __name__ == '__main__':
    # Call the main function to start the server
    main()