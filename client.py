import telnetlib

tn = telnetlib.Telnet('127.0.0.1', 2001)
tn.write('0001 A1 01:13:02.877 23[CR]'.encode())
tn.close()






