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

def ConNect():
    HOST = '10.50.41.99'
    PORT = 20020

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.sendall(os.getenv('COMPUTERNAME')+'\n\0')
    print('con1')
    sleep(1)
    # s.sendall(os.getenv('COMPUTERNAME'))
    # print('con2')
    return s

def sendandreceive_with_socket(msgtosend,s):
    lit = []
    lit2 = []
    if(msgtosend.Label == 'SetupTester'):
        ind = msgtosend.Body.find('key="TestProgChecksum')
        new = msgtosend.Body[:ind] + 'K' + msgtosend.Body[ind+1:]

        ind2 = new.find('TestProgFileName') + 18
        for i in range(ind2,len(new)):
            if(new[i] == '<'):
                eind2 = i
                break
        new2 = new[:ind2] + '/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una' + new[eind2:]

        msg = msgtosend.Label+'\n'+"{"+msgtosend.SourceMachineGuid+"}\\"+str(struct.unpack("I",msgtosend.Id[16:20])[0])+'\n'+new2+'\n\0'
        print(msg)
    else:
        msg = msgtosend.Label+'\n'+"{"+msgtosend.SourceMachineGuid+"}\\"+str(struct.unpack("I",msgtosend.Id[16:20])[0])+'\n'+msgtosend.Body+'\n\0'
        print(msg)
    # file = open('test.txt','w')
    # file.write(msg)
    # file.close()
    s.sendall(msg)
    print('send done')
#     s.sendall("SetupTester\n{7C14C04C-6765-4693-8E04-B34FCA8CC544}\\1234501\n<Vdt:dt=""string""key=\"TestProgFileName\""">"
# 			"/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>\n<V dt:dt=""string""key=\"ProductID\""">DECU1TV2XC10HD</V>\n<Vdt:dt=""string"" key=\"LotID\""">MTAI152402570.000</V>\n<V dt:dt=""string"" key=\"HandlerID\""">Manual</V>\n<V dt:dt=""string"" key=\"TempSetpoint\""">25</V>\n<V dt:dt=""string"" key=\"OperatorID\""">finalop</V>\n<V dt:dt=""string"" key=\"PartNum\""">18F67K</V>\n<V dt:dt=""string""key=\"DeviceType\""">QTP</V>\n<V dt:dt=""string"" key=\"CPOnChecksum\""">FFFF</V>\n<Vdt:dt=""string"" key=\"CPOffChecksum\""">EEEE</V>\n<V dt:dt=""string"" key=\"QCode\"""></V>\n<V dt:dt=""string""key=\"TestProgFileName\""">"
# 				"/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>\n<V dt:dt=""string"" Key=\"TestProgChecksum\""">195478132</V>\n<V dt:dt=""string"" key=\"HardwareMap\""">x28mct64tqfp</V>\n<V dt:dt=""string""key=\"TestFlow\""">f1-prd-std-ato-iqc</V>\n<V dt:dt=""string"" key=\"Environment\""">25C</V>\n<V dt:dt=""string"" key=\"HandlerType\""">Tapestry PH-1</V>\n<V dt:dt=""string"" key=\"SenderID\""">TapestryTAPCC071</V>\n<V dt:dt=""string"" key=\"TestMode\""">QC</V></Root>\n\0"
# )
 

    if(msgtosend.Label == 'SetupTester' or msgtosend.Label == 'EndLot'):
        # data = s.recv(1024)
        while(1):
            print('wait msg from oi')
            data = ''
            while(1):#data[0:16] != 'SetupTesterReply' or data[0:11] != 'EndLotReply'
                data = s.recv(1024)
                print(data)
                # print(data[0:16])
                if(data[0:16] == 'SetupTesterReply'):
                    print(data[0:16])
                    break
                if(data[0:11] == 'EndLotReply'):
                    print(data[0:11])
                    break
            if(data):
                # print('received:', data)
                
                if(data[0:16] == 'SetupTesterReply'):
                    
                    res_destination = win32com.client.Dispatch("MSMQ.MSMQDestination")
                    resmsg = win32com.client.Dispatch("MSMQ.MSMQMessage")
                    res_destination = msgtosend.ResponseDestination
                    resmsg.Body = data[16:]
                    resmsg.Label = data[0:16]
                    resmsg.CorrelationId = msgtosend.Id
                    resmsg.Send(res_destination)
                    res_destination.Close()
                    print('Resp:SetuptesterReply Done')
                    print('wait SetupEnded')
                    data2 = s.recv(1024)
                    print(data2)
                    
                    q_send_oi_2 = win32com.client.Dispatch("MSMQ.MSMQDestination")
                    q_resp_oi_2 = win32com.client.Dispatch("MSMQ.MSMQDestination")
                    msgto_oi_2 = win32com.client.Dispatch("MSMQ.MSMQMessage")

                    computer_name_contract_oi = os.getenv('COMPUTERNAME')

                    q_send_oi_2.Formatname = "DIRECT=OS:"+computer_name_contract_oi+"\\PRIVATE$\\tapestrycc"
                    q_resp_oi_2.Formatname = "DIRECT=OS:"+computer_name_contract_oi+"\\PRIVATE$\\testeroi"

                    msgto_oi_2.ResponseDestination = q_resp_oi_2

                    ind = data2.find('SetupTesterMsgID') + 18
                    sindex = None
                    eindex = None
                    stri = None
                    for i in range(ind,len(data2)):
                        if(data2[i] == '\\'):
                            sindex = i+1
                            for j in range(sindex,len(data2)):
                                if(data2[j] == '<'):
                                    eindex = j
                                    break
                            break
                    stri = data2[10:sindex] + str(struct.unpack("I",msgtosend.Id[16:20])[0]) + data2[eindex:]
                    print(stri)
                    msgto_oi_2.Body = stri          
                    msgto_oi_2.Label = data2[0:10]
                    msgto_oi_2.Send(q_send_oi_2)

                    print('Request:SetupEnded Done')
                    # s.close()
                    #         break


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
        if(checkmsg.Label == 'SetupTester'):
            pre_keepid = pre_pre_id.Receive()
            pre_pre_id.Close()
            sock = ConNect()
            sendandreceive_with_socket(pre_keepid,sock)
        elif(checkmsg.Label == 'SetupEndedReply' or checkmsg.Label == 'Endlot'):
            pre_keepid = pre_pre_id.Receive()
            pre_pre_id.Close()
            sendandreceive_with_socket(pre_keepid,sock)
        else:
            sleep(5)
            pre_pre_id.Receive()
    sleep(5)




    
