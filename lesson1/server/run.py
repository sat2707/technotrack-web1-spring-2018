# -*- coding: utf-8 -*-
import socket
from os import listdir



def get_response(request):
	top = request.split('\n')
	avm = top[0].split()[1]
	if avm == '/':
		for i in range(len(top)):
			if ''.join(top[i][:11]) =='User-Agent:':
				k=i
		agent = ' '.join(top[k].split()[1:])
		return 'HTTP/1.1 200 OK\n\n Hello mister! \n You are: ' + agent
	elif avm == '/test/' or avm == '/test':
		return 'HTTP/1.1 200 OK \n\n' + request
	elif avm == '/media/' or avm == '/media/':
		fls = ['<a href="'+i+'">'+i+'</a><br/>' for i in listdir('../files/')]
		return 'HTTP/1.1 200 OK\n\n'+'\n'.join(fls)
	elif avm[:7] == '/media/' and avm != '/media/':
		file_path = avm[7:]
		try:
			with open('../files/'+file_path) as f:
				return 'HTTP/1.1 200 OK\n\n'+f.read()
		except Exception as e:
			return 'HTTP/1.1 404 Not found\n\nFile not found'
		
	else:
		return 'HTTP/1.1 404 Not found\n\nPage not found'




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # Устанавливаем серверу локальный порт 8000
server_socket.listen(0)  # Слушаем порты 

print 'Started'

while 1:
	try:
		(client_socket, address) = server_socket.accept()
		print 'Got new client', client_socket.getsockname()  # В случае появления нового клиента
		request_string = client_socket.recv(2048)  # Полкчаем запрос от клиента
		client_socket.send(get_response(request_string))  # Отправляем ответ
		client_socket.close()
	except KeyboardInterrupt:  # Обработка прерываний
		print 'Stopped'
		server_socket.close()  # Останавливаем прослушку портов
		exit()
