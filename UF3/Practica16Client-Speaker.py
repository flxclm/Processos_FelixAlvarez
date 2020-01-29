# Echo client program
import socket
import threading

HOST = 'localhost'   # The remote host
PORT = 50006             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

def enviar(s):
    while True:
        n = raw_input("Digues alguna cosa: ")
        s.sendall(n)

        if n == "Bye":
            break


def rebre(s):
    while True:
        m = s.recv(1024)
        print m

        if m == "Bye":
            s.sendall(m)
            break

t1 = threading.Thread(target=enviar, args=(s,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=rebre, args=(s,))
t2.start()


t2.join()

s.close()
