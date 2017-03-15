def help():
	am5 = 0
	while am5 < 51:
		Root = input ("type help for a list of commands:")
		if Root == "help":
				print ("Cc - Grabs credit card numbers if backdoor completed")
				print ("Rat - instantly rat someone if you have their ip")
				print ("exit - exits shell")
		elif Root == "Cc":
				import random
				Ccs = ["363286234934103 - American Express", "4591456347672413 - visa", "5467732465406828 - MasterCard", "5496764423177261 - MasterCard","5445195009315094 - MasterCard","5174660863337358 - MasterCard", "5297735754256313 - MasterCard", "5299746312918953 - MasterCard","5424876291143808 - MasterCard", "5558357088099089 - MasterCard", "5555673197117353 - MasterCard", "5251024559367482 - MasterCard", "5471231233141704 - MasterCard", "5113539306960758 - MasterCard", "4532759568148241 - Visa 16 Dig.", "4485429928350575 - Visa 16 Dig.", "4066948875933726 - Visa 16 Dig.", "4916801869421293 - Visa 16 Dig.", "4716072598516447 - Visa 16 Dig.", "4716817304451960 - Visa 16 Dig.", "4532483608950983 - Visa 16 Dig.", "4783827205725881 - Visa 16 Dig.", "4539807644535692 - Visa 16 Dig.", "4731254252396081 - Visa 16 Dig.", "343437580711307 - American Express", "341831103860835 - American Express.", "340084020018175 - American Express", "377806123899804 - American Express", "379400446434982 - American Express"]
				CcG = Ccs[random.randrange(len(Ccs))]
				print (CcG)
		elif Root == "rat":
				ratp = input ("Enter your port to redirect rat to:")
				ratI = input ("Enter Remote computers Ip address:")
				print ("cannot find host, please try again later")
		elif Root == "exit":
				return





def main():
	import time
	import socket
	import random
	print ("make sure you enter a valid site")
	Site = input ("what site do you want to hack:")
	time.sleep(4) #delay five secs
	
	print ("gathering", Site, "recources........")
	time.sleep(1)
	print (socket.gethostbyname(Site))
	print ("")
	port = 443
	Rans = ["backdoor.php", "1337.php", "h4xor.php", "l33t.php", "anonemoose.php", "hax.php", "Rats.php"]
	Nme = Rans[random.randrange(len(Rans))]
	print ("Injecting",Nme,"into",Site, "now")
	time.sleep(2)
	print ("Injected succesfully [+]")
	print ("")
	print ("opening",Nme,"in remote shell")
	time.sleep(5)
	trck = ["2", "3", "4", "5"]
	trckR = trck[random.randrange(len(trck))]
	print (trckR, "trackers removed")
	time.sleep(3)
	print ("Opened Remote shell on---")
	print ("port:",port)
	print ("ip:",socket.gethostbyname(Site))
	help();
	
	
	return



import sys
import time
am = 0
while am < 50:
	longstring = """
	      .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'"""
	l33t = input("are you l33t enough:")
	if l33t == "yes":
		print (longstring)
		main();
	elif l33t == "no":
		print ("YOU, SHALL NOT, PAAAASSSSS")
		time.sleep(3)
		sys.exit(1)
	else:
		print ("yes or no")
		
#random comment that serves no purpose
	
