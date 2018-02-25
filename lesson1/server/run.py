# -*- coding: utf-8 -*-
import socket
import os

def get_response(request_str):
	request=request_str.decode("utf-8").split("\r\n")
	method, address, protocol=request[0].split(" ")
	if address=="/":
		for elem in request:
			if elem.count("User-Agent:"):
				user_agent=elem[12:]
				break;
		buf=b"HTTP/1.1 200OK\r\nContent-Type: text/plain\r\n\r\nHello, mister!\nYou are: " + user_agent.encode("utf8") + b"\r\n" 
	elif address=="/media/":
		buf=b"HTTP/1.1 200OK\r\nContent-Type: text/html\r\n\r\n"
		paths=os.listdir(path=".")
		paths.sort()
		for elem in paths:
			buf+=b"<a href=/media/"+elem.encode("utf8")+b">"+elem.encode("utf-8")+ b"</a><br>"
	elif address.count("/media/"):
		fname=address[7:]
		f=open(fname, 'r');
		buf=b"HTTP/1.1 200OK\r\nContent-Type: text/plain\r\n\r\n"+f.read().encode("utf-8")
	elif address=="/test/":
		buf=b"HTTP/1.1 200OK\r\nContent-Type: text/plain\r\n\r\n" + request_str + b"\r\n" 
	else:
		buf=b"HTTP/1.1 404 Not found\r\nContent-Type: text/plain\r\n\r\n Page not found. \r\n"
	return buf


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # связь сокета с хостом и портом (начало работы)
server_socket.listen(10)  # максимальное количество запросов

print('Started')
os.chdir("files")
while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print('Got new client', client_socket.getsockname())  # получение IP и адреса клиента
        request_string = client_socket.recv(2048)  # максимальное количество считываемых байт
        client_socket.send(get_response(request_string))  # отправка ответа сервера
        client_socket.close()
    except KeyboardInterrupt:  # обработка исключения (сигналов с клавиатуры, насколько я понимаю)
        print('Stopped')
        server_socket.close()  # остановка сервера
        exit()
