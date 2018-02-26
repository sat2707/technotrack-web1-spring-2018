# -*- coding: utf-8 -*-
import socket
import re
import os


def get_response(request):
    request_line = (request.replace('\n', ' ').split(' '))#including request_line (GET...)
    request_method = request_line[0] #(request_line[0] == GET, if everything is alright)
    request_path = request_line[1] #(request_line[1] is our path)

    response = 'HTTP/1.1'
    status = '200'
    content_type = 'text/html'
    page = ''

    if request_method == 'GET':

        if re.match(r'/$', request_path):
            user = request.split('\n')[2].split(' ')[1:]#(3d raw of http request)
            page = 'Hello mister! <br> You are: ' + ' '.join(user)


        elif re.match(r'/media/$', request_path):
            files = os.listdir('../files/')
            page = '<br>'.join(files)

        elif re.match(r'/media/', request_path):
            file_name = request_path[7:]#(length(/media/) == 7)
            try:
                file = open('../files/' + file_name, 'r')
                page = file.read()
            except (OSError, IOError) as e:
                status = '404 Not found'
                page = 'File not found'

        elif re.match(r'/test', request_path):
            return request
    else:
        status = '404 Not found'

    response += ' ' + status + '\n' + 'Content-Type: ' + content_type + '\n\n' + page

    return response.encode()





server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #bind server with localhost/port8000
server_socket.listen(0)  #listen to server

print ('Started')

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print ('Got new client', client_socket.getsockname())  #inform about new client
        request_string = client_socket.recv(2048)  #getting request
        client_socket.send(get_response(request_string))  #sending response, due to our request
        client_socket.close()
    except KeyboardInterrupt:  #key to stop our server
        print ('Stopped')
        server_socket.close()  #closing server/stop listening to server
        exit()
