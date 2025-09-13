import socket


def start_server(host='localhost', port=12345):
    """
    Starts a TCP server that listens for connections and sends a greeting message.
    """
    server_socket = None
    try:
        # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allow reuse of the address (prevents "Address already in use" error on restart)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the host and port
        server_socket.bind((host, port))

        # Listen for incoming connections (max 1 pending connection)
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")

        while True:
            # Wait for a client to connect
            client_conn, client_addr = server_socket.accept()
            print(f"Connected by {client_addr}")

            try:
                # Send message to client
                message = "Hello from server!"
                client_conn.sendall(message.encode('utf-8'))
                print("Sent: 'Hello from server!'")
            except Exception as e:
                print(f"Error sending message: {e}")
            finally:
                # Close client connection
                client_conn.close()
                print("Client connection closed.")

    except socket.error as e:
        print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if server_socket:
            server_socket.close()
            print("Server socket closed.")


if __name__ == "__main__":
    start_server()