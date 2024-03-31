@[TOC](自动检测IEEE Manuscript网站论文状态)
# 自动检测IEEE Manuscript网站论文状态
## 前言
众所周知，IEEE的期刊审核是十分慢的，而每天去官网看投稿状态的变化是一件极其分神的事情，因此使用脚本来自动检测投稿状态的变化是十分有必要的。
## 准备工作Preparation  
只需简单的几个步骤，即可让你省去查看投稿状态的时间，能够使用的前提为：
- 你需要有两个邮箱，一个用于发送邮件（最好是163邮箱），一个用于接收邮箱

具体步骤为： 
- 开启用于发送邮件的邮箱的POP3/SMTP服务
    服务的开启见此链接：[python自动发送邮件](https://blog.csdn.net/c1007857613/article/details/129751652)
- 获得获取对应邮箱的SMTP授权码，填入代码中的```auth_key```
- ```sender_email```填发送邮件的邮箱地址，```receiver_email```填接收邮件的邮箱地址
- 根据自己的需要修改```trans_type```，注意，需要先看官网的网址，如：

    若网址为https://mc.manuscriptcentral.com/tpami-cs，则```trans_type="tpami-cs"```，而不是```tpami```。
- 最后运行即可，如果有服务器的话，可以挂在服务器上后台运行。

发邮件的部分所给的链接中给的是qq的，我来演示一下网易的。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/cddfe3ae1d734a73b5119a77817c2a50.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/3ba6852ddc3946cd986602c65dc2b142.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/bc8434c81795405fa1637d98de91e80a.png)

## 步骤Steps 
### 获得投稿状态
该部分使用了**splinter库**，它是一个用于自动化浏览器行为的 Python 库，用于模拟和控制浏览器的行为。
使用它的一个原因是它可以在无头（headless）模式下运行浏览器，即在没有图形用户界面的情况下执行操作，这对于后台运行是十分有用的。
该部分的整体流程为：
（1）登录
（2）点击界面的Author按钮，得到投稿信息界面的内容
（3）找到界面里面显示投稿状态的元素，获取内容
代码为：

```bash
b = Browser('chrome', headless=True, executable_path=driver_path)
b.visit(f'https://mc.manuscriptcentral.com/{trans_type}')  # 此处设置scholar one对应期刊的网址
b.fill('USERID', username)  # 此处设置你的scholar one账号邮箱
b.fill('PASSWORD', pwd)  # 此处设置你的scholar one账号密码
b.find_by_id('logInButton').click()
b.links.find_by_partial_href('AUTHOR').click()
html_obj = b.html
soup = BeautifulSoup(html_obj, "lxml")
# 状态显示位置的元素
table = soup.find("span", attrs={"class": "pagecontents"})
current_manuscript_status = table.string
logger.info(f"当前的投稿状态为:{table.string}")
```
### 发送邮件
当检测到投稿状态发生改变后，就会发送邮件通知，这部分使用了python的smtp库，它通过SMTP协议发送电子邮件。
该部分的代码为：

```bash
if current_manuscript_status == previous_manuscript_status:
   logger.info('您的投稿状态没有改变 ...')
else:
   logger.info("投稿状态已改变，将发邮件通知您 ...")
   message = f'投稿状态已改变: \n{current_manuscript_status}\n 查看网址：https://mc.manuscriptcentral.com/{trans_type}/'
   subject = f'{trans_type}: 投稿状态'
   self.email_con.send(message, subject)
   previous_manuscript_status = current_manuscript_status
# 端口号:465(163邮箱)
port = 465
sender = "发送的邮箱"
receiver = "接收的邮箱"
auth_key = "授权码"
host = "smtp.163.com"
context= ssl.create_default_context()
# 正文
msg = MIMEText(content, 'plain','utf-8')
# 邮件主题
msg['Subject'] = subject  # 邮件主题
msg['From'] = sender
msg['To'] = ",".join(receiver)
try:
   logger.info("开始发送邮件...")
   smtp = smtplib.SMTP_SSL(host,port,context=context)  # 建立和SMTP邮件服务器的连接
   logger.info("连接服务器完成")
   smtp.login(self.sender, auth_key)
   logger.info("登录成功")
   smtp.sendmail(self.sender,receiver,msg.as_string())
   smtp.quit()
   logger.info("邮件发送完成!")
except:
   logger.error("Error: 无法发送邮件")```
```
### 收到通知邮件
如果投稿状态发生改变，会发送邮件通知，如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e47207a2b10e4c4288b92d15235bc6dc.png)
在运行代码之前，需要确保脚本文件同级目录下有一个log.txt文件，否则会报错，该文件内容为
2024-02-25 20:20,0,Under Review
其意义为日期，迭代次数，目前稿件状态
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e8d11ea16595461282f413d98dfd80bc.png)

## 遇到的问题
1 Splinter 安装
python -m pip install splinter
注意：需要确认是否安装selenium，否则会报错：

splinter.exceptions.DriverNotFoundError: Driver for firefox was not found.
python -m pip install selenium
### The chromedriver version cannot be discovered
没有找到浏览器驱动
解决办法：使用chrome_driver_path指定路径
from splinter import Browser
chrome_driver_path = "path"
b = Browser('chrome', headless=True, executable_path=chrome_driver_path)
同时需要注意
配置chromedriver地址到环境变量。或者把chromedriver.exe放到python下的Scripts文件夹下。
### element click intercepted: Element is not clickable at point
网速问题，页面还没加载出来

### 完整代码

```bash
import os
import time
from bs4 import BeautifulSoup
from splinter import Browser
import smtplib
import ssl
from email.mime.text import MIMEText
from loguru import logger
from datetime import datetime

