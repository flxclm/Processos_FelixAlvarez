# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Conectant...")

while True:
   print("Introdueix el teu missatge: ")
   msg = raw_input()
   s.sendto(msg,((HOST, PORT)))
   if msg == "Bye":
       break



s.close()
