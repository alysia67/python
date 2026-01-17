import time

import requests
import re
import os
#path  = input("path:")
path =r"C:\Users\alysia\Desktop\崩坏3"
url = "https://vodcnd09.myqqdd.com/20250917/ydQZOHFj/4172kb/hls/index.m3u8"
a = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36 Edg/143.0.0.0"
headers = {
    "User-Agent": a,  # 首字母大写，符合HTTP规范
    "Referer": "https://www.shankubf.com/",
    "Accept": "*/*",  # 补充接受任意内容类型
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive"  # 保持连接，减少断开概率
}

resp = requests.get(url,headers=headers)
for i in re.compile(r"AES-128,URI=\"(?P<key>.*?)\"").finditer(resp.text):
    open(path+"\\key.key","wb").write(requests.get("https://vodcnd09.myqqdd.com"+i.group("key"),headers=headers).content)
print(resp.text)
baseurl ="https://vodcnd09.myqqdd.com"
jx1 = re.compile(r",\n/(?P<url2>.*?).ts",re.S)
result1 = jx1.finditer(resp.text)
num = 0
for i in result1:
    url3 = baseurl+"/"+i.group("url2")+".ts"
    print(url3)
    resp = requests.get(url3,headers=headers)
    open(f"{path}"+"\\"+f"a{num}.ts","wb").write(resp.content)
    num+=1
    open(path+"\\www.ts","ab").write(resp.content)
    time.sleep(3)
ffmpeg = r"C:\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"
key1 = open(rf"{path}\key.key","r").read().strip()
file = r"C:\Users\alysia\Desktop\崩坏3\www.ts"
os.system(f"cd {path} & {ffmpeg} -i {file} -c copy -bsf:a aac_adtstoasc -decryption_key {key1} -iv 0x00000000000000000000000000000000 final.mp4")
