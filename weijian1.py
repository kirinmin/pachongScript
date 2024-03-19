import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument('--headless')
dirver = webdriver.Chrome(service=Service(r'C:\Users\AM\Downloads\chromedriver.exe'))

my_headers= [
    {"User-Agent":"User-Agent=Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
    {"User-Agent":"User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
]
dirver.get("http://125.74.55.238:8005/blmpms/#/homePage/index/")
# dirver.get('https://www.baidu.com/')
# dirver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# dictCookies = dirver.get_cookies()  #获得所有cookie信息(返回是字典)
# print(dictCookies)
# print(type(dictCookies))
# jsonCookies = json.dumps(dictCookies)  #dumps是将dict转化成str格式
# print(jsonCookies)
# print(type(jsonCookies))
# # 登录完成后,将cookies保存到本地文件
# with open("cookies.json", "w") as fp:
#     fp.write(jsonCookies)
# for cookie in listCookies:
dirver.add_cookie({
    'domain': '125.74.55.238',
    'name': 'username',
    'value': '18294888589',
    'path': '/blmpms',
    # 'expires': None
})
dirver.add_cookie({
    'domain': '125.74.55.238',
    'name': 'password',
    'value': 'OohUTL2xyUbwZ6QweEfWtg==',
    'path': '/blmpms',
    # 'expires': None
})
dirver.add_cookie({
    'domain': '125.74.55.238',
    'name': 'isRememberPass',
    'value': 'true',
    'path': '/blmpms',
    # 'expires': None
})
time.sleep(3)
dirver.get("http://125.74.55.238:8005/blmpms/#/homePage/index/")
