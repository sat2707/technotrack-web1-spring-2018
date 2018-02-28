# -*- coding: utf-8 -*-
import socket
import pip.download
import re


def get_response(http_request):
    k = 2
    request = ""
    for i in http_request: # при желании можно узнать и метод, и версию, но достаточно и этого)
        if i == ' ':
            k -= 1
            continue
        if k <= 0:
            break
        if k == 1:
            request += i
    if request == '/':
        client_socket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + '<!DOCTYPE html><html><head><title>Hello mister!</title><meta charset="Windows-1251"></head><body><div>Hello mister!</div><div>You are:' + pip.download.user_agent() +
                           '</div><div><a href="http://localhost:8000/media/">media</a></div></body></html>')
        return
    if request == '/media/':
        client_socket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' +
                           '<a href="http://localhost:8000/media/test1.txt">test1.txt</a>' + ' '
                            '<a href="http://localhost:8000/media/test2.txt">test2.txt</a>')
        return
    if request == '/media/test1.txt':
        file = open(r'C:\Users\zahar\git\web\technotrack-web1-spring-2018\lesson1\files\test1.txt')
        client_socket.send('HTTP/1.1 200 OK\r\n\r\n' + file.read())
        return
    if request == '/media/test2.txt':
        file = open(r'C:\Users\zahar\git\web\technotrack-web1-spring-2018\lesson1\files\test2.txt')
        client_socket.send('HTTP/1.1 200 OK\r\n\r\n' + file.read())
        return
    if re.match('/media/', request):
        client_socket.send('HTTP/1.1 404 Not found\r\n\r\nFile not found')
        return
    if request == '/test/':
        client_socket.send('HTTP/1.1 200 OK\r\n\r\n' + http_request)
        return
    client_socket.send('HTTP/1.1 404 Not found\r\n\r\nPage not found')
    return


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #
server_socket.listen(1)  # запускаем режим прослушавания для очереди из 1 клиента

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  # выводим в консоль сообщение о новом подключении
        request_string = client_socket.recv(2048)  # получаем запрос
        print request_string
        get_response(request_string)  # обработка запроса
        client_socket.close()
    except KeyboardInterrupt:  # обработка искльчения
        print 'Stopped'
        server_socket.close()  # разрыв соединения
        exit()
