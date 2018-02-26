# -*- coding: utf-8 -*-
import socket
from os import listdir #for list of files



def get_response(request):
    top = request.split('\n')                                               #spliting by \n
    avm = top[0].split()[1]                                                 #getting address
    if avm=='/':
        for i in range(len(top)):
            if ''.join(top[i][:11])=='User-Agent:':                         #check for eq
                k=i
        agent = ' '.join(top[k].split()[1:])                                #client name
        return 'HTTP/1.1 200 OK\n\n Hello mister! \n You are: ' + agent     #response 
    elif avm=='/test/' or avm=='/test':                                     #check for eq
        return 'HTTP/1.1 200 OK \n\n' + request                             #returning request
    elif avm=='/media/' or avm=='/media/':                                  #check for eq
        fls=['<a href="'+i+'">'+i+'</a><br/>' for i in listdir('../files/')]#list of files in /files/ with links
        return 'HTTP/1.1 200 OK\n\n'+'\n'.join(fls)                         #returning response and list of files
    elif avm[:7]=='/media/' and avm!='/media/':                             #check if it's smth in media
        file_path=avm[7:]                                                   #file name
        try: 
            with open('../files/'+file_path) as f:                          #if it is file and it exists
                return 'HTTP/1.1 200 OK\n\n'+f.read()                       #returning response & file 
        except Exception as e:                                              #if it is not file or file not exists
            return 'HTTP/1.1 404 Not found\n\nFile not found' 
        
    else:
        return 'HTTP/1.1 404 Not found\n\nPage not found'




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))                                     #set ro server local port 8000
server_socket.listen(0)                                                     #listening ports 

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()                 #if new client
        request_string = client_socket.recv(2048)                           #getting reqest from client
        client_socket.send(get_response(request_string))                    #sending answer
        client_socket.close()
    except KeyboardInterrupt:                                               #if ctrl + C
        print 'Stopped'
        server_socket.close()                                               #stop listening
        server_socket.close()                                               #stop listening
        exit()
