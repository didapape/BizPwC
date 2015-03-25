import smtplib
#import email
import os
#inicio funcion

def enviarmail(msg):
    server = smtplib.SMTP('es-hub000', 25)
    #Next, log in to the server
    try:

        fromaddr = 'diego.d.pandales@es.pwc.com' #input(u'from')
        tolist = ['diego.pandales@bizagi.com','didapape@gmail.com']#input('A quien lo enviara: ').split()
        sub =   'pruebas py'#input('Subject: ')''

        message = """Content-type: text/html\n
        Subject: SMTP HTML e-mail test\n

        <br>This is an e-mail message to be sent in HTML format
        <br>    
        <b>This is HTML message.</b>
        
        <p>Conclusi&oacute;n</p>
        <h1>This is headline.</h1>
        """
        #server.ehlo()
        #server.starttls()
        #passw= "***"
        #server.login("bizagipwc", "$")
        #Send the mail
        
        server.sendmail(fromaddr,tolist, message)
        print ("Mail enviado")
    except BaseException as e:
        print ("Falló enviando el Mail:"+str(e))

#fin funcion

enviarmail("Subject:pruebas \n To:didapape@gmail.com\nMail enviado automaticamente")

