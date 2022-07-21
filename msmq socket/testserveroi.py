import socket
from tabnanny import check
from time import sleep
import win32com.client
import os
import struct
import pythoncom
import platform
import ConfigParser
import sys
import urllib2
HOST = 'localhost'
PORT = 5432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(PORT)
lit = None
while True:

    print("waiting for connection")

    connection, client_address = s.accept()
    try:
        print("connection from", client_address)
        while True:
            data = connection.recv(1024)
            print("received:", data)

            if data:
                lit = data.split(',')
                if(lit[0] == 'SetupTester'):
                    print('receive SetupTester')
                    q_send_oi_1 = win32com.client.Dispatch("MSMQ.MSMQDestination")
                    q_resp_oi_1 = win32com.client.Dispatch("MSMQ.MSMQDestination")
                    msgto_oi = win32com.client.Dispatch("MSMQ.MSMQMessage")
                    computer_name = os.getenv('COMPUTERNAME')

                    q_send_oi_1.Formatname = "DIRECT=OS:"+computer_name+"\\PRIVATE$\\testeroi"
                    q_resp_oi_1.Formatname = "DIRECT=OS:"+computer_name+"\\PRIVATE$\\replyoi"

                    msgto_oi.ResponseDestination = q_resp_oi_1
                    msgto_oi.Body = lit[1]
                    msgto_oi.Label = lit[0]
                    msgto_oi.Send(q_send_oi_1)
                    print('send:SetupTester to oi Done')
                    while(1):
                        print('wait SetuptesterReply from oi')
                        q_reciv_oi_1 = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
                        q_reciv_q = win32com.client.Dispatch("MSMQ.MSMQQueue")
                        q_reciv_m = win32com.client.Dispatch("MSMQ.MSMQMessage")
                        q_reciv_oi_1.Formatname = "DIRECT=OS:"+computer_name+"\\PRIVATE$\\replyoi"
                        q_reciv_q = q_reciv_oi_1.Open(1,0)
                        q_reciv_m = q_reciv_q.Peek(pythoncom.Empty,pythoncom.Empty,1.0*1000)
                        if(q_reciv_m != None and q_reciv_m.Label == "SetupTesterReply"):
                            q_reciv_m = q_reciv_q.Receive()
                            print("Receive SetupTesterReply from oi")
                            connection.sendall(q_reciv_m.Label+","+q_reciv_m.Body)
                            # connection.sendall(",")
                            # connection.sendall(q_reciv_m.Body)
                            # connection.sendall(",")
                            # connection.sendall(q_reciv_m.Id)
                            # connection.sendall(",")
                            # connection.sendall(q_reciv_m)
                            q_reciv_q.Close()
                            print("Send SetupTesterReply Done")
                            while(1):
                                print("wait SetupEnded")
                                q_reciv_oi_2 = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
                                q_reciv_q2 = win32com.client.Dispatch("MSMQ.MSMQQueue")
                                q_reciv_m2 = win32com.client.Dispatch("MSMQ.MSMQMessage")
                                q_reciv_oi_2.Formatname = "DIRECT=OS:"+computer_name+"\\PRIVATE$\\replyoi"
                                q_reciv_q2 = q_reciv_oi_2.Open(1,0)
                                q_reciv_m2 = q_reciv_q2.Peek(pythoncom.Empty,pythoncom.Empty,1.0*1000)
                                if(q_reciv_m2 != None):
                                    q_reciv_m2 = q_reciv_q2.Receive()
                                    print("Receive SetupEnded from oi")
                                    connection.sendall(q_reciv_m2.Label+","+q_reciv_m2.Body)
                                    # connection.sendall(",")
                                    # connection.sendall(q_reciv_m2.Body)
                                    # connection.sendall(",")
                                    # connection.sendall(q_reciv_m2.Id)
                                    # connection.sendall(",")
                                    # connection.sendall(q_reciv_m2)
                                    print("Send SetupEnded Done")
                                    q_reciv_q2.Close() 
                                    break
                                q_reciv_q2.Close() 
                                sleep(5)   
                            break
                        q_reciv_q.Close()
                        sleep(5)

                elif(lit[0] == 'SetupEndedReply'):
                    print('receive SetupEndedReply')

                elif(lit[0] == 'EndLot'):
                    print('receive EndLot')
                # print("sending data back to the client")
                # connection.sendall(data)
            
            else:
                print("no more data from", client_address)
                break
    finally:
        connection.close()
        print("closed connection")
    
    lit = None