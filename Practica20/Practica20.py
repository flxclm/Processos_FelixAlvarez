
# -*- coding: utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import smtplib, ssl
password = "23anecs"

class http_server:
    def __init__(self):
        server = HTTPServer(('', 8080), myHandler)
        server.serve_forever()

class myHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            if "practica.html" in self.path:
                file = open("practica.html", 'rb')
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(file.read())
            elif "burns.png" in self.path:
                file = open("burns.png", 'rb')
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.end_headers()
                self.wfile.write(file.read())

            #La part del codi que envia un missatge al correu és aquesta

                mail = smtplib.SMTP_SSL("smtp.gmail.com", 465) #connexió ssl
                mail.hello() #missatge de salutació amb el servei/servidor
                mail.login("felix8ao@gmail.com", password)
                message = "Subject: Salutacions!" + "\nHa intentat entrar: %s" % str(self.client_address) #Cos del missatge
                mail.sendmail("felix8ao@gmail.com", "felix8ao@gmail.com", message) #envia el missatge
                mail.quit()
            else:
                self.send_error(404, "Not Found")

class main:
    def __init__(self):

        self.server = http_server()

if __name__ == '__main__':
    m = main()
