import socket
import threading
import time

def SearchHosts():
    PORT = 5050

    Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    Client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    Client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    Client.bind(("", PORT))
    
    Completed = ""
    HostDetails = []
    HostDetailsList = []

    def SearchHostNames():
        while True:
            Data, addr = Client.recvfrom(1024)
            Data = Data.decode('utf-8')
            if Data not in HostDetails:
                HostDetails.append(Data)
            if Completed == "!SearchComplete":
                break

    SearchThread = threading.Thread(target=SearchHostNames)
    SearchThread.daemon = True
    SearchThread.start()

    time.sleep(1)
    Completed = "!SearchComplete"
    
    for _ in HostDetails:
        HostDetailsList.append(_.split("~"))
        
    for _ in HostDetailsList:
        _[2] = int(_[2])
        
    return HostDetailsList

class HostConnection:
    def ConnectHost(self, HostIP, HostPort):
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.DISCONNECT = "!*Disconnect"
        ADDR = (HostIP, HostPort)

        self.Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Client.connect(ADDR)

    def Send(self, Details):
        Detail = Details.encode(self.FORMAT)
        Detail_Length = len(Detail)
        Send_Length = str(Detail_Length).encode(self.FORMAT)
        Send_Length += b' ' * (self.HEADER - len(Send_Length))
        self.Client.send(Send_Length)
        self.Client.send(Detail)
        
        return self.Client.recv(2048).decode(self.FORMAT)
    