#coding:gbk
import urllib.request
import json
from city import city
cityname = input('你想查询哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html'%citycode)
        content = urllib.request.urlopen(url).read()
        #print(content)
        data = json.loads(content)
        print(data)
        #print(type(content))
        #print(type(data))
        result = data['weatherinfo']
        string = ('%s\n%s~%s')%(
            result['weather'],
            result['temp1'],
            result['temp2']
            )
        print(string)

    except:
        print('查询失败')
    
else:
    print('未找到该城市')
        
