import time
from bs4 import BeautifulSoup
from splinter import Browser
import smtplib
import ssl
from email.mime.text import MIMEText
from loguru import logger
from datetime import datetime
# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

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
    def __init__(self, email_con, trans_type, username, pwd, delay_time, interval):
        self.email_con = email_con
        self.trans_type = trans_type
        self.username = username
        self.pwd = pwd
        self.interval = interval
        self.wait_delay = delay_time
        self.save_file = "log.txt"
        self.session = None

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
            # try:
                logger.info("-" * 50 + f"第{iter}次迭代" + "-" * 50)
                time_remaining = self.interval - time.time() % self.interval
                logger.info(f"休眠停止时间：{datetime.fromtimestamp(time.time() + time_remaining).strftime('%Y:%m:%d')} ({time_remaining}s)...")
                time.sleep(time_remaining)
                current_status = self.refresh_status(current_status, iter)
                logger.info("-" * 50 + f"第{iter}次迭代" + "-" * 50)
                iter += 1
            # except Exception as e:
                # logger.error("未知的Error" + f"发生错误: {e}")

    def login(self,timeout):
        # self.session = Browser('chrome', headless=True)
        self.timeout = timeout
        start_time = time.time()
        self.session = Browser('chrome', headless=True)
        logger.info("访问网站...")
        self.session.visit(f'https://mc.manuscriptcentral.com/{self.trans_type}')
        if time.time() - start_time > self.timeout:
            logger.error(f"访问超时，重新访问页面: {time.time() - start_time}")
            start_time = time.time()
            self.session.visit(f'https://mc.manuscriptcentral.com/{self.trans_type}')
        time.sleep(self.wait_delay)
        logger.info("输入账号、密码...")
        self.session.fill('USERID', self.username)
        time.sleep(self.wait_delay)
        time.sleep(self.wait_delay)
        self.session.fill('PASSWORD', self.pwd)
        time.sleep(self.wait_delay)
        logger.info("点击登录按钮...")
        if self.session.find_by_id("onetrust-accept-btn-handler").first.visible==True:
            self.session.find_by_id("onetrust-accept-btn-handler").click()
            self.session.find_by_css('#logInButton').click()
        else:
            self.session.find_by_css('#logInButton').click()
        logger.info("点击Author界面...")
        self.session.links.find_by_partial_href('AUTHOR').click()
        # self.session.find_by_css('#logInButton').click()
        # time.sleep(self.wait_delay)

    def refresh_status(self, status, iter):
        previous_manuscript_status = status
        logger.info('之前的投稿状态为: ' + previous_manuscript_status)
        time.sleep(self.wait_delay)
        if not self.session:
            self.login(6)

        # self.session.visit(f'https://mc.manuscriptcentral.com/{self.trans_type}/author')
        time.sleep(self.wait_delay)
        html_obj = self.session.html
        soup = BeautifulSoup(html_obj, "lxml")
        table = soup.find("span", attrs={"class": "pagecontents"})
        current_manuscript_status = table.string
        logger.info(f"当前的投稿状态为:{table.string}")

        ae_assignment_element = soup.select_one("#queue_0 > td:nth-child(1) > nobr")
        if ae_assignment_element:
            current_ae_assignment = ae_assignment_element.get_text(strip=True)
            logger.info(f"当前的AE分配状态为: {current_ae_assignment}")
        else:
            logger.warning("未找到AE分配状态字段")
            current_ae_assignment = "未知"

        with open(self.save_file, "a") as f:
            content = f"{datetime.now().strftime('%Y-%m-%d %H:%M')},{iter},{current_manuscript_status},{current_ae_assignment}\n"
            f.write(content)
        time.sleep(self.wait_delay)
        # self.session.quit()

        if current_manuscript_status != previous_manuscript_status:
            logger.info("投稿状态已改变，将发邮件通知您 ...")
            message = f'投稿状态已改变: \n{current_manuscript_status}\n 查看网址：https://mc.manuscriptcentral.com/{self.trans_type}/'
            subject = f'{self.trans_type}: 投稿状态'
            self.email_con.send(message, subject)
            previous_manuscript_status = current_manuscript_status

        if current_ae_assignment != "AE: Not Assigned" and current_ae_assignment != "Unknown" and current_ae_assignment != "None":
            logger.info("AE分配状态已更新，将发邮件通知您 ...")
            ae_message = f'AE分配状态已更新: \n{current_ae_assignment}\n 查看网址：https://mc.manuscriptcentral.com/{self.trans_type}/'
            ae_subject = f'{self.trans_type}: AE分配状态更新'
            self.email_con.send(ae_message, ae_subject)

        return current_manuscript_status


if __name__ == "__main__":
    auth_key = "CTADGSOKWBQGVBXV"
    sender_email = "kirinmin@163.com"
    receiver_email = ["kirinmin@hotmail.com"]
    email_con = EmailSend(sender_email, receiver_email, auth_key)
    trans_type = "tnsm"
    username = "kirinmin"
    pwd = ""
    interval = 10
    listener = ScholarOneManuscriptListener(email_con, trans_type, username, pwd, 2, interval)
    listener.run()
