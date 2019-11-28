from twilio.rest import Client
import smtplib

def sendmail(message,sender,receiver,password):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password)

    s.sendmail(sender, receiver, message)
    s.quit()

def sendmsg(message,receiver):
    account_sid = 'AC86ee91e8491f5c9ced042224245b8821'
    auth_token = 'd88eac98af6ee2498c4e512fbfd7ef76'
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=message,from_='+12055288894',to=receiver) 