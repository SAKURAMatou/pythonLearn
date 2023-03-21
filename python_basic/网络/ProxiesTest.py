import unittest
from urllib import request


class ProxiesTest(unittest.TestCase):
    def test_is_proxies(self):
        """判断当前系统是否使用网络代理"""
        proxies = request.getproxies()
        if proxies:
            print("当前系统正在使用代理")
            print(proxies)
        else:
            print("当前系统没有使用代理")
