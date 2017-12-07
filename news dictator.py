from bs4 import BeautifulSoup as bs
import requests as rs
from gtts import gTTS
from pygame import mixer
blabla="Ye bolke dikha"
#blabla=input()

client=rs.get("https://timesofindia.indiatimes.com",'html.content')
page = bs(client.content, 'html.parser')
#lis=page.findAll ("div","top-story")[0].findAll('a')
lis=page.findAll ("div","top-story")[0].findAll('li')
newsstring=""
for i in range(len(lis)):
    newsstring=newsstring+" \n"+str(i+1)+"."+" "+str(lis[i].find('a').text+".")
    print(str(i+1)+"."+" "+str(lis[i].find('a').text)+".")
tts=gTTS(text=newsstring,lang='hi')
tts.save("test2.mp3")
mixer.init()
mixer.music.load('test2.mp3')
mixer.music.play()
