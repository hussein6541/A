# coder: https://t.me/russe20

import os
try:
                             import random,time,mechanize
                             import requests as russe20
                             from urllib.parse import urlencode

except:
        os.system('pip3 install requests;pip3 install mechanize')
        import random,time,mechanize
        import requests as russe20
        from urllib.parse import urlencode

W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'

def banner():

	os.system('clear')
	print (f"""\n\n\n\n                  -   {R}# {W}Coder: Sayco {R}  #   {W}  -\n 	       {R}-{W} Telegram: https://t.me/russe20 {R}-\n   {R  }               #{W}   emsayco Version: 1.0 {R} #\n\n""")
	domin = {'1':'Facebook','2':'Instagram','3':'Twitter','4':'Yahoo','5':'Hotmail'}
	[ print (f"{G}	~{W} {key} {G}-{W} {value} ") for key , value in domin.items() ]
	return domin

class checker:

	def __init__(sayco,email):
		sayco.email = email

	def Yahoo(sayco):

               sayco.email = sayco.email.split('@')[0]
               post = '/account/module/create?validateField=password'
               head = {
                'Host':'login.yahoo.com',
	        'Connection':'keep-alive',
	        'Content-Length':'18171',
	        "Origin": "https://login.yahoo.com",
	        'X-Requested-With': 'XMLHttpRequest',
        	'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Griffe T2 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36',
	        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        	'Accept':'*/*',
	        'Referer': 'https://login.yahoo.com/',
        	'Accept-Encoding': 'gzip, deflate',
	        'Accept-Language': 'ar-DZ,en-US;q=0.9',
        	'Cookie': 'B=avpo5g1g7tmij&b=3&s=va; GUC=AQEBAQFggCtgiEIh5ATW; A1=d=AQABBKoy12ACEEe_-vQMpnJGb42fAghgozYFEgEBAQErgGCIYAAAAAAAAMAAgAcIU9p-YIAF568&S=AQAAAkIJqU1e8OIUTcaAWMCkT34; A1S=d=AQABBKoy12ACEEe_-vQMpnJGb42fAghgozYFEgEBAQErgGCIYAAAAAAAAMAAgAcIU9p-YIAF568&S=AQAAAkIJqU1e8OIUTcaAWMCkT34&j=WORLD; GUCS=ATKAL7ZC; AS=v=1&s=tR1afqgt&d=A60f6fb5e|H2spAAz.2Sp6QuYKGXXzcd7ch.FP1G0iAkuXaLBkICyxj4ZzYACxdhuqwXexJrz3KK5UY5Qwor0tbjssuGU4U2DpOdzmhoSp2BEinffvp9kyVb5TD0D6865CT11HiN8Hf6wg4z_bEdBTYdc2S6xnqcEe0vSBqUQLlKcCwsyDMbJrg9MisMea0EhSSnGbrJwZsGpK.i57RmiZ33nw_Oo8X.UC5NPlsN0fIhXJ24uQwsfRYEqDPLePAzVCjv4ym0B5_l0f3w15WTgNB0RlYzVvJK3Sm6ejrsejH03XE5D4sjm8k_MvjnPDMbcGf9sueJ1mxl6yucql127xw.On_1axHBKV_GVMgKBqjSxqP03jtstjnN2W.jrr4Gv6HgSodNFhSnaomiTobIdO9RoFOfUicLmu8YIWAi_bedVJ44gOX9PD4u49hTZi2BQw5f4ORZfxFRqYVMZ9UYM4DOzBGuoIbXpsAit.xlD_fQcy2BtDUjQV9v_HrG4sRc2OJrMpv0HKstU2GDvS.stz8PV5IF8lePsxjXDJAZ7CHdOMsLRdHAjyEiGFRiKNPNNm6N8cu78JBkOZ37xMCl9d07PKn9f5tX50n9IemBnqUdh1V0Sl9NHzbNbmrvXOLGHYLDLt81RNjq7poitwGnAwTyN1ZYjl2tGpd.Wbuh5tatdG65HrlFgwuXogabK4fj6Rhq.B4.4_6ExGsDLdhcBMcaUroJBgNcG2oQqfV_A24EV.z56cVnSmIZjpD.oYAG_eTqaPgtXs7T3..uIKrr2w.mWH0wshjyfeC94ATV1K2uc0xEbR9m1Rw_HeW2eVlR.khGmWa2DKupp5_ygyl2m3dNRu74N4qENKXy1SVuisoGGVYtBRxfFnqcS4kTpT0fbvj7Ave.EinMFNd3GwFRdXsm4p.BCPwiTBc_Q0K.Ehxrv2yaS9Zn9Fa7tj07RJW2XGpjLRBVXtLIjlIXbSHe2JHFkZtrPCiqBPvcq6PQ6XS3_1o7BAybjZqPfKKyx2rOn.MrNlVx6eGA4mLxTqXKU7t1GxHlJQipZpmT81G1QkwfDhzwQ1WyVfab4Df00GTwZQWzC1mjZG.5bWq5S478QRScc-~A|B60f6fc55|PaM0JA_.2TpUzUyEasKC1KJX5FDglpvdiPKUnZ7QFIrnb9CP7bB8hwDerQSX3XgqCjFtIouXhupY.8vapBxg_Asi8JTNJ5NdyoL4P8pQax0pc1dYWR4GhfTqK0tOy6WqnDCdyEzkYTqlXGa35Dr1iAhEowQ51cFah40A.xrxYPowVXe1AcZFguSRKTi56PsYReDUtutkheKS5Y2rX8ywRf6fJO1Pviv5ckGdT5CkmxUCMWk2RegXuI3V0rDe_HFk1eCbA3TlnjbLtrSblwCLyuZHh_ht8GTapjLFnKSY9eINTrRHpVjJ1quQ8lFc9kGsoGbW_8cn1H95.k2sSImJdRPcrRc20A2.4cp65yxYQe9X3I5368BavSTuCtjo5f52N4NQNdASLZqUruZn18DHMwMhfnTSFiT2wyuFy3sUHeyqmWzhDROsCaO7IchEwFmDHKYjLg6GtwTVJPAPI5Lo0tJedpwbf_eDpTrlKCKm2d.QJpGqkPUPj_B3HhfZZsyoh.QGQN0lhL74atSKDwo6Y1qIY0aYVHUWRHR.NTGcImlAba1.eUDmJ5Fe.emgnVFYUvUf2qVmFtqtVwH5.x1pRkUEgThf_Zkltmc7cpX7WJtEmhbzucvXOXCCbp8UA.aBkIerDiruXTSw1ZeJ5Be7lrbe.l1xJGAx88w00Cabm56o351p3ddInZ7cmJx0RZ1umU7Qha33.X2utxA.sxWw3oaAZACT._Se3nM9fKgJzrY7X9AwqALT.XoQfueYBljAlH0qJL8I66ljbhqr..QhCogldjBJ.ozPvGPqCRWCjYAeYa6BXxZZ_q.GMIVJWjOSLvnTnt0gp1bO.qAzR_1nW.IJiyMh1uQ.JLcKd9JraA--~A'};data={"language":"ar-DZ","colorDepth":32,"deviceMemory":"unknown"
	        ,"pixelRatio":1.7000000476837158,"hardwareConcurrency":4,
        	"timezoneOffset":-60,"timezone":"Africa/Brazzaville",
        	"sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,
	        "cpuClass":"unknown","platform":"Linux armv7l","doNotTrack":"unknown",
	        "plugins":{"count":0,"hash":"24700f9f1986800ab4fcc880530dd0ed"},
        	"canvas":"canvas winding:yes~canvas","webgl":1,
	        "webglVendorAndRenderer":"ARM~Mali-400 MP","adBlock":0,
        	"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,
	        "hasLiedBrowser":0,"touchSupport":{"points":2,"event":1,"start":1},
        	"fonts":{"count":11,"hash":"1b3c7bec80639c771f8258bd6a3bf2c6"},
	        "audio":"124.08072748804261","resolution":{"w":"424","h":"753"},
        	"availableResolution":{"w":"753","h":"424"},
	        "ts":{"serve":1626712821242,"render":1626712819533}};url = "https://login.yahoo.com"+post;ur = f"&specId=yidreg&cacheStored=&crumb=g4rpM.Igx0K&acrumb=tR1afqgt&done=https://mail.yahoo.com/m/?.intl=xa&.lang=ar&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9zZWFyY2g_cT15YWhvbw&guce_referrer_sig=AQAAABRDbeqTas5I_X_6PENhbP4x3VtUH8CpbagRV-NSaRWXHXwedew_ZXILOnBQOmn9vdnFFN_oDrPgvLJF-6Tgtvu6ppSnZq2xEp3m0xJrLh-2KzJwZNnKY7Wnrc58CYHulbHzc7JoxMBaYLEaCgGKUvkJ7xrPzWNbmt_8ANVaWu09&googleIdToken=&authCode=&attrSetIndex=0&specData=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&firstName=sayco&lastName=sayco&yid={sayco.email}&password=gjakzjzjzbznn&shortCountryCode=DZ&phone=0667683858&mm=3&dd=5&yyyy=1990&freeformGender=U&signup=&signup";data = urlencode(data)+ur;resp = russe20.post(url,data=data,headers=head);return ('IDENTIFIER_NOT_AVAILABLE' in resp.text or 'IDENTIFIER_EXISTS' in resp.text ) and resp.status_code == 200


	def Hotmail(sayco):

                url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + sayco.email + "&_=1604288577990" # From : @xfff0800
                headers = {
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
                        "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                    }

                return 'MSAccount' in russe20.get(url,data='',headers=headers).text

	def Facebook(sayco):

                sayco.email2 = sayco.email.replace('@','&#064;')
                br = mechanize.Browser()
                br.set_handle_robots(False)
                url = 'https://mbasic.facebook.com/login/identify/?ctx=recover'
                br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
                br.open(url)
                br.select_form(nr=0)
                br.set_all_readonly(False)
                br["email"] = sayco.email
                req = br.submit()
                return sayco.email2 in str(req.read())

	def Instagram(sayco):

                sayco.email = urlencode({'em':sayco.email}).split('=')[1]
                sayco.url = "https://i.instagram.com/api/v1/users/lookup/"
                sayco.head = {'Host': 'i.instagram.com',
                'Connection':'keep-alive',
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3Ro=',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
                'Accept-Encoding': 'gzip, deflatet'} ; sayco.data = 'signed_body=acd10e3607b478b845184ff7af8d796aec14425d5f00276567ea0876b1ff2630.%7B%22_csrftoken%22%3A%22rZj5Y3kci0OWbO8AMUi0mWwcBnUgnJDY%22%2C%22q%22%3A%22'+sayco.email+'%22%2C%22_uid%22%3A%226758469524%22%2C%22guid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%2C%22device_id%22%3A%22android-1a9898fad127fa2a%22%2C%22_uuid%22%3A%22a475d908-a663-4895-ac60-c0ab0853d6df%22%7D&ig_sig_key_version=4' ;  return 'email' in russe20.post(sayco.url,headers=sayco.head,data=sayco.data).text

	def Twitter(sayco):

		sayco.session = russe20.session()
		sayco.session.get('https://twitter.com')
		return sayco.session.get(f'https://api.twitter.com/i/users/email_available.json?email={sayco.email}&send_error_codes=1').json()['taken'] == True

def main():

	list_d = banner()
	domin = input(f'\n{G}         ~{W} Chosee by number:{G} > {W} ')
	if domin in [ str(line) for line in range(1,6) ]:
		While = True ; status = False
		while While:
			print (f"{R}         ~{W} The file you entered doesn't exist. !{W}") if status else False
			combo = input(f'{G}         ~{W} Enter your combo:{G} > {W} ')
			While = False if combo in os.listdir() else True ; status = True

		emails = []
		[ emails.append(email) if '@' in email else False for email in open(combo,'r').read().split('\n') ]
		out = False ; new = []
		if list_d[domin].lower() in ['yahoo','hotmail']:
			out = True
			for line in emails:
				new.append(line) if list_d[domin].lower() in line else False

		emails = new if out else emails
		domin = list_d[domin]
		for line in emails:
			def true(email,site):
				open(f'{site}.txt','a').write(f'{email}\n')
				return f'exist ( {domin} )'
			false = f'not exist ( {domin} )'
			print (f'{G}	 ~ {W}{line} {G} -> {W} { true(line,domin) if eval(f"checker(line).{domin}()") else false  }')
	else:
		main()
main()

