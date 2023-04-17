from socket import *
import threading
import os
import constant

import builtins
import socket as stdlib_socket

socket = getattr(builtins, 'socket', stdlib_socket)



class MyServer:
   
        
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def start(self):
        print(f"Server started on http://{constant.IP_SERVER}:{constant.PORT}")
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((constant.IP_SERVER, constant.PORT))
        self.server_socket.listen()
        while True:
            client_connection, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client_request, args=(client_connection, client_address))
            client_thread.start()
    
        

    def handle_client_request(self, client_connection,client_socket):
        data = client_connection.recv(1024)
        request = str(data.decode('utf-8'))
        request_method = request.split(' ')[0]
        request_path = request.split(' ')[1]

        if request_method == 'GET':
            if request_path == '/' :
                html_content=self.get_html_content('/')
                response_headers = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + bytes(str(len(html_content)), 'utf-8') + b"\r\n\r\n"
                response_body = html_content
            else:
                html_content=self.get_html_content(request_path)
                if html_content:
                    response_headers = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + bytes(str(len(html_content)), 'utf-8') + b"\r\n\r\n"
                    response_body = html_content
                else:
                    response_headers = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 0\r\n\r\n"
                    response_body = b""
        elif request_method == 'HEAD':
            if request_path == '/' :
                html_content=self.get_html_content('/')
                response_headers = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + bytes(str(len(html_content)), 'utf-8') + b"\r\n\r\n"
                response_body = b""
            else:
                html_content=self.get_html_content(request_path)
                if html_content:
                    response_headers = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + bytes(str(len(html_content)), 'utf-8') + b"\r\n\r\n"
                    response_body = b""
                else:
                    response_headers = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 0\r\n\r\n"
                    response_body = b""
        elif request_method == 'POST':
            # Handle POST request
            content_length = request.split('Content-Length: ')[1].split('\r\n')[0]
            data = client_connection.recv(int(content_length))
            post_data = str(data.decode('utf-8'))
            name = post_data.split('name=')[1].split('&')[0]
            response_body = f"<h1>Hello, {name}!</h1>".encode('utf-8')
            response_headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\nConnection: close\r\n\r\n'.format(len(response_body)).encode('utf-8')
            response = response_headers + response_body

            client_connection.sendall(response)
        
        else:
            response_headers = b"HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/html\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
            response_body = b""

        response = response_headers + response_body
        client_connection.sendall(response)
        client_connection.close()

    def get_html_content(self, request_path):
        # Split the request path by "/"
        path_parts = request_path.split("/")

        # Check if the second element is "caso1"
        if len(path_parts) > 1 and path_parts[1] == "caso1":
            # Join the rest of the elements with "/" to get the file path
            file_name = "/".join(path_parts[2:])
            file_path = os.path.join(os.path.dirname(__file__), "documentRootFolder", "caso1", file_name)
        else:
            # If the second element is not "caso1", get the file path normally
            if request_path == "/":
                file_name = "index.html"
            else:
                file_name = request_path.lstrip("/")
            file_path = os.path.join(os.path.dirname(__file__), "documentRootFolder", file_name)

    # Check if the file exists and can be read
        if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
            # Read the file contents
            with open(file_path, "rb") as f:
                html_content = f.read()
        else:
            # If the file doesn't exist or can't be read, return a "file not found" message
            html_content = b"<h1>File not found</h1>"

        return html_content



server = MyServer()
server.start()
