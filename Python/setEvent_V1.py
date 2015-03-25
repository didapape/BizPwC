from parametros import * #archivo con parametros usados.
def setEvent(xmlmsg, bGenerarSalida):
    from suds.client import Client
    
    import xml.dom.minidom 
    import xml.etree.ElementTree as ET
    errorsolo=str('')

    
    url=parametros['urlSetEvent']
    
    client = Client(url)
   # print (client)
    resp =  client.service.setEventAsString(xmlmsg)
    #print (resp)
    #xmlDocument = xml.dom.minidom.parseString (resp);
    if bGenerarSalida==True:
        entrada= ET.fromstring(xmlmsg)
        processRadNumber=''
        xmlDocument=ET.fromstring(resp)

        for proc in entrada [2][0].findall('EventData'): 
            try:
                processRadNumber=proc.find('radNumber').text
            except:
                processRadNumber=proc.find('idCase').text


     
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

    return errorsolo
#fin funcion

'''
f= open('c:\\temp\\setEvent.txt','r')
xmldata= ""
while 1:
    line = f.readline()
    if not line:break
    setEvent(line)

f.close()
'''