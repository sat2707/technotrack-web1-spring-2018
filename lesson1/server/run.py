import socket


def send_answer(mySocket, status="200 OK", typ="text/plain; charset=utf-8", data=""):
    data = data.encode("utf-8")
    mySocket.send(b"HTTP/1.1 " + status.encode("utf-8") + b"\r\n")
    mySocket.send(b"Server: simplehttp\r\n")
    mySocket.send(b"Connection: close\r\n")
    mySocket.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
    mySocket.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    mySocket.send(b'\r\n')
    mySocket.send(data)


def get_response(mySocket, request):
    if not request:
        return

    information = request.split(" ", 2)
    if information[0] == 'GET' and information[1] == '/':
        udata = request.split('User-Agent: ', 1)[1]
        finalUdata = udata.split('Accept')[0]
        answer = """<!DOCTYPE html>"""
        answer += """<html><head><title>localhost</title></head><body><h1>"""
        answer += """<p>Hello, mister!"""
        answer += """<br>You are: """ + finalUdata + """</br></h1></body></html>"""
        send_answer(mySocket, typ="text/html; charset=utf-8", data=answer)
    elif information[0] == 'GET' and (information[1] == '/media/' or information[1] == '/media'):
        answer = """<!DOCTYPE html>"""
        answer += """<html><head><title>localhost</title></head><body><h1>"""
        answer += """<a href="http://localhost:8000/media/test1.txt">test1.txt</a><br>"""
        answer += """<a href="http://localhost:8000/media/test2.txt">test2.txt</a>"""
        answer += """</h1></body></html>"""
        send_answer(mySocket, typ="text/html; charset=utf-8", data=answer)
    elif information[0] == 'GET' and (information[1] == '/media/test1.txt' or information[1] == '/media/test1.txt/'):
        f = open('/Users/Peter/Desktop/test1.txt')
        line = f.read()
        answer = """<!DOCTYPE html>"""
        answer += """<html><head><title>localhost</title></head><body><h1>"""
        answer += """<br>""" + line + """</br></h1></body></html>"""
        send_answer(mySocket, typ="text/html; charset=utf-8", data=answer)
        f.close()
    elif information[0] == 'GET' and (information[1] == '/media/test2.txt' or information[1] == '/media/test2.txt/'):
        f = open('/Users/Peter/Desktop/test2.txt')
        line = f.read()
        answer = """<!DOCTYPE html>"""
        answer += """<html><head><title>localhost</title></head><body><h1>"""
        answer += """<br>""" + line + """</br></h1></body></html>"""
        send_answer(mySocket, typ="text/html; charset=utf-8", data=answer)
        f.close()
    elif information[0] == 'GET' and (information[1] == '/test' or information[1] == '/test/'):
        answer = """<!DOCTYPE html>"""
        answer += """<html><head><title>localhost</title></head><body><h1>"""
        firstLine = request.split('Host', 1)
        secondLine = firstLine[1].split('Connection', 1)
        thirdLine = secondLine[1].split('Upgrade-Insecure-Requests', 1)
        fourthLine = thirdLine[1].split('User-Agent', 1)
        fifthLine = fourthLine[1].split('Accept', 1)
        sixthLine = fifthLine[1].split('Accept-Encoding', 1)
        seventhLine = sixthLine[1].split('Accept-Language', 1)
        answer += """<br>""" + firstLine[0]
        answer += """<br>""" + 'Host' + secondLine[0]
        answer += """<br>""" + 'Connection' + thirdLine[0]
        answer += """<br>""" + 'Upgrade-Insecure-Requests' + fourthLine[0]
        answer += """<br>""" + 'User-Agent' + fifthLine[0]
        answer += """<br>""" + 'Accept' + sixthLine[0]
        answer += """<br>""" + 'Accept-Encoding' + seventhLine[0]
        answer += """<br>""" + 'Accept-Language' + seventhLine[1]
        answer += """</h1></body></html>"""
        send_answer(mySocket, typ="text/html; charset=utf-8", data=answer)
    else:
        answer = """<!DOCTYPE html>"""
        answer += """<html><head><title>localhost</title></head><body><h1>"""
        answer += """<p>Page not found"""
        answer += """</h1></body></html>"""
        send_answer(mySocket, status="404 Not found", typ="text/html; charset=utf-8", data=answer)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))
server_socket.listen(1)

print('Started')

while True:
    try:
        (client_socket, address) = server_socket.accept()
        print('Got new client', client_socket.getsockname())
        request_string = client_socket.recv(2048).decode('utf-8')
        get_response(client_socket, request_string)
        client_socket.close()
    except KeyboardInterrupt:
        print('Stopped')
        server_socket.close()
        exit()