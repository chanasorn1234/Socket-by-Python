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

def sendandreceive_with_socket(msgtosend):
    lit = []
    lit2 = []
    HOST = 'localhost'
    PORT = 5432

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))

    # s.sendall(b'Hello World')
    s.sendall(msgtosend.Label)
    s.sendall(',')
    s.sendall(msgtosend.Body)
    s.sendall(',')
    # s.sendall(msgtosend.Id)
    # s.sendall(',')
    # s.sendall(msgtosend)

    if(msgtosend.Label == 'SetupTester' or msgtosend.Label == 'EndLot'):
        # data = s.recv(1024)
        while(1):
            print('wait msg from oi')
            data = s.recv(1024)
            sleep(5)
            if(data):
                print('received:', repr(data))
                lit = data.split(',')
                if(lit[0] == 'SetupTesterReply'):
                    res_destination = win32com.client.Dispatch("MSMQ.MSMQDestination")
                    resmsg = win32com.client.Dispatch("MSMQ.MSMQMessage")
                    res_destination = msgtosend.ResponseDestination
                    resmsg.Body = lit[1]
                    resmsg.Label = lit[0]
                    resmsg.CorrelationId = msgtosend.Id
                    resmsg.Send(res_destination)
                    res_destination.Close()
                    print('Resp:SetuptesterReply Done')
                    while(1):
                        print('wait msg from SetupEnded oi')
                        data2 = s.recv(1024)
                        if(data2):
                            print('received:', repr(data2))
                            lit2 = data2.split(',')
                            if(lit2[0] == 'SetupEnded'):
                                print('Request:SetupEnded Done')
                            break
                elif(lit[0] == 'EndLotReply'):
                    pass
                break
            sleep(5)

while(1):
    print("wait msg")
    pre_qinfo_id = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    pre_keepid = win32com.client.Dispatch("MSMQ.MSMQMessage")
    pre_pre_id = win32com.client.Dispatch("MSMQ.MSMQQueue")

    precheck_computer_name = os.getenv('COMPUTERNAME')
    pre_pathname = precheck_computer_name+"\\PRIVATE$\\testeroi"
    pre_qinfo_id.FormatName = "DIRECT=OS:"+pre_pathname
    pre_pre_id = pre_qinfo_id.Open(1,0)

    timeout_sec = 1.0
    checkmsg = pre_pre_id.peek(pythoncom.Empty,pythoncom.Empty,timeout_sec * 1000)
    if(checkmsg != None):
        print("msg from cell controller")
        if(checkmsg.Label == 'SetupTester' or checkmsg.Label == 'SetupEndedReply' or checkmsg.Label == 'Endlot'):
            pre_keepid = pre_pre_id.Receive()
            pre_pre_id.Close()
            sendandreceive_with_socket(pre_keepid)
        else:
            sleep(5)
            pre_pre_id.Receive()
    sleep(5)




    