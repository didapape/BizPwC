import pypyodbc as pyodbc
from parametros import * #archivo con parametros usados.
#Clase para manipulación de base de datos
class  CDataDabase (object):

    connectionString=''
    #Constructor
    def __init__(self, sConnectionString):
        self.connectionString = sConnectionString
        if self.connectionString=='':
        #    self.connectionString = pyodbc.connect('DRIVER={SQL Server};SERVER=ES-BPMTRN002;DATABASE=BizagiTRN;UID=Bizagi;PWD=BizagiBPM2012')
            raise 'ERROR: Debe definir la cadena de conexion'
    #Ejecutar una query (Select)
    #Retorna un cursor (datatable) con base en la consulta
    def executeQuery (self, sQuerySelect):
        cnxn = pyodbc.connect( self.connectionString)
        cursor = cnxn.cursor()
        cursor.execute(sQuerySelect)
        #recorre: solo para dummy
        '''
        for row in cursor.fetchall():
            for field in row: 
                print (field)
            print ('')
            '''
        #retornar la consulta
        #cnxn.close()
        return cursor;

    #fin executeQuery

    #Ejecutar comando SQL contra DB
    def executeCommand(self,sCommand):
        cnxn = pyodbc.connect( self.connectionString)
        cursor = cnxn.cursor()
        retorno=False
        try:
            cursor.execute(sCommand)
            cursor.commit()
            cnxn.close()
            retorno=True
        except  BaseException as e:
               print('Ocurrió un error Ejecutando el comando:'+sCommand +str(e))

        retorno
    #fin executeCommand
    #funcion obtener codigo de tabla
    def Get_IdSurrogateKey(self,sTabla, sColumnaFiltro,  sValor, sColumnaRetorno):
        cursor= self.executeQuery(str("select  "+sColumnaRetorno+" from " +sTabla+" where "+sColumnaFiltro+ " ='" +sValor +"'"))
        fila  =cursor.fetchone()
        if fila is not  None:
            return fila[0]
        else:
            return None
     #fin Get_IdSurrogateKey
#fin Clase
'''

db=CDataDabase(parametros['connectionString'])
print (db.connectionString)
squery="Select * from p_los";
cur=db.executeQuery(str(squery))


  
for row in cur.fetchall():
    for field in row: 
        print (field)
    print ('')    
        
#except :
#print ('Fin por error:')
'''
