# -*- coding: utf-8 -*-
# ВАЖНО: на моем компьютере почему - то требуется обновлять постоянно страницу, чтобы она показывала содержимое, иначе пустая страница
import socket
import os

m = 0
filenames = ''
directory = '/home/styopa/technotrack-web1-spring-2018/lesson1/files' 
files = os.listdir(directory) 
while m < len(files):
	filenames = filenames + '\n'+ '<a href="/media/' + files[m] + '">' + files[m] + '</a>'
	m = m + 1
f1 = open("/home/styopa/technotrack-web1-spring-2018/lesson1/files/test1.txt").read()
f2 = open("/home/styopa/technotrack-web1-spring-2018/lesson1/files/test2.txt").read()

def get_response(request):
	i = 0
	j = 0
	req = ''
	User = ''
	while i <> 2:
		if request[j] == ' ':
			i = i + 1
		req = req + request[j]
		j = j + 1
	while i <> 20:
		if request[j] == ' ':
			i = i + 1
		j = j + 1
		if request[j:j+12] == 'User-Agent: ':
			k = 0
			while request[j+12+k] <> ' ':
				User = User + request[j+12+k]
				k = k + 1 
	if req[4:-1] == '/':
		return 'HTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\nContent-Length: 100\n\n' + ' ' + 'Hello mister!\nYou are: ' + User
	elif req[4:-1] == '/test/':
		return 'HTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\nContent-Length: 1000\n\n' + ' ' + request
	elif req[4:-1] == '/media/':
		return 'HTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\nContent-Length: 1000\n\n' + ' ' + filenames
	elif req[-10:-1] == 'test1.txt':
		return 'HTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\nContent-Length: 1000\n\n' + ' ' + f1
	elif req[-10:-1] == 'test2.txt':
		return 'HTTP/1.1 200 OK\nContent-Type: text/html;charset=UTF-8\nContent-Length: 1000\n\n' + ' ' + f2
	else:
		return 'HTTP/1.1 404 Not found\nContent-Type: text/html;charset=UTF-8\nContent-Length: 100\n\n' + ' ' + req

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #связывает сокет с конкретным адресом
server_socket.listen(0)  #переключает сокет в состояние прослушивания, то есть подготовливает к принятию входящих соединений

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #возвращает текущий адрес, к которому привязан сокет
        request_string = client_socket.recv(2048)  #запрос к серверу
  	client_socket.send(get_response(request_string))  #обработка запроса и его отправка
        client_socket.close()
    except KeyboardInterrupt:  #прерывание, то есть остановка работы сервера
        print 'Stopped'
        server_socket.close()  #закрывает подключение к удаленному узлу
        exit()
