import requests
import re
import json
import numpy as np


def writeExample():
    """测试获取数据并写入本地"""
    url = 'https://sou.zhaopin.com/?jl=639&kw=Python&p=1'
    j = open("./pythonJob_1.1.json", 'w+', encoding='utf-8')
    try:
        data = getData(url)
        if data is not None:
            j.write(data)
        else:
            print('无数据')
    except Exception as e:
        print(e)
        print('异常')
        j.close()
    else:
        print('结束')
        j.close()


def getData(url: str) -> str:
    """处理请求的结果"""
    resp = requests.get(url)
    print(url)
    # 正则匹配获取到数据的json
    matchObj = re.search(r"(?<=__INITIAL_STATE__=).*(?=</script>)", resp.text)
    data = matchObj.group(0)
    if data is None:
        return f'地址{url}获取数据失败！'

    return data.replace("_INITIAL_STATE__=", "")


def getJonListByCity(cityCode: str):
    """传入城市code，获取这个城市的数据"""
    url = f'https://sou.zhaopin.com/?jl={cityCode}&kw=Python&p=1'
    print(f'获取城市{cityCode}的数据')
    return getData(url)


def getCityCode() -> list:
    data = getData('https://sou.zhaopin.com/?jl=538&kw=Python&p=1')
    data = json.loads(data)
    return data['baseData']['hotCity']


def getAllcityData():
    # 先获取城市code列表，根据列表获取每一个城市的数据，把获取到的数据写入
    cityList = getCityCode()
    f = open("./pythonJobAllCity.json", 'a', encoding='utf-8')
    try:
        for city in cityList:
            print(city['code'], city['name'])
            f.write(getJonListByCity(city['code']))
            f.write('\n')
    except Exception as e:
        print(f"异常:{e}")
        f.close()
    else:
        print("结束")
        f.close()


def writeTest():
    f = open("./pythonJobAllCity.json", 'a', encoding='utf-8')
    try:
        for city in np.random.randint(0, 10, size=10):
            f.write(str(city))
            f.write('\n')
    except Exception as e:
        print(f"异常:{e}")
        f.close()
    else:
        print("结束")
        f.close()


# print(getCityCode())
getAllcityData()
# writeExample()
