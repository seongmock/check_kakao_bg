#!/opt/QPython3/bin/python3

from datetime import date
import sqlite3
import requests
import os
from pushbullet import Pushbullet
#from telegram_.telegram_ import send_message

# Connect DB
con = sqlite3.connect('/share/my/Kakao/kakao.db')
cur = con.cursor();

#Create Table
try:
  cur.execute("CREATE TABLE Check_hist(Date text, Status text);")
except:
  pass;

today = date.today()
target = today.strftime('%Y%m');


#Check Already checked or not
cur.execute("SELECT * FROM Check_hist WHERE Date = %s;"%target);
for row in cur:
  exit();


#Check Web Respose
url='https://store.kakaofriends.com/kr/brand/wallpaper%s'%target;
r = requests.get(url);

#if Page Exist Save and Send
if (r.status_code==200):
  #send_message("%s\n%s"%("Download Kakao BG", url));
  api_key = "xxx"
  pb = Pushbullet(api_key, "xxx")
  pb.push_link("Download Kakao BG", url)
  
  file_url = "https://store.kakaofriends.com/download?url=https://t1.kakaocdn.net/friends/prod/brand/%s_type1_1440.jpg"%target
  pb.push_link("Android Version", file_url)
  file_url = "https://store.kakaofriends.com/download?url=https://t1.kakaocdn.net/friends/prod/brand/%s_type1_2880.jpg"%target
  pb.push_link("PC Version", file_url)
  
  cur.execute("INSERT INTO Check_hist Values(\'%s\',\'%s\');"%(target, "O"));
  con.commit();
  con.close();
  exit();


###### tele.py Contents ######
#import telegram
#import sys
#text = ""
#for item in sys.argv[1:]:
#    text = text + " " + item;
#gram_token = 'Use own TOKEN'
#chat_id = 'Use own chat_id'
#mybot = telegram.Bot(token= gram_token)
#mybot.sendMessage(chat_id = chat_id, text=text);
#print("[Telegram] Send "+text);
####################################
