# -*- encoding: utf-8 -*-
"""
File auto_detect.py
Created on 2024/2/19 0:02
Copyright (c) 2024/2/19
@author:
"""
# -- coding:UTF-8 --
#查看Scripts文件夹路径
# import sys
# import os
# python_path=sys.executable
# scripts_path= os.path.join(os.path.dirname(python_path),"Scripts")
#python -m pip install selenium 需要安装，否则会报错 Driver for chrome was not found.
#pip install lxml 需要安装，否则会报错
# print(scripts_path)
import selenium
import os
from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup
from splinter import Browser
import smtplib
import ssl
from email.mime.text import MIMEText
from loguru import logger
from datetime import datetime
# from selenium.webdriver.chrome.service import Service

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
        # chrome浏览器的驱动器exe地址(需要修改为你自己的地址）
        # self.driver_path = "chromedriver.exe"
        # self.driver_path = os.path.abspath("chromedriver.exe")
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
                logger.info("-" * 50 + f"第{iter}次迭代" + "-" * 50)
                time_remaining = self.interval - time.time() % self.interval

                logger.info(f"休眠停止时间：{datetime.fromtimestamp(time.time() + time_remaining).strftime('%Y:%m:%d')} ({time_remaining}s)...")
                time.sleep(time_remaining)
                current_status = self.refresh_status(current_status, iter)
                logger.info("-" * 50 + f"第{iter}次迭代" + "-" * 50)
                iter += 1
            except Exception as e:
                logger.error("未知的Error"+f"发生错误: {e}")


    def refresh_status(self, status, iter):
        previous_manuscript_status = status

        logger.info('之前的投稿状态为: ' + previous_manuscript_status)
        time.sleep(self.wait_delay)
        # chrome_driver_path = "E://chromedriver-win64//chromedriver.exe"
        # chrome_driver_path = os.path.abspath("chromedriver.exe")

        # b = Browser('chrome', headless=True, executable_path=self.driver_path)
        # service = Service(self.driver_path)
        # b = Browser('chrome', headless=True, service=service)

        b = Browser('chrome')
        # b = Browser('chrome', headless = True, executable_path = chrome_driver_path)
        # time.sleep(self.wait_delay)
        logger.info("访问网站...")
        b.visit(f'https://mc.manuscriptcentral.com/{trans_type}')  # 此处设置scholar one对应期刊的网址
        # b.visit(f'https://mc.manuscriptcentral.com/{self.trans_type}')  # 此处设置scholar one对应期刊的网址
        time.sleep(self.wait_delay)
        logger.info("输入账号、密码...")
        b.fill('USERID', username)  # 此处设置你的scholar one账号邮箱
        time.sleep(self.wait_delay)
        b.fill('PASSWORD', pwd)  # 此处设置你的scholar one账号密码
        # time.sleep(self.wait_delay)
        logger.info("点击登录按钮...")
        # # 定位登录按钮元素
        # login_button = b.find_by_id('logInButton')
        # login_button.send_keys(Keys.ENTER)
        time.sleep(self.wait_delay)
        #处理显示的cookie界面
        if b.find_by_id("onetrust-accept-btn-handler").first.visible==True:
            b.find_by_id("onetrust-accept-btn-handler").click()
            b.find_by_css('#logInButton').click()
        else:
            b.find_by_css('#logInButton').click()
        # # 使用JavaScript执行点击操作
        # b.execute_script("arguments[0].click();", login_button)
        # b.find_by_id('logInButton').click()
        time.sleep(self.wait_delay)
        logger.info("点击Author界面...")
        # b.click_link_by_href("javascript:setDataAndNextPage('XIK_CUR_ROLE_ID','xik_2xXquy1Zk5i2mYWPBYAnU2UAZAPcChffdzgRzQoDWbME','AUTHOR_VIEW_MANUSCRIPTS')")
        b.links.find_by_partial_href('AUTHOR').click()
        # b.click_link_by_partial_href('AUTHOR_VIEW_MANUSCRIPTS')
        time.sleep(self.wait_delay)
        html_obj = b.html
        soup = BeautifulSoup(html_obj, "lxml")
        # # 状态显示位置的元素
        # table = soup.find("span", attrs={"class": "pagecontents"})
        # current_manuscript_status = table.string
        # logger.info(f"当前的投稿状态为:{table.string}")
        # # 写入文件
        # with open(self.save_file, "a") as f:
        #     content = f"{datetime.now().strftime('%Y-%m-%d %H:%M')},{iter},{table.string}\n"
        #     f.write(content)
        # time.sleep(self.wait_delay)
        # b.quit()
        # if current_manuscript_status == previous_manuscript_status:
        #     logger.info('您的投稿状态没有改变 ...')
        # else:
        #     logger.info("投稿状态已改变，将发邮件通知您 ...")
        #     message = f'投稿状态已改变: \n{current_manuscript_status}\n 查看网址：https://mc.manuscriptcentral.com/{self.trans_type}/'
        #     subject = f'{trans_type}: 投稿状态'
        #     self.email_con.send(message, subject)
        #     previous_manuscript_status = current_manuscript_status
        #
        # return current_manuscript_status

        # 状态显示位置的元素
        table = soup.find("span", attrs={"class": "pagecontents"})
        current_manuscript_status = table.string
        logger.info(f"当前的投稿状态为:{table.string}")
        # 使用CSS选择器定位元素
        ae_assignment_element = soup.select_one("#queue_0 > td:nth-child(1) > nobr")

        # 提取元素的文本内容
        if ae_assignment_element:
            current_ae_assignment = ae_assignment_element.get_text(strip=True)  # strip=True会去除两端的空白字符
            logger.info(f"当前的AE分配状态为: {current_ae_assignment}")
        else:
            logger.warning("未找到AE分配状态字段")
            current_ae_assignment = "未知"
        # 写入文件，包含投稿状态和AE分配状态
        with open(self.save_file, "a") as f:
            content = f"{datetime.now().strftime('%Y-%m-%d %H:%M')},{iter},{current_manuscript_status},{current_ae_assignment}\n"
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

        if current_ae_assignment != "AE: Not Assigned" and current_ae_assignment != "Unknown" and current_ae_assignment != "None":
            logger.info("AE分配状态已更新，将发邮件通知您 ...")
            ae_message = f'AE分配状态已更新: \n{current_ae_assignment}\n 查看网址：https://mc.manuscriptcentral.com/{self.trans_type}/'
            ae_subject = f'{self.trans_type}: AE分配状态更新'
            self.email_con.send(ae_message, ae_subject)

        return current_manuscript_status

if __name__ == "__main__":
    # 邮箱授权码 POP3/SMTP服务
    auth_key = "CTADGSOKWBQGVBXV"
    # 发送者的邮箱
    sender_email = "kirinmin@163.com"
    # 接收者的邮箱
    receiver_email = ["kirinmin@hotmail.com"]
    email_con = EmailSend(sender_email, receiver_email, auth_key)
    # trans_type = "tcsvt"
    trans_type = "tnsm"
    username = "kirinmin"
    pwd = ""
    # 此处设置间隔时间
    interval = 10
    listener = ScholarOneManuscriptListener(email_con, trans_type, username, pwd, 2, interval)
    listener.run()

    # test()


