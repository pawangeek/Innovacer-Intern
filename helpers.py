from twilio.rest import Client
import smtplib

def sendmail(message,sender,receiver,password):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password)

    s.sendmail(sender, receiver, message)
    s.quit()

def sendmsg(message,receiver):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=message,from_='+12055288894',to=receiver) 
