# coder: https://t.me/russe20
#https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1

#https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fnext%26ref%3Ddbl%26fl%26login_from_aymh%3D1%26refid%3D8&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&ref=dbl&_rdr

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
	domin = {'1':'Facebook'}
	[ print (f"{G}	~{W} {key} {G}-{W} {value} ") for key , value in domin.items() ]
	return domin

class checker:

	def __init__(sayco,email):
		sayco.email = email




	def Facebook(sayco):

                sayco.email2 = sayco.email.replace('@','&#064;')
                br = mechanize.Browser()
                br.set_handle_robots(False)
                url = 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1 '
                br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
                br.open(url)
                br.select_form(nr=0)
                br.set_all_readonly(False)
                br["email"] = sayco.email
                req = br.submit()
                return sayco.email2 in str(req.read())



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
