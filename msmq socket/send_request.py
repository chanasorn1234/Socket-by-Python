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

HOST = '10.50.41.99'
PORT = 20020

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.sendall(os.getenv('COMPUTERNAME')+'\n\0')
print('con1')
sleep(1)
# s.sendall("SetupTester\n{7C14C04C-6765-4693-8E04-B34FCA8CC544}\\1234501\n<Vdt:dt=""string""key=\"TestProgFileName\""">"
# 			"/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>\n<V dt:dt=""string""key=\"ProductID\""">DECU1TV2XC10HD</V>\n<Vdt:dt=""string"" key=\"LotID\""">MTAI152402570.000</V>\n<V dt:dt=""string"" key=\"HandlerID\""">Manual</V>\n<V dt:dt=""string"" key=\"TempSetpoint\""">25</V>\n<V dt:dt=""string"" key=\"OperatorID\""">finalop</V>\n<V dt:dt=""string"" key=\"PartNum\""">18F67K</V>\n<V dt:dt=""string""key=\"DeviceType\""">QTP</V>\n<V dt:dt=""string"" key=\"CPOnChecksum\""">FFFF</V>\n<Vdt:dt=""string"" key=\"CPOffChecksum\""">EEEE</V>\n<V dt:dt=""string"" key=\"QCode\"""></V>\n<V dt:dt=""string""key=\"TestProgFileName\""">"
# 				"/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>\n<V dt:dt=""string"" Key=\"TestProgChecksum\""">195478132</V>\n<V dt:dt=""string"" key=\"HardwareMap\""">x28mct64tqfp</V>\n<V dt:dt=""string""key=\"TestFlow\""">f1-prd-std-ato-iqc</V>\n<V dt:dt=""string"" key=\"Environment\""">25C</V>\n<V dt:dt=""string"" key=\"HandlerType\""">Tapestry PH-1</V>\n<V dt:dt=""string"" key=\"SenderID\""">TapestryTAPCC071</V>\n<V dt:dt=""string"" key=\"TestMode\""">QC</V></Root>\n\0"
# )

# s.sendall('SetupTester\n{9A30C945-0EBC-410D-B9E5-504FAD490FE9}\\235607\n'+\
#             '<Root xmlns:dt="urn:schemas-microsoft-com:datatypes">'+\
#             '<Dictionary key="Top">'+\
#             '<V dt:dt="string" key="ProductID">LEAK1TN2XAXF</V>'+\
#             '<V dt:dt="string" key="LotID">MMT-230401629.000</V>'+\
#             '<V dt:dt="string" key="HandlerID">TapestryZ</V>'+\
#             '<V dt:dt="string" key="TempSetpoint">25</V>'+\
#             '<V dt:dt="string" key="OperatorID">finalop</V>'+\
#             '<V dt:dt="string" key="PartNum">24F16KA102</V>'+\
#             '<V dt:dt="string" key="DeviceType">OTP</V>'+\
#             '<V dt:dt="string" key="CPOnChecksum">0</V>'+\
#             '<V dt:dt="string" key="CPOffChecksum">0</V>'+\
#             '<V dt:dt="string" key="QCode">0</V>'+\
#             '<V dt:dt="string" key="TestProgFileName">/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>'+\
#             '<V dt:dt="string" Key="TestProgChecksum">29187440</V>'+\
#             '<V dt:dt="string" key="HardwareMap">x24mct28ssop</V>'+\
#             '<V dt:dt="string" key="TestFlow">f1-prd-std-28L</V>'+\
#             '<V dt:dt="string" key="Environment">FS1@25C</V>'+\
#             '<V dt:dt="string" key="HandlerType">Tapestry PH-1</V>'+\
#             '<V dt:dt="string" key="SenderID">TapestryZ</V>'+\
#             '<V dt:dt="string" key="TestMode">FT</V>'+\
#             '</Dictionary>'+\
#             '</Root>\n\0'
# )
s.sendall('SetupTester\n{9A30C945-0EBC-410D-B9E5-504FAD490FE9}\\236128\n'+\
            '<Root xmlns:dt="urn:schemas-microsoft-com:datatypes">'+\
            '<Dictionary key="Top">'+\
            '<V dt:dt="string" key="ProductID">MFAF1TN2XLX5</V>'+\
            '<V dt:dt="string" key="LotID">MMT-231400168.000</V>'+\
            '<V dt:dt="string" key="HandlerID">TapestryZ</V>'+\
            '<V dt:dt="i2" key="TempSetpoint">25</V>'+\
            '<V dt:dt="string" key="OperatorID">finalop</V>'+\
            '<V dt:dt="string" key="PartNum">16LF18855</V>'+\
            '<V dt:dt="string" key="DeviceType">OTP</V>'+\
            '<V dt:dt="string" key="CPOnChecksum">0</V>'+\
            '<V dt:dt="string" key="CPOffChecksum">0</V>'+\
            '<V dt:dt="string" key="QCode">0</V>'+\
            '<V dt:dt="string" key="TestProgFileName">/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>'+\
            '<V dt:dt="string" Key="TestProgChecksum">220704906</V>'+\
            '<V dt:dt="string" key="HardwareMap">x48mct28ssop</V>'+\
            '<V dt:dt="string" key="TestFlow">f1-prd-ato-cpr-iqc-lf</V>'+\
            '<V dt:dt="string" key="Environment">FS1@25C</V>'+\
            '<V dt:dt="string" key="HandlerType">Tapestry PH-1</V>'+\
            '<V dt:dt="string" key="SenderID">TapestryZ</V>'+\
            '<V dt:dt="string" key="TestMode">FT</V>'+\
            '</Dictionary>'+\
            '</Root>\n\0')



print("send done")
data = None
while(1):
    print('wait receive')
    data = s.recv(1024)
    print('Data =',data)
    print(data[0:11])
    if(data[0:10] == "SetupEnded"):
        print('555')
        sleep(10)
        s.close()
        break
    
