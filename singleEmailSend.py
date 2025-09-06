# import required libraries

import smtplib

print("smtplib is available!")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


#configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORt = 587
SENDER_EMAIL = "entertest1@gmail.com"
SENDER_PASSKEY = "tyqofkmhpgddxiez"

# create single email function
def single_email_send(to_email:str, subject: str, body: str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg.attach(MIMEText(body, 'plain'))
    
    
    # start server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORt)
    server.starttls()  # create sequere connection
    server.login(SENDER_EMAIL, SENDER_PASSKEY) # login with email and password
    server.sendmail(SENDER_EMAIL, to_email, msg.as_string())  # email send
    server.quit() # close the server
    print(f"Successfully email send to {to_email}")
    

