from selenium import webdriver
import time
import pickle
from selenium.webdriver.chrome.service import Service

driver_path = r'D:\software\python3.8\Scripts\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
# 创建Edge浏览器实例
br = webdriver.Chrome()

# 最大化浏览器窗口
br.maximize_window()

# 设置最大等待时长为10秒
br.implicitly_wait(10)

# 打开抖音网站
br.get('https://www.douyin.com/')

# 等待一段时间，以便手动登录
time.sleep(1)
input("登入抖音账号后，请输入任意键继续...")
time.sleep(0.3)

# 保存Cookie到文件
with open("douyin_cookie.pickle", 'wb') as file:
    pickle.dump(br.get_cookies(), file)

# 删除浏览器中的所有Cookie
br.delete_all_cookies()

# 关闭浏览器
br.quit()