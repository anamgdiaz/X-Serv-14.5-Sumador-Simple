#!/usr/bin/python3

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
	while True:
		print("Waiting for connections")
		(recvSocket,address) = mySocket.accept()
#PROCESO DE PETICIÓN
		print("Request received:")
		bytes_received = recvSocket.recv(2048)
		peticion = str(bytes_received,'utf-8')
		print(peticion)
		resource = peticion.split()[1]
		print(resource)
		_,op1,operacion, op2 = resource.split('/')
		print("Quiero hacer")
		print(op1,operacion,op2)
		resultado = calculadora.calcular(op1,op2,operacion)
		respuesta = str(resultado)
		recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><p>El resultado es: "+respuesta+"</html></body></p>","utf-8"))
		recvSocket.close()
except KeyboardInterrupt:
	print("Closing bind socket")
mySocket.close()