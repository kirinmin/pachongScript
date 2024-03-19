import requests
from bs4 import BeautifulSoup
import os


def simulate_login(session, login_url, login_payload):

    # 获取登录页的HTML内容
    login_page_response = session.get(login_url)
    login_page_html = login_page_response.text

    # 使用BeautifulSoup解析HTML，找到登录表单的相关信息
    soup = BeautifulSoup(login_page_html, 'html.parser')

    # 提取登录表单中的重要信息，如_csrf、referer等
    csrf_token = soup.find('input', {'name': '_csrf'})['value']
    referer = login_url  # 登录时的referer一般为登录页URL

    # 找到登录按钮的URL
    login_action = soup.find('form', {'id': 'loginForm'})['action']
    login_action_url = f'https://www.uaa003.com{login_action}'

    # 构造登录请求的headers和data
    headers = {
        'Referer': referer,
    }

    login_data = {
        '_csrf': csrf_token,
        'email': login_payload['email'],
        'password': login_payload['password'],
    }

    # 发送模拟点击登录按钮的请求
    login_response = session.post(login_action_url, headers=headers, data=login_data)

    # 检查登录是否成功
    if '登录成功' in login_response.text:
        print('登录成功')
    else:
        print('登录失败，请检查用户名和密码')
        exit()


def get_novel_chapters(session, novel_url):
    # 示例：获取小说章节
    response = session.get(novel_url)
    html_content = response.text

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取所有章节链接
    chapter_links = soup.select('.volume a.chapter')

    all_chapters = []
    for chapter_link in chapter_links:
        chapter_url = 'https://www.uaa003.com' + chapter_link['href']
        chapter_title = chapter_link.select_one('.title').text.strip()
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

    # 创建一个session来保持登录状态
    session = requests.Session()

    # 登录
    simulate_login(session, login_url, login_payload)

    # 获取小说章节
    novel_url = 'https://www.uaa003.com/novel/intro?id=11306906'
    get_novel_chapters(session, novel_url)
