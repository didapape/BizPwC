import sys, os
from parametros import *
from CDataBase import * 
#funcion para crear trace
def trace(sFileName,sLog):
    f = open(sFileName+'.log', 'a') #create new file for writing
    f.write(sLog+'\n') #write first line
    f.close()
    print (sLog)
#fin funcion
    
def setEvent(xmlmsg,iterador):
    from suds.client import Client
    import xml.dom.minidom 
    import xml.etree.ElementTree as ET
    url = parametros['urlSetEvent']
    client = Client(url)
   # print (client)
    
    resp =  client.service.setEventAsString(xmlmsg)
    #print (resp)
    #xmlDocument = xml.dom.minidom.parseString (resp);
    entrada= ET.fromstring(xmlmsg)
    processRadNumber=''
    xmlDocument=ET.fromstring(resp)
    print (resp)

    for proc in entrada [2][0].findall('EventData'): 
        processRadNumber=proc.find('radNumber').text

    errorsolo=str('')
    try:
        for errores in xmlDocument[0].findall('processError'): 
            errorsolo=errores.find('errorMessage').text
    except:
          errorsolo=str('')

    if  errorsolo !=None and errorsolo!='':       
        print (  str(iterador) + ';' + processRadNumber + ';' + errorsolo)
       # print ( errorsolo)
    else:
        print ( str(iterador) + ';' + processRadNumber + ';EJECUTADO' )

    return errorsolo


import xml.etree.ElementTree as ET1
print("INICIO:" )
db=CDataDabase(parametros['connectionStringIPower'])
print (db.connectionString)
squery="select   intLinkId,intOptyCode,chClientJobCode,chCaseNumber,intCaseId,dcAjuste,xmlBizagi,btProcess,vcErrMsg from tblCRMBZGLinkAjuste where intLinkId = 38509 and vcerrmsg like '%time%'";
cur=db.executeQuery(str(squery))
xmldata= ""
i = 1

registros=cur.fetchall()
print ("# Registros a procesar:"+ str(cur.rowcount))
print("Inicio Ciclo..." )
for registro in registros:
    line = str(registro[6])#xmlBizagi
    #print (line)
    try:
        inLine = ET1.fromstring(line)
        processRadNumber = ''
        
        for proc in inLine [2][0].findall('EventData'): 
            processRadNumber = proc.find('radNumber').text
            
        errorSetEvent=setEvent(line,i)

        if(errorSetEvent!=''):
            db.executeCommand("update tblCRMBZGLinkAjuste set btprocess =1, vcerrmsg='RELANZADO OK' WHERE INTLINKID=" +str(registro[0]))
        else:
            db.executeCommand("update tblCRMBZGLinkAjuste set btprocess =0, vcerrmsg='ERROR:" + errorSetEvent+"' WHERE INTLINKID=" +str(registro[0]))

    except BaseException as e:
        #print (  str(i) + ';' + processRadNumber + ';ERROR :: ' + str(e))
        db.executeCommand("update tblCRMBZGLinkAjuste set btprocess =0, vcerrmsg='ERROR:" + str(e)+"' WHERE INTLINKID=" +str(registro[0]))

    i = i + 1
    
print("FIN:" )
