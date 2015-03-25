#from parametros import * #archivo con parametros usados.
def setEvent( bGenerarSalida):
    from suds.client import Client
    
    import xml.dom.minidom 
    import xml.etree.ElementTree as ET
    errorsolo=str('')

    
    url='http://es-bpmpro001/BizagiBPM/webservices/cache.asmx?wsdl'#parametros['urlSetEvent']
    print("Limpiara cache en :" +url)
    client = Client(url)
   # print (client)
    resp =  client.service.CleanUpCache('*','*')
    #print (resp)
    #xmlDocument = xml.dom.minidom.parseString (resp);
    if bGenerarSalida==True:
            
        try:
            for errores in xmlDocument[0].findall('processError'): 
                errorsolo=errores.find('errorMessage').text
        except:
              errorsolo=str('')

        if  errorsolo !=None and errorsolo!='': 
             print (errorsolo)
           # print ( errorsolo)
        else:
            print ('Cache Limpiado' )

    return errorsolo
#fin funcion

setEvent(True)
input("Terminado!")