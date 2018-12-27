#!/usr/bin/python2
import os, platform, time, random
sembarang = random.randint(1,3)

err_keyint = "[!] Keyboard Interrupted by User !!!"
err_invld = "[!] Error: Invalid number selected !"
err_invalid = "[!] Error: Invalid option !"
err_blank = "[!] Error: Don't leave it blank !"
err_cantcon = "[!] Error: Can't connect with Target !"
err_cantconp = '''[!] Error: Can't connect to Target's Port !
	Are You sure that Port is opened and allow connection ?
	Try to scan it with Nmap'''
err_cantfind = '''[!] Error: Can't reach Target ! Are You sure Your Target
	is Online ? Are the URL is correct ? Are You Online ?'''
err_cantbck = "[!] Error: Can't go back ! this is the main Modules !"
err_notavai = '''[!] Sorry: This Modules is currently not available right now...
	This Modules maybe Unlocked in the next Version of M-Evil Tools :)
	so...stay with Me :)'''
err_bukalst = '''[!] Error: Can't open List File ! The file is too large
	or the File is not exists or corrupted !
	Please Try Again !'''
err_bacalst = '''[!] Error: Can't read List File ! The file is too large
	or the File is not exists or corrupted !
	Please Try Again !'''
banner1 = '''
      _____                 _____                _
     |  __ \               /  __ \              | |
     | |  \/_ __ ___ ______| /  \/_ __ __ _  ___| | __
     | | __| '_ ` _ \______| |   | '__/ _` |/ __| |/ /
     | |_\ \ | | | | |     | \__/\ | | (_| | (__|   <
      \____/_| |_| |_|      \____/_|  \__,_|\___|_|\_|

      ---{ Gm-Crack v1 }---{ Coded by M-XacT-666 }---
'''
banner2 = '''
	 _________                 _________                   ______
	 __  ____/______ ___       __  ____/____________ _________  /__
	 _  / __ __  __ `__ \_______  /    __  ___/  __ `/  ___/_  //_/
	 / /_/ / _  / / / / //_____/ /___  _  /   / /_/ // /__ _  ,<
	 \____/  /_/ /_/ /_/       \____/  /_/    \__,_/ \___/ /_/|_|

		  ---{ Gm-Crack v1 }---{ Coded by M-XacT-666 }---
'''
banner3 = '''
	  ______           ______                  _
	 / _____)         / _____)                | |
	| /  ___ ____ ___| /       ____ ____  ____| |  _
	| | (___)    (___) |      / ___) _  |/ ___) | / )
	| \____/| | | |  | \_____| |  ( ( | ( (___| |< (
	 \_____/|_|_|_|   \______)_|   \_||_|\____)_| \_)

	 ---{ Gm-Crack v1 }---{ Coded by M-XacT-666 }---
'''
def clearscreen(x):
	if x == "Windows":
		os.system('CLS')
	else:
		os.system('clear')
def tidur(x):
	time.sleep(x)
def keluar():
	print ""
	print "[*] Closing Tools..."
	tidur(1)
	print "[^] Thanks for using My Tools !"
	exit()
def banner(x):
	if x == 1:
		print banner1
	elif x == 2:
		print banner2
	elif x == 3:
		print banner3
def judul():
	banner(sembarang)