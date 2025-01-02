import socket
# configuración del cliente
HOST = '10.0.0.4'  # localhost
PORT = 5000        # puerto del servidor

# creación del socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola, servidor!')
    data = s.recv(1024)

print('Recibido:', repr(data))