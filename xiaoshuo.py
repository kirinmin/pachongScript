from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def simulate_login(driver, login_url, login_payload):
    # 打开登录页
    driver.get(login_url)

    # 等待登录按钮可点击
    # login_button = WebDriverWait(driver, 0.5).until(
    #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[1]/a[1]'))
    # )
    login_button=driver.find_element(By.CSS_SELECTOR, '#root > div.navigation_box > div > div.user > div.nav_icons > a:nth-child(1)')
    # 点击登录按钮
    login_button.click()

    # 输入邮箱和密码
    email_input = driver.find_element(By.NAME, 'email')  # 请替换为实际的邮箱输入框的name属性值
    password_input = driver.find_element(By.NAME, 'password')  # 请替换为实际的密码输入框的name属性值

    email_input.send_keys(login_payload['email'])
    password_input.send_keys(login_payload['password'])

    # 点击登录按钮
    login_button_final = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[1]/a[1]')  # 请替换为实际的登录按钮的XPath
    login_button_final.click()

    # 可以添加等待登录成功的逻辑，例如等待某个页面元素出现

    print('登录成功')



def get_novel_chapters(driver, novel_url):
    # 打开小说章节页面
    driver.get(novel_url)

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'volume')))

    # 示例：获取小说章节
    chapter_links = driver.find_elements(By.CSS_SELECTOR, '.volume a.chapter')

    all_chapters = []
    for chapter_link in chapter_links:
        chapter_url = chapter_link.get_attribute('href')
        chapter_title = chapter_link.find_element(By.CLASS_NAME, 'title').text.strip()
        all_chapters.append((chapter_title, chapter_url))

    # 保存章节信息到txt文件
    with open('novel_chapters.txt', 'w', encoding='utf-8') as file:
        for chapter_title, chapter_url in all_chapters:
            file.write(f'{chapter_title}\n{chapter_url}\n\n')

    print(f'已保存{len(all_chapters)}章节到 novel_chapters.txt 文件中.')

if __name__ == '__main__':
    os.environ['NO_PROXY'] = 'www.uaa003.com'

    # 登录信息
    login_url = 'https://www.uaa003.com/login'
    login_payload = {
        'email': 'kirinanmin@foxmail.com',  # 替换为你的邮箱
        'password': '12345678'  # 替换为你的密码
    }

    # 使用Chrome浏览器，你也可以选择其他浏览器
    driver = webdriver.Chrome()

    try:
        # 登录
        simulate_login(driver, login_url, login_payload)

        # 获取小说章节
        novel_url = 'https://www.uaa003.com/novel/intro?id=11306906'
        get_novel_chapters(driver, novel_url)
    finally:
        # 关闭浏览器
        driver.quit()
