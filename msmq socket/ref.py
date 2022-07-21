# print("SetupTester\n{7C14C04C-6765-4693-8E04-B34FCA8CC544}\\1234501\n<Vdt:dt=""string""key=\"TestProgFileName\""">"
# 			"/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>\n<V dt:dt=""string""key=\"ProductID\""">DECU1TV2XC10HD</V>\n<Vdt:dt=""string"" key=\"LotID\""">MTAI152402570.000</V>\n<V dt:dt=""string"" key=\"HandlerID\""">Manual</V>\n<V dt:dt=""string"" key=\"TempSetpoint\""">25</V>\n<V dt:dt=""string"" key=\"OperatorID\""">finalop</V>\n<V dt:dt=""string"" key=\"PartNum\""">18F67K</V>\n<V dt:dt=""string""key=\"DeviceType\""">QTP</V>\n<V dt:dt=""string"" key=\"CPOnChecksum\""">FFFF</V>\n<Vdt:dt=""string"" key=\"CPOffChecksum\""">EEEE</V>\n<V dt:dt=""string"" key=\"QCode\"""></V>\n<V dt:dt=""string""key=\"TestProgFileName\""">"
# 				"/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>\n<V dt:dt=""string"" Key=\"TestProgChecksum\""">195478132</V>\n<V dt:dt=""string"" key=\"HardwareMap\""">x28mct64tqfp</V>\n<V dt:dt=""string""key=\"TestFlow\""">f1-prd-std-ato-iqc</V>\n<V dt:dt=""string"" key=\"Environment\""">25C</V>\n<V dt:dt=""string"" key=\"HandlerType\""">Tapestry PH-1</V>\n<V dt:dt=""string"" key=\"SenderID\""">TapestryTAPCC071</V>\n<V dt:dt=""string"" key=\"TestMode\""">QC</V></Root>\n\0"
# )
x = "SetupTester\n{7C14C04C-6765-4693-8E04-B34FCA8CC544}\\1234501\n"+\
            "<V dt:dt=""string""key=\"ProductID\""">DECU1TV2XC10HD</V>\n"+\
            "<Vdt:dt=""string"" key=\"LotID\""">MTAI152402570.000</V>\n"+\
            "<V dt:dt=""string"" key=\"HandlerID\""">Manual</V>\n"+\
            "<V dt:dt=""string"" key=\"TempSetpoint\""">25</V>\n"+\
            "<V dt:dt=""string"" key=\"OperatorID\""">finalop</V>\n"+\
            "<V dt:dt=""string"" key=\"PartNum\""">18F67K</V>\n"+\
            "<V dt:dt=""string""key=\"DeviceType\""">QTP</V>\n"+\
            "<V dt:dt=""string"" key=\"CPOnChecksum\""">FFFF</V>\n"+\
            "<Vdt:dt=""string"" key=\"CPOffChecksum\""">EEEE</V>\n"+\
            "<V dt:dt=""string"" key=\"QCode\"""></V>\n"+\
            "<V dt:dt=""string""key=\"TestProgFileName\""">/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una</V>\n"+\
            "<V dt:dt=""string"" Key=\"TestProgChecksum\""">195478132</V>\n"+\
            "<V dt:dt=""string"" key=\"HardwareMap\""">x28mct64tqfp</V>\n"+\
            "<V dt:dt=""string""key=\"TestFlow\""">f1-prd-std-ato-iqc</V>\n"+\
            "<V dt:dt=""string"" key=\"Environment\""">25C</V>\n"+\
            "<V dt:dt=""string"" key=\"HandlerType\""">Tapestry PH-1</V>\n"+\
            "<V dt:dt=""string"" key=\"SenderID\""">TapestryTAPCC071</V>\n"+\
            "<V dt:dt=""string"" key=\"TestMode\""">QC</V></Root>\n\0"


y = 'SetupTester\n{7C14C04C-6765-4693-8E04-B34FCA8CC544}\\1234501\n'+\
            '<Root xmlns:dt="urn:schemas-microsoft-com:datatypes">'+\
            '<Dictionary key="Top">'+\
            '<V dt:dt="string" key="ProductID">LEAK1TN2XAXF</V>'+\
            '<V dt:dt="string" key="LotID">MMT-230401629.000</V>'+\
            '<V dt:dt="string" key="HandlerID">TapestryZ</V>'+\
            '<V dt:dt="string" key="TempSetpoint">25</V>'+\
            '<V dt:dt="string" key="OperatorID">finalop</V>'+\
            '<V dt:dt="string" key="PartNum">24F16KA102</V>'+\
            '<V dt:dt="string" key="DeviceType">OTP</V>'+\
            '<V dt:dt="string" key="CPOnChecksum">0</V>'+\
            '<V dt:dt="string" key="CPOffChecksum">0</V>'+\
            '<V dt:dt="string" key="QCode">0</V>'+\
            '<V dt:dt="string" key="TestProgFileName">P:\LEAK0\LEAK0_B56\LEAK0_B56.XLS</V>'+\
            '<V dt:dt="string" key="TestProgChecksum">29187440</V>'+\
            '<V dt:dt="string" key="HardwareMap">x24mct28ssop</V>'+\
            '<V dt:dt="string" key="TestFlow">f1-prd-std-28L</V>'+\
            '<V dt:dt="string" key="Environment">FS1@25C</V>'+\
            '<V dt:dt="string" key="HandlerType">Tapestry PH-1</V>'+\
            '<V dt:dt="string" key="SenderID">TapestryZ</V>'+\
            '<V dt:dt="string" key="TestMode">FT</V>'+\
            '</Dictionary>'+\
            '</Root>\n\0'

print(y.find('key="TestProgChecksum'))
ind = y.find('key="TestProgChecksum')
new = y[:ind] + 'K' + y[ind+1:]
print(new)

ind2 = new.find('TestProgFileName') + 18
# print(new[:ind2])
for i in range(ind2,len(new)):
	if(new[i] == '<'):
		eind2 = i
		break
new2 = new[:ind2] + '/mnt/d10tp/35468/35468_FT_U1709_A7/35468_FT_U1709_A7.una' + new[eind2:]
print(new2)





# if(x == y):
# 	print('TRUE')

# else:
# 	print("FALSE")
# 	for i in range(0,len(x)):
# 		if(x[i] != y[i]):
# 			print(x[i] , y[i],i)