# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get('http://www.weather.com.cn/textFC/hb.shtml', headers=headers)
#r = requests.get('', headers=headers)
r.encoding = "utf-8"
content = r.text
#print(content)
soup = BeautifulSoup(content, 'lxml')
# print(r.content)
# print(r.text)
divs = soup.find_all(class_ = 'w_city city_guonei')
divs_ = soup.find_all(class_ = 'last')
# print(divs)
for d in divs:
    for d1 in divs_:
        lis1 = d1.select('a')
        lis = d.select('a')
        for li in lis:
            for li1 in lis1:

                # print(li['href'],'---',li.text)
                #根据li['href']在抓取里面的信息
                href = li1['href']
                # print(li.text,href.split('#')[0])
                re = requests.get(href.split('#')[0], headers=headers)
                re.encoding = "utf-8"
                c = re.text
                s = BeautifulSoup(c, 'lxml')
                #print(li.text)
                # print("-----------------------------------------------")
                # print(s)
                # print("-----------------------------------------------")
                divs1 = s.find_all('li','sky skyid lv1')
                divs2 = s.find_all('li','sky skyid lv2')
                divs3 = s.find_all('li', 'sky skyid lv3')
                divs4 = s.find_all('li', 'sky skyid lv4')
                divs5 = s.find_all('li', 'sky skyid lv5')
                divs6 = s.find_all('li', 'sky skyid lv6')
                divs7 = s.find_all('li', 'sky skyid lv7')
                divs1_h1 = s.find_all(class_ = 'tem')
                divs1_wea = s.find_all(class_ = 'wea')
                divs1_win = s.find_all(class_ = 'win')
                if divs1 != '':
                    print('城市：',li.text,'温度'+divs1_h1[0].text,'天气：'+divs1_wea[0].text,'风力：'+divs1_win[0].i.text)
                if divs2 != '':
                    print('城市：',li.text,'温度'+divs1_h1[1].text,'天气：'+divs1_wea[1].text,'风力：'+divs1_win[1].i.text)
                if divs3 != '':
                    print('城市：', li.text, '温度'+divs1_h1[2].text, '天气：'+divs1_wea[2].text, '风力：'+divs1_win[2].i.text)
                if divs4 != '':
                    print('城市：', li.text, '温度'+divs1_h1[3].text, '天气：'+divs1_wea[3].text, '风力：'+divs1_win[3].i.text)
                if divs5 != '':
                    print('城市：', li.text, '温度'+divs1_h1[4].text, '天气：'+divs1_wea[4].text, '风力：'+divs1_win[4].i.text)
                if divs6 != '':
                    print('城市：', li.text, '温度'+divs1_h1[5].text, '天气：'+divs1_wea[5].text, '风力：'+divs1_win[5].i.text)
                if divs7 != '':
                    print('城市：', li.text, '温度'+divs1_h1[6].text, '天气：'+divs1_wea[6].text, '风力：'+divs1_win[6].i.text)
