import json
import threading
from datetime import datetime

import requests


class WriteData(threading.Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        """数据写入本地的json"""
        now = datetime.now()
        time_str = now.strftime('%Y-%m-%d_%H%M%S')
        filename = f"./hot_{time_str}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            for item in self.data:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')
        print('写入数据成功')


def main():
    """发送请求获取数据"""
    # 天行数据接口提供的网络API获取热搜数据，结果是list
    url = 'https://apis.tianapi.com/networkhot/index?key=15b19428ba2998e261dbac04ec0501ab&'
    # 设置代理信息
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
    response = requests.get(url=url, headers={'Content-Type': 'application/json'}, proxies=proxies)
    # 获取返回值的数据，json格式
    resData = response.json()
    if resData['code'] != 200:
        # 如果返回状态码是200，则表示请求成功
        print("请求失败，结果为：{}".format(resData))

    # 请求成功之后解析数据
    hot_list = resData['result']['list']
    # 通过新的写入数据线程写入数据
    WriteData(hot_list).start()


if __name__ == '__main__':
    main()
