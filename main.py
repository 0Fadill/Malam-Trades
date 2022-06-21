##name = input('What is your name?\n')
##print('Hi, %s.' % name)
import requests
import json
import priceget

names =["hololive","sora","roboco","miko","suisei","azki","mel","fubuki","matsuri","aki","haato","aqua","shion","ayame","choco","subaru","mio","okayu","korone","pekora","rushia","flare","noel","marine","kanata","coco","watame","towa","himemoriluna","lamy","nene","botan","polka","laplus","lui","koyori","chloe","iroha","calliope","kiara","inanis","gura","amelia","irys","sana","fauna","kronii","mumei","baelz","risu","moona","iofi","ollie","melfissa","reine","zeta","kovalskia","kanaeru","ui","nana","pochimaru","ayamy","nabi","nachoneko","rurudo","civia"]

#coin = "himemoriluna"
#name = coin

for name in names:
  priceget.get(name)