import socket
import threading

from LogPasser import *
from BroadcastServer import*

def VerificationServer(Server_Name, Server_Password, MySql_Details):
    from ServerFunctions import CheckUser, CheckUserPresence, CreateNewUser, SendSecurityQuestion, CheckSecurityAnswer, ChangeUserPassword, SendNumberIfEmail, SendNameFromEmail
    HEADER = 64
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    ADDR = (SERVER_IP, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!*Disconnect"

    Verification_Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Verification_Server.bind(ADDR)
    

    def handle_client(conn, addr):
        WriteLog(f'[NEW CONNECTION] {addr} is trying to connect.')
        
        Active_Count = 0
        Connected = True
        while Connected:
            Input_Length = conn.recv(HEADER).decode(FORMAT)
            if Input_Length:
                Input_Length = int(Input_Length)
                Input = conn.recv(Input_Length).decode(FORMAT)
                if Input == Server_Password:
                    conn.send("!*Correct".encode(FORMAT))
                    Active_Count += 1
                    WriteLog(f'[ACTIVE CONNECTIONS] {Active_Count}')
                elif Input[:10] == "CheckUser~":
                    if CheckUser(MySql_Details, Input[10:]) == "Matched":
                        conn.send(f"ServerDetails~{SERVER_IP}~{MySql_Details[0]}~{MySql_Details[1]}~{MySql_Details[2]}".encode(FORMAT))
                        WriteLog(f'[NEW CONNECTION] {addr} connected.')
                    else:
                        conn.send(CheckUser(MySql_Details, Input[10:]).encode(FORMAT))
                elif Input[:18] == "CheckUserPresence~":
                    conn.send(str(CheckUserPresence(MySql_Details, Input[18:])).encode(FORMAT))
                elif Input[:14] == "CreateNewUser~":
                    conn.send(str(CreateNewUser(MySql_Details, Input[14:])).encode(FORMAT))
                elif Input[:20] == "GetSecurityQuestion~":
                    conn.send(str(SendSecurityQuestion(MySql_Details, Input[20:])).encode(FORMAT))
                elif Input[:20] == "CheckSecurityAnswer~":
                    conn.send(str(CheckSecurityAnswer(MySql_Details, Input[20:])).encode(FORMAT))
                elif Input[:15] == "ChangePassword~":
                    conn.send(str(ChangeUserPassword(MySql_Details, Input[15:])).encode(FORMAT))
                elif Input[:17] == "GetNumberIfEmail~":
                    conn.send(str(SendNumberIfEmail(MySql_Details, Input[17:])).encode(FORMAT))
                elif Input[:17] == "GetNameFromEmail~":
                    conn.send(str(SendNameFromEmail(MySql_Details, Input[17:])).encode(FORMAT))
                elif Input == DISCONNECT_MESSAGE:
                    Active_Count -= 1
                    WriteLog(f'[DISCONNECTED] {addr} disconnected.')
                    WriteLog(f'[ACTIVE CONNECTIONS] {Active_Count}')
                    Connected = False
                else:
                    conn.send("Incorrect Password!".encode(FORMAT))

        conn.close()

    def Start():
        Verification_Server.listen()
        WriteLog(f'[LISTENING] Server({Server_Name}) is listening on {SERVER_IP}')
        while True:
            conn, addr = Verification_Server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            
    WriteLog("[STARTING] Server Started.")
    
    VerificationServer_ = threading.Thread(target=Start)
    VerificationServer_.daemon = True
    VerificationServer_.start()
    
    BroadcastServer_ = threading.Thread(target=StartBroadcastServer, args=(Server_Name, SERVER_IP, PORT))
    BroadcastServer_.daemon = True
    BroadcastServer_.start()
