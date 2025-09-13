import socket


def connect_to_server(host='localhost', port=12345):
    """
    Connects to the server and receives the greeting message.
    """
    client_socket = None
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Receive data from server
        data = client_socket.recv(1024)  # Buffer size of 1024 bytes
        if data:
            message = data.decode('utf-8')
            print(f"Received: '{message}'")
        else:
            print("No data received.")

    except ConnectionRefusedError:
        print("Connection refused. Is the server running?")
    except socket.gaierror:
        print(f"Cannot resolve hostname '{host}'. Check the address.")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if client_socket:
            client_socket.close()
            print("Client socket closed.")


if __name__ == "__main__":
    connect_to_server()