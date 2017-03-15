import os
import getpass
import smtplib
def mailTst():
	x = int(input ("Input the number Zero (0):"))
	while x < y:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(OutUsr, OutPass)
		msg = OutMsg
		server.sendmail(OutUsr, OutReciptent, msg)
		server.quit()
		x+=1
		print ("sent", x, "succesfully")

OutUsr = input ("what is your email:")
OutPass = getpass.getpass("what is your password:") #hides user input
OutMsg = input ("what message do you want to send:")
OutReciptent = input ('who are you sending it to:')
y = int(input ("how many times to send:"))
mailTst();
