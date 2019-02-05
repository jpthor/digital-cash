import socketserver, socket, sys

host = "0.0.0.0"
port = 10000
address = (host, port)

class myTCPServer(socketserver.TCPServer):
    allow_address_reuse = True

class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        message = self.request.recv(10).strip()
        print(f"Got a message: {message}")

        if message == b"ping":
            self.request.sendall(b"pong\n")

def serve():
    server = myTCPServer(address, TCPHandler)
    server.serve_forever()

def ping():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.sendall(b"ping")
    data = sock.recv(10)
    print(f"data: {data.decode()}")


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "serve":
        serve()
    elif command == "ping":
        ping()
    else: print("invalid")
