from CDataBase import *
from setEvent import *
from parametros import * #archivo con parametros usados.
from datetime import date
import sys
#funcion para crear trace
def trace(sFileName,sLog):
    f = open(sFileName+'.log', 'a') #create new file for writing
    f.write(sLog+'\n') #write first line
    f.close()
    print (sLog)
#fin funcion

#funcio RegistroCobro (enviando el numero de factura)
def registroCobros(NUMERO_FACTURA):
    today = date.today()
    fileTrace="O2C_JobProcesarRegistroCobroFactura_" +str(today.year)+str(today.month)+str(today.day);
    trace(fileTrace,"***INICIO***");
    connString=parametros['connectionString']
    db=CDataDabase(connString)
    db.executeCommand("update  P_RegCobroFact_EntityKey set BAInstanceVirtualState=100")

    diasFactura=db.Get_IdSurrogateKey(str("P_ParametrosProceso"),str("SCodigo"),str("15"),str("IEntero"))
    diasFactura=diasFactura*(-1)


    trace(fileTrace,"No se Ejecutara Replicacion de Registros de Cobro..(dummy)");
    #replication=new BizAgi.EntityManager.CEMReplication();
    try:
        #replication.ReplicateEntity(10101);//P_RegCobroFact
        pass
    except:
        trace(fileTrace,"Falla en replicacion:"+e);

    trace(fileTrace,"Antes del Get Entity");

    cobrosFacturaTabla= db.executeQuery("Select ChBillNo from P_RegCobroFact where chBillno in('"+NUMERO_FACTURA+"')")
    
    trace(fileTrace,"Despues del Get Entity")

    sXml=str("<BizAgiWSParam>   <domain>es</domain><userName>dpandales002</userName><Events><Event><EventData><idCase>CASE_NUMBRE</idCase><eventName>EventoFacturaCobrada</eventName></EventData><Entities>")
    cobrosFacturaAll=cobrosFacturaTabla.fetchall()
    trace(fileTrace,"cuantos cobros par la factura:"+str(cobrosFacturaTabla.rowcount))
    listaCobros=[]
    for cobrosFactura in cobrosFacturaAll : #Recorrer cada registro cobro obteniendo la factura
        numeroFactura=cobrosFactura[0]; #ChBillNo
        if numeroFactura  not in  listaCobros:
            listaCobros.append(numeroFactura)
            entFactura= str(db.Get_IdSurrogateKey("P_Factura","SNumeroFactura",numeroFactura,"IdCaseFactura"))
            
            if entFactura is not None:
                trace(fileTrace,"Factura #:"+numeroFactura +" - Encontrada en bizagi:" + numeroFactura);
            
                xmlSetEvent=sXml.replace("CASE_NUMBRE",entFactura)
                xmlSetEvent=xmlSetEvent+"<M_Factura businessKey=\"SNumeroFactura='"+numeroFactura+ "'\"><IdM_Cobro><M_RegistroCobros>"
                #Obtener todos los registro de la factura actual y Hacer otro ciclo para enviar la coleccion de registros cobro completa y no uno a uno....!!!!
                regCobroPorFacturaTodos=  db.executeQuery("Select IntJnlDtlID, ChJnlType from P_RegCobroFact where chBillno='"+numeroFactura+"'")
                bNuevoRegistro=False #Utilizado para verificar que para la factura actual se incluya algun registro nuevo
                regCobroPorFacturaAll=regCobroPorFacturaTodos.fetchall()
                for  regCobroPorFactura in regCobroPorFacturaAll:#Recorrer cada rP_RegCobroFactegistro por factura, adicionando al mensaje solo si no se ha incluido
                    IntJnlDtlID=str(regCobroPorFactura[0])
                    ChJnlType=str(regCobroPorFactura[1])
                  
                    #Verificar que en M_RegistroCobro  ... no exista el mismo IdP_RegCobroFact ..por eos necesario el id desde ipower   ;)
                    entPRegCobro= db.executeQuery("Select idP_RegCobroFact from P_RegCobroFact_entityKey where IntJnlDtlID='"+IntJnlDtlID+ "' AND ChJnlType='"+ChJnlType+"'")
                    curRegCo=entPRegCobro.fetchone()
                    IdPRegCobro=''
                    if curRegCo is not None:
                        IdPRegCobro= str(curRegCo[0])
                    #verificar si el registro cobro ya fue procesado antes, utilizando el id del registro cobro
                    IdM_Cobro=db.Get_IdSurrogateKey("P_Factura","SNumeroFactura",numeroFactura,"IdM_Cobro")
                    filtro="IdP_RegCobroFactura="+IdPRegCobro+" AND M_Cobro="+str(IdM_Cobro) #OJO: Bk de PwC
                    registroExistentes=db.executeQuery("Select  count(*) from M_RegistroCobro where "+filtro).fetchone()[0]
                    trace(fileTrace,str('Registro existente para ('+str(filtro)+')') + str(registroExistentes))
                    if registroExistentes==0: #Si aun no se incluido este registro cobro, agregar a la coleccion definiendolo en el xml de envio
                        xmlSetEvent=xmlSetEvent+" <M_RegistroCobro><IdP_MedioCobro businessKey =\"SCodigoPwC='3'\"/>" #TODO: todos los cobros seran efectivo o ipower debe enviar el medio de pago???
                        xmlSetEvent=xmlSetEvent+"<IdP_RegCobroFactura businessKey=\"IntJnlDtlID='"+IntJnlDtlID+ "' AND ChJnlType='"+ChJnlType +"'\" /></M_RegistroCobro> " #OJO: Bk de PwC
                        bNuevoRegistro=True

                   
                #fin while regCobroPorFactura 
                xmlSetEvent=xmlSetEvent+"</M_RegistroCobros>  </IdM_Cobro></M_Factura> </Entities> </Event> </Events></BizAgiWSParam>"
                
                if bNuevoRegistro ==True: #solo si hay algun nuevo registro (no adicionado aun) para la factura.
                    trace(fileTrace,xmlSetEvent)
                    try:
                        retorno=setEvent(str(xmlSetEvent),False)
                        if(retorno==''):
                            trace(fileTrace,"Registro cobro aplicado")
                        else:
                            trace(fileTrace,"Erorr en setevent:"+ retorno)
                        
                    except:
                        e = sys.exc_info()[0]
                        print("ERORR SETEVENT")
                        print (e)
                        #trace(fileTrace,e)
                        
                
            #fin if hay factura  
       
    #Fin while registros cobro
    print ("Facturas seteadas:" )
    print( listaCobros)
    trace(fileTrace,"***FIN***")
#fin funcion Registro Cobro
    
registroCobros(str('34303354'))