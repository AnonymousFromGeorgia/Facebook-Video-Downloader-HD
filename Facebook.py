#!/usr/bin/env python

import os
os.system('clear')

import signal

def keyboardInterruptHandler(signal, frame):
    print("\nპროგრამა გაითიშა.".format(signal))
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

import pyfiglet 
  
result = pyfiglet.figlet_format("Facebook.com") 

print(result)
print("Facebook-Video-Downloader-HD ფეისბუქიდან ვიდეოების გადმომწერი")
print("--------------------------------------------------------------------")
print("https://github.com/AnonymousFromGeorgia/Facebook-Video-Downloader-HD")
print("--------------------------------------------------------------------")

from datetime import datetime
from tqdm import tqdm
import requests
import re

url = input("შეიყვანეთ ვიდეოს ბმული (URL): ")
x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

if x:
    html = requests.get(url).content.decode('utf-8')
else:
    print("--------------------------------------------------")
    print("მითითებული ვიდეო ვერ მოიძებნა.")
    print("--------------------------------------------------")
    print("პროგრამის ავტორი: გიო რგი")
    print("--------------------------------------------------")
    print("YouTube - https://youtube.com/AnonymousFromGeorgia")
    print("--------------------------------------------------")
    print("Github - https://github.com/AnonymousFromGeorgia")
    print("--------------------------------------------------")
    print("Facebook - https://facebook.com/anonimaluri")
    print("--------------------------------------------------")
    print("Twitter - https://twitter.com/anonimaluri")
    print("--------------------------------------------------")
    print("ანონიმუსი საქართველოდან - Anonymous From Georgia")
    print("--------------------------------------------------")
    exit()

_qualityhd = re.search('hd_src:"https', html)
_qualitysd = re.search('sd_src:"https', html)
_hd = re.search('hd_src:null', html)
_sd = re.search('sd_src:null', html)

list = []
_thelist = [_qualityhd, _qualitysd, _hd, _sd]
for id,val in enumerate(_thelist):
    if val != None:
        list.append(id)

try:
    if len(list) == 2:
        if 0 in list and 1 in list:
            _input_1 = str(input("\nდააჭირეთ კლავიშ 'A'-ს რათა გადმოწეროთ ვიდეო HD ხარისხში.\nდააჭირეთ კლავიშ 'B'-ს რათა გადმოწეროთ ვიდეო SD ხარისხში.\n: ")).upper()
            if _input_1 == 'A':
                print("\nმიმდინარეობს ვიდეოს გადმოწერა HD ხარისხით.")
                video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("--------------------------------------------------")
                print("ვიდეოს გადმოწერა წარმატებით დასრულდა.")
                print("--------------------------------------------------")
                print("პროგრამის ავტორი: გიო რგი")
                print("--------------------------------------------------")
                print("YouTube - https://youtube.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Github - https://github.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Facebook - https://facebook.com/anonimaluri")
                print("--------------------------------------------------")
                print("Twitter - https://twitter.com/anonimaluri")
                print("--------------------------------------------------")
                print("ანონიმუსი საქართველოდან - Anonymous From Georgia")
                print("--------------------------------------------------")   

            if _input_1 == 'B':
                print("\nმიმდინარეობს ვიდეოს გადმოწერა SD ხარისხით.")
                video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("--------------------------------------------------")
                print("ვიდეოს გადმოწერა წარმატებით დასრულდა.")
                print("--------------------------------------------------")
                print("პროგრამის ავტორი: გიო რგი")
                print("--------------------------------------------------")
                print("YouTube - https://youtube.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Github - https://github.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Facebook - https://facebook.com/anonimaluri")
                print("--------------------------------------------------")
                print("Twitter - https://twitter.com/anonimaluri")
                print("--------------------------------------------------")
                print("ანონიმუსი საქართველოდან - Anonymous From Georgia")
                print("--------------------------------------------------")   

    if len(list) == 2:
        if 1 in list and 2 in list:
            _input_2 = str(input("ბოდიში! სამწუხაროდ ვიდეო არაა ხელმისაწვდომი HD ხარისხში. გნებავთ, რომ მაინც გადმოწეროთ? ('Y' ან 'N'): ")).upper()
            if _input_2 == 'Y':
                print("\nმიმდინარეობს ვიდეოს გადმოწერა SD ხარისხით.")
                video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("--------------------------------------------------")
                print("ვიდეოს გადმოწერა წარმატებით დასრულდა.")
                print("--------------------------------------------------")
                print("პროგრამის ავტორი: გიო რგი")
                print("--------------------------------------------------")
                print("YouTube - https://youtube.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Github - https://github.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Facebook - https://facebook.com/anonimaluri")
                print("--------------------------------------------------")
                print("Twitter - https://twitter.com/anonimaluri")
                print("--------------------------------------------------")
                print("ანონიმუსი საქართველოდან - Anonymous From Georgia")
                print("--------------------------------------------------")
            if _input_2 == 'N':
                exit()

    if len(list) == 2:
        if 0 in list and 3 in list:
            _input_2 = str(input("ბოდიში! სამწუხაროდ ვიდეო არაა ხელმისაწვდომი SD ხარისხში. გნებავთ, რომ მაინც გადმოწეროთ? ('Y' ან 'N'): \n")).upper()
            if _input_2 == 'Y':
                print("\nმიმდინარეობს ვიდეოს გადმოწერა HD ხარისხით.")
                video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("ვიდეოს გადმოწერა წარმატებით დასრულდა.")
                print("--------------------------------------------------")
                print("პროგრამის ავტორი: გიო რგი")
                print("--------------------------------------------------")
                print("YouTube - https://youtube.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Github - https://github.com/AnonymousFromGeorgia")
                print("--------------------------------------------------")
                print("Facebook - https://facebook.com/anonimaluri")
                print("--------------------------------------------------")
                print("Twitter - https://twitter.com/anonimaluri")
                print("--------------------------------------------------")
                print("ანონიმუსი საქართველოდან - Anonymous From Georgia")
                print("--------------------------------------------------")
            if _input_2 == 'N':
                exit()
except(KeyboardInterrupt):
    print("\nპროგრამა გაითიშა.")
