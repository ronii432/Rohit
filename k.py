import socket

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Bind to an arbitrary free port
        return s.getsockname()[1]

free_port = find_free_port()
print(f"Available free port: {free_port}")
