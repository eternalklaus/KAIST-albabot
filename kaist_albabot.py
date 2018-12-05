# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import telegram

def diffing(filename, resdic2):
	f = open(filename,'r')
	l = ['','']
	resdic1 = {}
	resdic3 = {}
	# 로그파일을 파싱해서 resdic1을 만든다. 
	while True:
		line = f.readline()
		if not line: break
		if ', ' not in line: break
		l[0] = line[:line.index(', ')]
		l[1] = line[line.index(', ')+2:-1]
		resdic1[l[0]] = l[1]

	for key2 in resdic2.keys():
		if key2 not in resdic1.keys():
			resdic3[key2] = resdic2[key2]
	return resdic3

def sanitize(resdic):
	resdic2 = {}
	resdic3 = {}
	blacklist = ['마감', '판매', '삽니다', '팝니다', '홍보', '원총']
	whitelist = ['아르바이트', '알바', '참가자', '구인', '모집', '실험 참가' ]
	appendit = 0
	removeit = 0
	# 화이트리스트 추가
	for key in resdic.keys():
		for w in whitelist:
			if w in resdic[key]:
				appendit = 1
				break

		if appendit == 1:
			appendit = 0
			resdic2[key] = resdic[key]

	# 블랙리스트 제거
	for key in resdic2.keys():
		removeit = 0
		for w in blacklist:
			if w in resdic2[key]:
				removeit = 1
				break
		if removeit == 0:
			resdic3[key] = resdic2[key]
	
	return resdic3


def logfile(resdic, filename):
	f = open(filename, 'w')
	for key in resdic.keys():
		f.write(key + ', ' + resdic[key] + '\n') # 파일로 저장
	f.close()


def parsehtml(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.content, 'html.parser')
	
	# 데이터 검색 
	articlenames = soup.find_all('td',{'class':'title'}) # <td class="title"></td>
	articlenums = soup.find_all('td',{'class': 'articleid hidden'}) # <td class="articleid hidden"></td>
	
	for i in range(0,len(articlenames)):
		articlenames[i] = articlenames[i].next_element
		articlenames[i] = articlenames[i].strip()

	for i in range(0,len(articlenums)):
		articlenums[i] = articlenums[i].next_element
		articlenums[i] = articlenums[i].strip()

	resdic = {}
	for i in range(0,len(articlenames)):
		resdic[articlenums[i]] = articlenames[i]

	return resdic

def sendMsg(key, resdic):
	my_token = '' # kaist_albabot's API tocken
	bot = telegram.Bot(token = my_token)   # bot 선언.
	updates = bot.getUpdates()  # 업데이트

	chat_id = bot.getUpdates()[-1].message.chat.id

	theText  = ''
	theText += '새로운 알바소식 도착 ◕‿◕' + '\n\n'
	theText += resdic[key] + '\n'
	theText += 'https://ara.kaist.ac.kr/all/' + str(key)
	bot.sendMessage(chat_id = chat_id, text=theText)


if __name__=='__main__':
	url = 'https://ara.kaist.ac.kr/all/'
	log = '/home/osboxes/Desktop/kaist_albabot/log'
	resdic = parsehtml(url)
	resdic = sanitize(resdic)
	print('-----------------')

	resdic3 = diffing(log, resdic)

	# 다 하고나서는 이제 지금읽은값을 로그만들기
	for key in resdic3.keys():
		sendMsg(key, resdic3)

	logfile(resdic, log)