class EmailSend():
    def __init__(self,sender,receiver,auth_key):
        self.sender = sender
        self.receiver = receiver
        self.auth_key = auth_key

    def send(self, content, subject):
        # 端口号:465 or 587
        port = 465
        ## qq邮箱不行,网易邮箱可以
        host = "smtp.163.com"
        context = ssl.create_default_context()
        # 正文
        msg = MIMEText(content, 'plain','utf-8')
        # 邮件主题
        msg['Subject'] = subject  # 邮件主题
        msg['From'] = self.sender
        msg['To'] = ",".join(self.receiver)
        try:
            logger.info("开始发送邮件...")
            smtp = smtplib.SMTP_SSL(host,port,context=context)  # 建立和SMTP邮件服务器的连接
            logger.info("连接服务器完成")
            smtp.login(self.sender, self.auth_key)
            logger.info("登录成功")
            smtp.sendmail(self.sender,self.receiver,msg.as_string())
            smtp.quit()
            logger.info("邮件发送完成!")
        except:
            logger.error("Error: 无法发送邮件")

class ScholarOneManuscriptListener:
    def __init__(self, email_con, trans_type, name, pwd, delay_time, interval):
        # chrome浏览器的驱动器exe地址
        self.driver_path = "chromedriver.exe"
        self.email_con = email_con
        self.trans_type = trans_type
        self.name = name
        self.pwd = pwd
        self.interval = interval
        self.wait_delay = delay_time
        self.save_file = "log.txt"

    def get_last_status(self):
        status = "NULL"
        iter = 0
        with open(self.save_file, "r") as f:
            content = f.readline()
            if content != "":
                _, iter, status = content.strip().split(",")
        return int(iter), status

    def run(self):
        logger.info("-" * 100)
        logger.info(f"发送请求的间隔时间：{self.interval}s")
        logger.info("-" * 100)
        iter, current_status = self.get_last_status()
        while True:
            try:
                logger.info("-" * 50 + f"第{iter}迭代" + "-" * 50)
                time_remaining = self.interval - time.time() % self.interval

                logger.info(f"休眠停止时间：{datetime.fromtimestamp(time.time() + time_remaining).strftime('%Y:%m:%d')} ({time_remaining}s)...")
                time.sleep(time_remaining)
                current_status = self.refresh_status(current_status, iter)
                logger.info("-" * 50 + f"第{iter}迭代" + "-" * 50)
                iter += 1
            except Exception:
                logger.error("未知的Error")

    def refresh_status(self, status, iter):
        previous_manuscript_status = status

        logger.info('之前的投稿状态为: ' + previous_manuscript_status)
        time.sleep(self.wait_delay)

        b = Browser('chrome', headless=True, executable_path=self.driver_path)
        time.sleep(self.wait_delay)
        logger.info("访问网站...")
        b.visit(f'https://mc.manuscriptcentral.com/{trans_type}')  # 此处设置scholar one对应期刊的网址
        time.sleep(self.wait_delay)
        logger.info("输入账号、密码...")
        b.fill('USERID', username)  # 此处设置你的scholar one账号邮箱
        time.sleep(self.wait_delay)
        b.fill('PASSWORD', pwd)  # 此处设置你的scholar one账号密码
        time.sleep(self.wait_delay)
        logger.info("点击登录按钮...")
        b.find_by_id('logInButton').click()
        time.sleep(self.wait_delay)
        logger.info("点击Author界面...")
        b.links.find_by_partial_href('AUTHOR').click()
        time.sleep(self.wait_delay)
        html_obj = b.html
        soup = BeautifulSoup(html_obj, "lxml")
        # 状态显示位置的元素
        table = soup.find("span", attrs={"class": "pagecontents"})
        current_manuscript_status = table.string
        logger.info(f"当前的投稿状态为:{table.string}")
        # 写入文件
        with open(self.save_file, "a") as f:
            content = f"{datetime.now().strftime('%Y-%m-%d %H:%M')},{iter},{table.string}\n"
            f.write(content)
        time.sleep(self.wait_delay)
        b.quit()
        if current_manuscript_status == previous_manuscript_status:
            logger.info('您的投稿状态没有改变 ...')
        else:
            logger.info("投稿状态已改变，将发邮件通知您 ...")
            message = f'投稿状态已改变: \n{current_manuscript_status}\n 查看网址：https://mc.manuscriptcentral.com/{self.trans_type}/'
            subject = f'{trans_type}: 投稿状态'
            self.email_con.send(message, subject)
            previous_manuscript_status = current_manuscript_status

        return current_manuscript_status

if __name__ == "__main__":
    # 邮箱授权码 POP3/SMTP服务
    auth_key = "你的邮箱key"
    # 发送者的邮箱
    sender_email = "@163.com"
    # 接收者的邮箱
    receiver_email = ["@qq.com"]
    email_con = EmailSend(sender_email, receiver_email, auth_key)
    trans_type = "tcsvt"
    username = "@163.com"
    pwd = "你的密码"
    # 此处设置间隔时间
    interval = 5
    listener = ScholarOneManuscriptListener(email_con, trans_type, username, pwd, 1, interval)
    listener.run()
```


