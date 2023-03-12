import socket
import select

port = 5566
con = {}
req = {}
resp = {}

def Server(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setblocking(False)
        s.bind((host, port))
        s.listen(10)
        yield s
    except socket.error:
        print("Get socket error")
        raise
    finally:
        if s:
            s.close()

def Poll():
    try:
        e = select.poll()
        yield e
    finally:
        for fd, c in con.items():
            e.unregister(fd)
            c.close()

def accept(server, poll):
    conn, addr = server.accept()
    conn.setblocking(False)
    fd = conn.fileno()
    poll.register(fd, select.POLLIN)
    req[fd] = conn
    con[fd] = conn
    return conn, addr

def recv(fd, poll):
    if fd not in req:
        return
    conn = req[fd]
    msg = conn.recv(1024)
    if msg:
        resp[fd] = msg
        poll.modify(fd, select.POLLOUT)
    else:
        conn.close()
        del con[fd]
        del req[fd]



# To use the above code, you need to call the Server() and Poll() functions in a loop to continuously listen for incoming connections and data
# here's an example below

server = None
poll = None

try:
    server = Server('', port)
    poll = Poll()

    for s in server:
        poll[0].register(s.fileno(), select.POLLIN)

    while True:
        for fd, event in poll[0].poll():
            if event & select.POLLIN:
                if fd == server[0].fileno():
                    conn, addr = accept(server[0], poll[0])
                    print(f'New connection from {addr[0]}:{addr[1]}')
                else:
                    recv(fd, poll[0])
            elif event & select.POLLOUT:
                conn = con[fd]
                msg = resp[fd]
               
