import random
import re

from faker import Faker

fake = Faker(['zh_cn'])


def generateContent(maxLen=500):
    if type(maxLen) != int:
        maxLen = int(maxLen)
    if (maxLen < 100):
        maxLen += 100
    len = random.randint(100, maxLen)
    print(fake.text(len))
    print("=*" * 10)


def generateTitle(maxLen=150):
    if type(maxLen) != int:
        maxLen = int(maxLen)
    if maxLen > 150:
        maxLen = 150
    print(fake.text(random.randint(5, maxLen)))
    print("=*" * 10)


switchObj = {
    "content": generateContent,
    "title": generateTitle
}

if __name__ == '__main__':
    commend = input("输入类型：")
    if 'random' == commend:
        generateContent(random.randint(100, 500))
        generateTitle(random.randint(2, 100))
    else:
        commends = re.findall("\w+=\d+", commend)
        for c in commends:
            m = c.split("=")
            func = switchObj.get(m[0])
            if func is not None:
                func(m[1])
