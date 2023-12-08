import socket
ip=input("ip giriniz: ")
aciks=""
for port in range (65536):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if sock.connect_ex((ip,port))==0:
        print(port,"acik port")
        aciks+=(str(port)+" ")
    else:
        print(port,"kapali port")
print("acik portlar: ",aciks)