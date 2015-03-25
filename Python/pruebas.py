
import smtplib
import email
import os
#inicio funcion
def enviarmail(msg):
    
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #Next, log in to the server
    try:

        fromaddr = 'musikdpp@gmail.com' #input(u'from')
        tolist = 'didapape@gmail.com'#input('A quien lo enviara: ').split()
        sub =   'pruebas py'#input('Subject: ')''


        server.ehlo()
        server.starttls()
        server.login("musikdpp", "Sebasdanna1228")
        #Send the mail
        #msg = "\nHello!" # The /n separates the message from the headers
        server.sendmail(fromaddr,tolist,sub, msg)
        print ("Mail enviado")
    except:
        print ("Falló enviando el Mail")

#fin funcion



def setEvent(xmlmsg):
    from suds.client import Client
    import xml.dom.minidom 
    import xml.etree.ElementTree as ET
    url = 'http://es-bpmtrn001/Bizagitrn/webservices/workflowenginesoa.asmx?WSDL'
    client = Client(url)
   # print (client)
    resp =  client.service.setEventAsString(xmlmsg)
    #print (resp)
    #xmlDocument = xml.dom.minidom.parseString (resp);
    entrada= ET.fromstring(xmlmsg)
    processRadNumber=''
    xmlDocument=ET.fromstring(resp)

    for proc in entrada [2][0].findall('EventData'): 
        processRadNumber=proc.find('radNumber').text

    errorsolo=str('')
    try:
        for errores in xmlDocument[0].findall('processError'): 
            errorsolo=errores.find('errorMessage').text
    except:
          errorsolo=str('')

    if  errorsolo !=None and errorsolo!='': 
       
        print (  processRadNumber + ';' + errorsolo)
       # print ( errorsolo)
    else:
        print (processRadNumber )



f = open('c:\\temp\\setEvent.txt','r')
xmldata= ""
while 1:
    line = f.readline()
    if not line:break
    setEvent(line)

f.close()