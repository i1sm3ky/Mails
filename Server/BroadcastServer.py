import socket
import time

def StartBroadcastServer(Server_Name, SERVER_IP, PORT):
    Broadcast_Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    Broadcast_Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    Broadcast_Server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    Broadcast_Server.settimeout(0.2)

    Details = f'{Server_Name + "~" + str(SERVER_IP) + "~" + str(PORT)}'.encode('utf-8')

    while True:
        Broadcast_Server.sendto(Details, ('<broadcast>', 5050))
        time.sleep(1)