import os

domain="gmail.com"
username="musikdpp"
password="Sebasdanna1228"
com="wget -q -O - https://mail.google.com/a/"+domain+"/feed/atom --http-user="+username+"@"+domain+" --http-password="+password+" --no-check-certificate"

temp=os.popen(com)
msg=temp.read()
index=msg.find("<fullcount>")
index2=msg.find("</fullcount>")
fc=int(msg[index+11:index2])

if fc==0:
    print("No hay mensajes nuevos")
else:
    print(str(fc)+" mensajes nuevos")