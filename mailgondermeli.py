import time
from datetime import datetime
import datetime
import os
import sys
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gpio.init()
hareket = port.PA20
gpio.setcfg(hareket, gpio.INPUT)

mailgonder = "test"

def internet(mailgonder):
    gunvesaat = time.strftime("%d/%m/%Y %H:%M:%S")
    murat = "ehm"
    email = 'ehminternetcafebilgi@gmail.com'
    password = 'fsdfs' şifre
    send_to_email = 'muratdikmetas@gmail.com'
    subject = 'This is the subject' # The subject line
    message = (gunvesaat) +" " + 'Cafede Hareket Var'
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string() # You now need to convert the MIMEMultipart object t$
    server.sendmail(email, send_to_email, text)


while True:
    gunvesaat = time.strftime("%d/%m/%Y %H:%M")
    if gpio.input(hareket):
        print "hareketvar"
        internet(mailgonder)
        time.sleep(5)









