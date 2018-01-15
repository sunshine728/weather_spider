import  requests
from bs4  import BeautifulSoup

#第一步：爬到所有华东城市的URL并输出到控制台
url1 = 'http://www.weather.com.cn/textFC/hb.shtml'
r = requests.get(url1)
#设置编码方式
r.encoding ='utf-8'
bs41 = BeautifulSoup(r.text,'html.parser')
all_city_href = bs41.find_all(class_ = 'conMidtab2')
list_set = {}
for city_href in all_city_href:
    children = city_href.children
    city_td = '<td width="83" height="23">'
    for child in children:
         for child_dtl_a in child.findAllNext('a'):
             # for child_dtl_a in child_dtl.findAllNext('a'):
                 # print(child_dtl_a)
                 # print(dir(child_dtl_a))
                 child_dtl_a_item = child_dtl_a.attrs
                 for item in child_dtl_a_item:
                    # print("--------",item)
                     if item == 'href' :
                         child_Dtl_a_text = child_dtl_a.text
                         s = child_dtl_a['href']+""
                         if s.find("http://www.weather.com.cn/weather/") != -1:
                             list_set.update({child_Dtl_a_text:child_dtl_a['href']})

list_set.pop('详情')
print(list_set)
#print(child_Dtl_a_text,child_dtl_a['href'])
#第二步：根据所有城市对应的详情的href爬到该城市一周的温度并输出到控制台
for list_set_one in list_set:
    print(list_set_one)
    re = requests.get(list_set.get(list_set_one))
    re.encoding = "utf-8"
    c = re.text
    s = BeautifulSoup(c, 'lxml')
    divs1 = s.find_all('li', 'sky skyid lv1')
    divs2 = s.find_all('li', 'sky skyid lv2')
    divs3 = s.find_all('li', 'sky skyid lv3')
    divs4 = s.find_all('li', 'sky skyid lv4')
    divs5 = s.find_all('li', 'sky skyid lv5')
    divs6 = s.find_all('li', 'sky skyid lv6')
    divs7 = s.find_all('li', 'sky skyid lv7')
    # print(dir(divs1))
    divs1_h1 = s.find_all(class_='tem')
    divs1_wea = s.find_all(class_='wea')
    divs1_win = s.find_all(class_='win')
    if divs1 != '':
        print('城市：', list_set_one,'温度' + divs1_h1[0].text, '天气：' + divs1_wea[0].text, '风力：' + divs1_win[0].i.text)
    if divs2 != '':
        print('城市：', list_set_one, '温度' + divs1_h1[1].text, '天气：' + divs1_wea[1].text, '风力：' + divs1_win[1].i.text)
    if divs3 != '':
        print('城市：', list_set_one, '温度' + divs1_h1[2].text, '天气：' + divs1_wea[2].text, '风力：' + divs1_win[2].i.text)
    if divs4 != '':
        print('城市：', list_set_one, '温度' + divs1_h1[3].text, '天气：' + divs1_wea[3].text, '风力：' + divs1_win[3].i.text)
    if divs5 != '':
        print('城市：', list_set_one, '温度' + divs1_h1[4].text, '天气：' + divs1_wea[4].text, '风力：' + divs1_win[4].i.text)
    if divs6 != '':
        print('城市：', list_set_one, '温度' + divs1_h1[5].text, '天气：' + divs1_wea[5].text, '风力：' + divs1_win[5].i.text)
    if divs7 != '':
        print('城市：', list_set_one, '温度' + divs1_h1[6].text, '天气：' + divs1_wea[6].text, '风力：' + divs1_win[6].i.text)
