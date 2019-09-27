import requests

while True:
    cityname = input('你想查询哪个城市的天气？\n')
    if cityname:
        try:        
            url = ('http://wthrcdn.etouch.cn/weather_mini?city=%s'%cityname)
            req = requests.get(url)
            req.encoding = 'utf8'
            #print(req.text)
            #print(type(req.text))
            data = req.json()
            print(data)
            #print(type(data))

            result = data['data']
            print(result)
            forecast = result['forecast'][0]
            print(forecast.get('date'))
            print(forecast.get('high'))
            print(forecast.get('low'))
            print(forecast.get('fengli'))
            print(forecast.get('fengxiang'))
            print(forecast.get('type'))
        except:
            print('查询失败')
    else:
        print('未找到该城市')
            

    


