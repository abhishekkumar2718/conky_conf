#!/usr/bin/python3

import os
import shutil

""" Check if any previous files are left """

if os.path.exists(os.path.expanduser('~/.conky')):
	var = input("Previous files are not deleted. Delete ? (Y/N) : ")
	if var == 'Y':
		shutil.rmtree(os.path.expanduser('~/.conky'))
		os.mkdir(os.path.expanduser('~/.conky'))
	else:
		print("Delete any previous files before procceding.")
		exit()
else:
	print(".conky/ does not exist. Procceding to create.")
	os.mkdir(os.path.expanduser('~/.conky'))

""" Copying all relevant files to .conky/ 
    In future, consider taking dimensions of monitor, font size from user. 	
"""

filelist = [ "cal.txt", "events.txt", "info.rc", "music_info.sh", "time_event.rc", "todo.rc", "todo.txt" ]

for name in filelist:
	shutil.copyfile(name,os.path.expanduser('~/.conky/'+ name))

print("Files successfully copied.")

""" Make executable 'conky_start' in bin/ """

if os.path.exists(os.path.expanduser('~/bin')):
	print("bin/ exists. Procceding to make executable.")
	if os.path.exists(os.path.expanduser('~/bin/conky_start')):
		var = input("Previous 'conky_start' found. Delete ? (Y/N) : ")
		if var == 'Y':
			os.remove(os.path.expanduser('~/bin/conky_start'))
			shutil.copyfile('conky_start',os.path.expanduser('~/bin/conky_start'))
		else:
			print("'conky_start' not removed.")	
	else:
		copyfile("conky_start",os.path.expanduser('~/bin/conky_start'))
else:
	print("bin/ does not exists. Creating.")
	os.makedir(os.path.expanduser('~/bin'))
	shutil.copyfile('conky_start',os.path.expanduser('~/bin/conky_start'))
		
""" Cleanup """

input("Please change your wallpaper manually before procceding./nPress any key to continue.")

var = input("Configuration done. Remove installer and other associated files ? (Y/N) : ")
if var == 'Y':
	os.chdir(os.pardir)
	shutil.rmtree('conky_conf')

