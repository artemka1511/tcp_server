import socket
import datetime


def edit_data(data):
    dt_now = datetime.datetime.now()

    if data[21:23] == '00':
        message = f'{dt_now}| Спортсмен, нагрудный номер "{data[0:4]}" прошёл отсечку "{data[5:7]}" в "{data[8:18]}"'
        print(message)
    else:
        message = f'{dt_now}| ' + data

    file = open('logs.txt', 'a')
    file.write(message + "\n")
    file.close()


def run_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 2001))
        server.listen(12)
        print('Working...')
        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(4096).decode('utf-8')
            edit_data(data)

    except KeyboardInterrupt:
        server.close()


if __name__ == '__main__':
    run_server()


