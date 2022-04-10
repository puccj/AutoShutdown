import urllib.request
import time
import os
import socket
 
def shtdwn():
    print("\a")
    print("Server seems off. Close this window to cancel shutdown.")
    time.sleep(30)
    os.system("shutdown /s")
 
#Get IP
def ip() :
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print("IP : " + external_ip)
    return external_ip
 
#Check if server is on
def vstat(ip, port) :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    sock.close()
    if result == 0:
        return True
    else:
        return False
 
#Set the port of the server ( default : 25565 )
port = 25565
 
#Other stuff
ip = ip()
on = vstat(ip, port)

if not on:
    print("\a")
    print("Server seems already off. You should run this script after starting the server.")
    print("However, you have 5 minutes to open the server and avoid the shutdown.")

on = True

while on:
    print("System up and running")
    #Wait 5 minutes
    time.sleep(300)
 
    #Check again if server is running
    on = vstat(ip, port)
    
shtdwn()
