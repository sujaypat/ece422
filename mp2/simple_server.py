import socket

# modified by Brian Winkelmann
# code modified from sample code at
# https://docs.python.org/2/library/socket.html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("localhost", 31337))
s.listen(1)

print("Simple server running on http://127.0.0.1:31337/")
print("Use (ctrl + c) to end server")
i = 0
while True:
    try:
        conn, addr = s.accept()
        data = conn.recv(1024)
        conn.close()
        print "\n {0}".format(i)
        print(data.splitlines()[0])
        i += 1
    except KeyboardInterrupt:
        s.close()
        print("\nGoodbye")
        break
