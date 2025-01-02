import socket
# configuración del servidor
HOST = '10.0.0.4'  # localhost
PORT = 5000        # puerto de escucha

# creación del socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()  # poner el socket en modo escucha
    print('Servidor escuchando en', (HOST, PORT))
    conn, addr = s.accept()  # esperar una conexión
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)  # recibir datos del cliente
            if not data:
                break
            conn.sendall(data)  # enviar los mismos datos de vuelta al cliente