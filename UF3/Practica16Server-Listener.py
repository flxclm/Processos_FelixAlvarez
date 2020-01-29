# Echo server program
import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50006              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()

def rebre(conn):
    while True:
        m = conn.recv(1024)
        print m

        if m == "Bye":
            conn.sendall(m)
            break

def enviar(conn):
    while True:
        n = raw_input("Digues alguna cosa: ")
        conn.sendall(n)

        if n == "Bye":

            break

t1 = threading.Thread(target=enviar, args=(conn,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=rebre, args=(conn,))
t2.start()

t2.join()

s.close()
