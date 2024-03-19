from selenium import webdriver
import time
import pickle
import random
import pyautogui
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 主函数
def main():
    # 创建两个线程，一个用于点赞，一个用于发送消息
    thread1 = threading.Thread(target=like_and_comment, name="LikeAndComment")
    # thread2 = threading.Thread(target=keyword_detection, name="KeywordDetection")

    # 启动线程
    thread1.start()
    # thread2.start()

# 点赞和发送消息的函数
def like_and_comment():
    # 进入直播间后点赞300次
    # for i in range(20):
    #     x = random.randrange(500, 550)
    #     y = random.randrange(500, 550)
    #     pyautogui.click(x, y)
    #     time.sleep(0.2)

    # 随机选择发送的消息
    messages = [
        # "回关回关回关回关回关回关回关回关[色][色][色]",
        # "求关注求关注求关注[比心][舔屏]",
        # "回关回关回关回关回关回关回关回关回关回关回关回关[666][666][666][666]",
        # "回关回关回关回关回关[candy][candy][candy]",
        # "互关互关，家人们互相关注啦[呲牙]"

        # "大家戳戳屏幕点点关注，点点赞，主播需要你们的支持哦",
        "大家戳戳屏幕点点关注，点点赞，小师妹需要你们的支持哦",
        #         "亮一个抖币可以加群哦，群里面有高清手稿分享",
        #         "主播现在写的字是形楷，喜欢的可以加群跟着练哦",
                "来吧，大家把赞点起来！",
        "听说现在点赞关注的有机会吃到小师妹的口水哦"
    ]

    for j in range(1000):
        # wait_time = random.randrange(2, 3)
        wait_time = 2
        time.sleep(wait_time)
        while True:
            text_element = br.find_element(By.XPATH, '//textarea[@class="webcast-chatroom___textarea"]')
            text_element.clear()
            text_element.send_keys(random.choice(messages))
            time.sleep(0.5)
            # send_element = br.find_element(By.XPATH, '//button[@class="webcast-chatroom___send-btn"][@type="button"]')
            # time.sleep(1)
            # send_element.click()
            fayan_box = br.find_element(By.CSS_SELECTOR, '#chat-textarea')
            fayan_box.send_keys(Keys.ENTER)
            break

# 关键字检测和回复的函数
def keyword_detection():
    # 监测公屏的最后一个发言，根据关键字发送回复消息
    keywords_and_responses = {
        "笔": "9390",
        "纸": "80g木浆纸",
        "垫": "主播使用的垫子在橱窗有哦"
    }

    while True:
        web_text = br.find_elements(By.XPATH, '//*[@id="chat-textarea"]')
        latest_message = web_text[-1].text if web_text else ""

        for keyword, response in keywords_and_responses.items():
            if keyword in latest_message:
                while True:
                    text_element = br.find_element(By.XPATH, '//textarea[@class="webcast-chatroom___textarea"]')
                    text_element.clear()
                    text_element.send_keys(response)
                    time.sleep(0.5)
                    # fayan_box = br.find_element(By.CSS_SELECTOR, '#chat-textarea')
                    #
                    # fayan_box.send_keys(Keys.ENTER)

                    send_element = br.find_element(By.XPATH, '//button[@class="webcast-chatroom___send-btn"][@type="button"]')
                    time.sleep(1)
                    send_element.click()
                    break

if __name__ == '__main__':
    # 加载之前保存的Cookie
    with open("douyin_cookie.pickle", 'rb') as file:
        cookies_list = pickle.load(file)

    # # 创建Edge浏览器实例
    # edge = webdriver.Edge()
    # edge.maximize_wi9017ndow()
    br=webdriver.Chrome()
    br.maximize_window()
    # 打开抖音网站
    # edge.get('https://www.douyin.com/')
    br.get('https://www.douyin.com/')

    # 添加Cookie以实现持久登录
    for cookie in cookies_list:
        br.add_cookie(cookie)

    # 自定义您要进入的直播间链接
    # br.get('https://live.douyin.com/60040407039')
    # br.get('https://live.douyin.com/939660187691')
    # br.get('https://live.douyin.com/30874620324')
    # br.get('https://live.douyin.com/304051872962')
    # br.get('https://live.douyin.com/huwaifa168')
    br.get('https://live.douyin.com/93173086668')#神隐小师妹
    # br.get('https://live.douyin.com/41498419462')

    # 等待一段时间，确保页面加载完毕
    time.sleep(35)

    # 启动主程序
    main()