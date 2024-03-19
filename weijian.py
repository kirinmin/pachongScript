# coding:utf-8
# pip install selenium
# pip install baidu-aip
# pip install pillow
# pip install pandas and pip install lxml and pip install html5lib、BeautifulSoup4 (bs4)
import base64
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import requests
from io import BytesIO
# pip install matplotlib
# pip install opencv-python
# pip install chardet


import matplotlib.pyplot as plt
Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--no-sandbox");
Chrome_options.add_argument("--disable-dev-shm-usage");
Chrome_options.add_argument("--window-size=1920,1080"); # 建议设置窗口大小
Chrome_options.add_argument('--headless')
browser = webdriver.Chrome(service=Service(r'D:\software\python3.8\Scripts\chromedriver.exe'))

my_headers= [
    {"User-Agent":"User-Agent=Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
    {"User-Agent":"User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
]
def dealTime(update_time):
    timeArray = time.localtime(update_time)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime

def login(x,y):
    loginUrl="https://www.gsyqfk.com/epidemic_platform/#/wgyLogin"
    browser.get(loginUrl)
    br1 = browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.login-border > div.login-main > form > div:nth-child(1) > div > div > input")
    br2 = browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.login-border > div.login-main > form > div:nth-child(2) > div > div > input")
    br1.send_keys('18294888589')
    br2.send_keys('bykb@2022!')
    br3 = browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.login-border > div.login-main > form > div:nth-child(3) > div > div > div.el-col.el-col-8 > div > img")
    yzmdata = requests.get(br3.get_attribute('src'))
    tempIm = BytesIO(yzmdata.content)
    im = Image.open(tempIm)
    print(code)
    browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.login-border > div.login-main > form > div:nth-child(3) > div > div > div.el-col.el-col-16 > div > input").send_keys(str(code))
    browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.login-border > div.login-main > form > div:nth-child(5) > div > button").click()




def homework():
    browser.find_element(By.CSS_SELECTOR,"#app > div > div:nth-child(2) > main > div > div.main-page > section.searchArea.showSearchArea > div > div:nth-child(2) > div > div > div > input").click()
    time.sleep(0.8)
    browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[2]/span").click()
    #/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[2]/span

    time.sleep(0.8)
    browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[1]/label").click()
    time.sleep(0.8)
    #/html/body/div[1]/div/div[2]/main/div/div[6]/section[1]/div/div[12]/div[1]
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[6]/section[1]/div/div[12]/div[1]").click()
    for k in range(888):
        time.sleep(0.8)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[6]/section[1]/div/div[12]/div[1]").click()
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[6]/div/div[2]/div[4]/div[2]/table/tbody/tr/td[39]/div/span[1]").click()
        mainWindow = browser.current_window_handle
        new_window = browser.window_handles[-1]
        time.sleep(0.8)
        browser.switch_to.window(new_window)
        # time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div/div[1]/input").click()
        time.sleep(0.6)
        browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li[1]").click()
        time.sleep(0.6)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input").click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[1]/ul/li[3]").click()
        time.sleep(0.8)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[2]/div[1]/form/div[2]/div[5]/div/div/div/input").send_keys('水沟沿小区')
        time.sleep(0.6)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[2]/div[1]/form/div[2]/div[6]/div[1]/div/div/div/input").click()
        time.sleep(0.6)
        browser.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/ul/li[1]").click()
        time.sleep(0.6)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[2]/div[1]/div/div[2]").click()
        time.sleep(0.6)
        browser.close()
        browser.switch_to.window(mainWindow)
        try:
            browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/main/div/div[6]/div/div[3]/div[2]/div[2]/ul/li").click()
        except Exception as e:
            print('翻页失败')
# http://www.360doc.com/content/20/1024/09/55172838_942118715.shtml
def discern_captcha():
    # 识别码
    APP_ID = '26735828'
    API_KEY = 'HmGUVHEr1dZlSifohGG6eKj2'
    SECRET_KEY = '5eh3ps9LFNSaWxgCUI1zNy5o4OkBRe1L'
    # 初始化对象
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 读取图片
    def get_file_content(file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    image = get_file_content('yzm.png')
    # 定义参数变量
    options = {'language_type': 'ENG', }  # 识别语言类型，默认为'CHN_ENG'中英文混合
    #  调用通用文字识别
    # result = client.basicGeneral(image, options)  # 高精度接口 basicAccurate
    result = client.basicAccurate(image, options)  # 高精度接口 basicAccurate
    # result = client.handwriting(image, options)  #手写识别
    for word in result['words_result']:
        captcha = (word['words'])
        print('识别结果：' + captcha)
        return captcha
def bykb(account,pw):
    loginUrl = "http://125.74.55.238:8005/blmpms/#/login"
    browser.get(loginUrl)
    browser.maximize_window()
    br1 = browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[2]/form/div[1]/div/div/input")
    br2 = browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[2]/form/div[2]/div/div/input")
    br1.send_keys(account)
    br2.send_keys(pw)
    # br3 = browser.find_element(By.CSS_SELECTOR,"#app > div > div.login-area > div.login-area-right > div.login-area-form > form > div:nth-child(3) > div > div.imgAreas.el-col.el-col-6 > img")
def login_pictrue():
    browser.save_screenshot('bykb_login.png')
    # #获取验证码元素的位置
    yzm = browser.find_element(By.CSS_SELECTOR,'#app > div > div > div.login-border > div.login-main > form > div:nth-child(3) > div > div > div.el-col.el-col-8 > div > img')
    # #获取验证码的坐标
    loc = yzm.location
    # #获取验证码图片的宽高
    size = yzm.size
    print("坐标:", loc)
    print("宽高", size)
    # #获取验证码位置（此处的定位有问题，所以只能自己手动调整位置）
    left = loc['x'] + 250
    top = loc['y'] + 100
    bottom = top + size['height'] + 30
    right = left + size['width'] + 30
    # #打开页面截图
    page_pic = Image.open('bykb_login.png')
    yzm_pic = page_pic.crop((left, top, right, bottom))  # 这里需要传入一个元组
    yzm_pic.save('yzm.png')

    img = cv2.imread('yzm.png')
    img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 灰度化
    img3 = cv2.inRange(img2, lowerb=160, upperb=255)

    result2 = cv2.bilateralFilter(img3, 3, 560, 560)  # 双边滤波函数

    cv2.imwrite('yzm.png', result2)
    captcha = discern_captcha()
    browser.find_element(By.CSS_SELECTOR, "#app > div > div > div.login-border > div.login-main > form > div:nth-child(3) > div > div > div.el-col.el-col-16 > div > input").send_keys(
        captcha)
    time.sleep(7)
    browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.login-border > div.login-main > form > div:nth-child(5) > div > button").click()
    time.sleep(2)
    try:
        msg = browser.find_element(By.CSS_SELECTOR,"#app > div > div.home-page-header > div.header-right > div > div.top-bar__right > div.dept-box.el-dropdown > span").text
        if msg:
            print('登陆成功')
            print(msg)
    except Exception as e:
        print('登陆失败:{}'.format(e))
        login_pictrue()
    # finally:
    #     time.sleep(1)
def bykb_homework(pw):
    # 初始化pw部分
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/form/div[1]/div/div/input").send_keys(pw)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/form/div[2]/div/div/input").send_keys(pw)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div/button/span").click()
    # 疫情防控管理
    browser.find_element(By.CSS_SELECTOR,"#app > div > div.home-model-box > div > div.el-scrollbar__wrap > div > div:nth-child(3) > div.home-model-title").click()
    time.sleep(0.5)
    # 循环点击开始
    for k in range(8):
        # 入银上报管理
        browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li/ul/li[4]").click()
        time.sleep(0.8)
        # 未核查查询与点击
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[4]/div/div[1]/input").click()
        time.sleep(0.8)
        browser.find_element(By.CSS_SELECTOR,"body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)> span").click()
        time.sleep(0.8)
        # ActionChains(browser).move_to_element(move)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[6]/button").click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[11]/div/div/div[2]/button").click()
        time.sleep(0.5)
        browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(9) > div:nth-child(1) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input").click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/ul/li[2]").click()
        time.sleep(0.5)
        browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(17) > div > div > div > div > div.el-input.el-input--medium.el-input--suffix > input").click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[1]/ul/li[1]").click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/button[2]").click()
        # 每页100条
        # browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/span[2]/div/div").click()
        # time.sleep(0.8)
        # browser.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/ul/li[4]").click()
        time.sleep(0.5)
        # 关闭该小标签页，后续循环重新打开，否则不利于元素定位
        browser.find_element(By.CSS_SELECTOR,"#tab-\/nucleicAcid\/comeYing > span").click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li/ul/li[4]").click()
        # try:
        #     browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li").click()
        # except Exception as e:
        #     print('翻页失败')
def bykb_text():
    bykb('19994317972', 'bykb@2022!')
    login_pictrue()
    informationList = []

    # # 初始化pw部分
    # pwd='bykb@2022!'
    # browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/form/div[1]/div/div/input").send_keys(pwd)
    # browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/form/div[2]/div/div/input").send_keys(pwd)
    # browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/div/button/span").click()
    # time.sleep(0.4)
    # 信息抓取准备
    # 跳过初始化密码部分
    browser.get("http://125.74.55.238:8005/blmpms/#/wel/index")
    time.sleep(0.8)
    browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
    time.sleep(0.5)
    # # 已核查查询
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[4]/div/div[1]/input").click()
    # time.sleep(0.8)
    # browser.find_element(By.CSS_SELECTOR,"body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)> span").click()
    # time.sleep(0.8)
    # 查询按钮点击
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[6]/button").click()
    time.sleep(0.5)
    #循环获取信息
    for k in range(6):
        # 核查点击
        # browser.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[11]/div/div/div[1]/button").click()
        # time.sleep(0.5)
        name=browser.find_elements(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[2]")
        #//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[2]/td[2]
        #//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[3]/td[2]
        tel=browser.find_elements(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[3]")
        address=browser.find_elements(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[5]")
        come_date=browser.find_elements(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[7]")
        come_place=browser.find_elements(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[6]")
        # xingchen=browser.find_elements(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(11) > div > div > div")
        for n, t,ad,cd,cp in zip(name, tel,address,come_date,come_place):
            informationList.append(n.text+" "+t.text+" "+ad.text+" "+cd.text+" "+"从"+cp.text+"来平，请网格员联系报备")
        print(informationList),
        # browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__header > button").click()
        # time.sleep(0.5)
        # 翻页部分
        browser.find_element(By.CSS_SELECTOR, "#app > div > div > div.avue-layout > div.avue-main > div.main-scroll-box.el-scrollbar > div.el-scrollbar__wrap > div > div > div > div.el-col.el-col-20 > div > div:nth-child(3) > div > button.btn-next").click()
        time.sleep(0.5)
    for i in range(len(informationList)):
        title='白银快办后台核查信息简报'
        # 格式化字符串还能这么用！
        with open("%s.txt" %title, "w") as f:
            f.write(str(informationList)+'\n')

def get_data(page):
    bykb('19994317972', 'bykb@2022!')
    login_pictrue()
    informationList=[]
    # 跳过初始化密码部分
    browser.get("http://125.74.55.238:8005/blmpms/#/wel/index")
    #http://125.74.55.238:8005/blmpms/#/nucleicAcid/comeYing
    time.sleep(0.8)
    browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
    time.sleep(0.5)
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[6]/button").click()
    # time.sleep(0.5)
    # for i in range(1):
    if page == 1:
        for i in range(10):
            browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
            time.sleep(0.4)
            browser.find_element(By.XPATH,str("//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[" + str( i + 1) + "]/td[11]/div/div/div[2]/button")).click()
            time.sleep(0.4)
            n = browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").get_attribute('value')
            t = browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").get_attribute('value')
            time.sleep(0.1)
            ad = browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > input").get_attribute('value')
        # ad = browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > input").get_attribute('textContent')
        # cd = browser.find_element(By.CLASS_NAME,'[placeholder="请选择入银日期"]').text
            cd = browser.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').get_attribute('value')
        # cd = browser.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').get_attribute('innerText')
        # cp = browser.find_element(By.CLASS_NAME,'[placeholder="请选择从何地到银"]').text
            time.sleep(0.1)
            cp = browser.find_element(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').get_attribute('value')
            xc=browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(11) > div > div > div > textarea").get_attribute('value')
        # actions = ActionChains(browser)
        # actions.move_by_offset(0, 0).perform()
        # actions.move_by_offset(0,0).click()
            time.sleep(0.1)
            healthCode = browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(14) > div:nth-child(2) > div.el-form-item.el-form-item--medium > div > div > input").get_attribute('value')
            browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--default.el-button--medium").click()
            time.sleep(0.3)
            browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.avue-layout > div.avue-main > div.avue-tags > div > div.avue-tags__menu.el-dropdown > button > span").click()
            time.sleep(0.3)
            browser.find_element(By.XPATH,"/html/body/ul/li[2]").click()
            time.sleep(0.3)
            informationList.append(n + " " + t + " " + ad + " " + cd + "日" + "从" + cp + "来平，" + "行程信息：" + xc + "【健康码状态】：" + "【" + healthCode + "】" + "，请网格员联系报备")
            # print(informationList[i])
    elif page == 2:
        for i in range(10):
            browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
            time.sleep(0.4)
            browser.find_element(By.XPATH,str("//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[" + str(i + 1) + "]/td[11]/div/div/div[2]/button")).click()
            time.sleep(0.4)
            n = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").get_attribute(
                'value')
            t = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            time.sleep(0.1)
            ad = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            cd = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').get_attribute(
                'value')
            time.sleep(0.1)
            cp = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').get_attribute(
                'value')
            time.sleep(0.1)
            xc = browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(11) > div > div > div > textarea").get_attribute('value')
            healthCode = browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(14) > div:nth-child(2) > div.el-form-item.el-form-item--medium > div > div > input").get_attribute('value')
            #
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--default.el-button--medium").click()
            time.sleep(0.3)
            browser.find_element(By.CSS_SELECTOR,
                                 "#app > div > div > div.avue-layout > div.avue-main > div.avue-tags > div > div.avue-tags__menu.el-dropdown > button > span").click()
            time.sleep(0.3)
            browser.find_element(By.XPATH, "/html/body/ul/li[2]").click()
            time.sleep(0.3)
            informationList.append(n + " " + t + " " + ad + " " + cd + "日" + "从" + cp + "来平，" + "行程信息：" + xc + "【健康码状态】：" + "【" + healthCode + "】" + "，请网格员联系报备")
            # print(informationList[i])
        for i in range(10):
            browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
            time.sleep(0.3)
            # 翻页1次
            browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.avue-layout > div.avue-main > div.main-scroll-box.el-scrollbar > div.el-scrollbar__wrap > div > div > div > div.el-col.el-col-20 > div > div:nth-child(3) > div > button.btn-next").click()
            time.sleep(0.3)
            browser.find_element(By.XPATH,str("//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[" + str(
                                     i + 1) + "]/td[11]/div/div/div[2]/button")).click()
            time.sleep(0.3)
            n = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").get_attribute(
                'value')
            t = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            time.sleep(0.1)
            ad = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')

            cd = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').get_attribute(
                'value')

            time.sleep(0.1)
            cp = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').get_attribute(
                'value')
            time.sleep(0.1)
            xc = browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(11) > div > div > div > textarea").get_attribute(
                'value')
            healthCode = browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(14) > div:nth-child(2) > div.el-form-item.el-form-item--medium > div > div > input").get_attribute('value')
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--default.el-button--medium").click()
            time.sleep(0.4)

            browser.find_element(By.CSS_SELECTOR,
                                 "#app > div > div > div.avue-layout > div.avue-main > div.avue-tags > div > div.avue-tags__menu.el-dropdown > button > span").click()
            time.sleep(0.4)
            browser.find_element(By.XPATH, "/html/body/ul/li[2]").click()
            time.sleep(0.4)
            informationList.append(n + " " + t + " " + ad + " " + cd + "日" + "从" + cp + "来平，" + "行程信息：" + xc + "【健康码状态】：" + "【" + healthCode + "】" + "，请网格员联系报备")
            # print(informationList[i+10])

    elif page == 3:
        for i in range(10):
            browser.find_element(By.XPATH,
                                 "/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
            time.sleep(0.5)
            browser.find_element(By.XPATH,
                                 str("//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[" + str(
                                     i + 1) + "]/td[11]/div/div/div[2]/button")).click()
            time.sleep(0.5)
            n = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").get_attribute(
                'value')
            t = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            time.sleep(0.1)
            ad = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')

            cd = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').get_attribute(
                'value')

            time.sleep(0.1)
            cp = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').get_attribute(
                'value')
            xc = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(11) > div > div > div > textarea").get_attribute(
                'value')

            time.sleep(0.1)
            healthCode = browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(14) > div:nth-child(2) > div.el-form-item.el-form-item--medium > div > div > input").get_attribute('value')
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--default.el-button--medium").click()
            time.sleep(0.3)
            browser.find_element(By.CSS_SELECTOR,
                                 "#app > div > div > div.avue-layout > div.avue-main > div.avue-tags > div > div.avue-tags__menu.el-dropdown > button > span").click()
            time.sleep(0.3)
            browser.find_element(By.XPATH, "/html/body/ul/li[2]").click()
            time.sleep(0.3)

            informationList.append(n + " " + t + " " + ad + " " + cd + "日" + "从" + cp + "来平，" + "行程信息：" + xc + "【健康码状态】：" + "【" + healthCode + "】" + "，请网格员联系报备")
            # print(informationList[i])
        for i in range(10):
            browser.find_element(By.XPATH,
                                 "/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
            time.sleep(0.4)
            # 翻页1次
            browser.find_element(By.CSS_SELECTOR,
                                 "#app > div > div > div.avue-layout > div.avue-main > div.main-scroll-box.el-scrollbar > div.el-scrollbar__wrap > div > div > div > div.el-col.el-col-20 > div > div:nth-child(3) > div > button.btn-next").click()
            time.sleep(0.3)
            browser.find_element(By.XPATH,
                                 str("//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[" + str(
                                     i + 1) + "]/td[11]/div/div/div[2]/button")).click()
            time.sleep(0.3)
            n = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").get_attribute(
                'value')
            time.sleep(0.1)
            t = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            ad = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            cd = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').get_attribute(
                'value')
            time.sleep(0.1)
            cp = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').get_attribute(
                'value')
            xc = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(11) > div > div > div > textarea").get_attribute(
                'value')
            healthCode = browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(14) > div:nth-child(2) > div.el-form-item.el-form-item--medium > div > div > input").get_attribute('value')
            time.sleep(0.1)
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--default.el-button--medium").click()
            time.sleep(0.4)
            browser.find_element(By.CSS_SELECTOR,
                                 "#app > div > div > div.avue-layout > div.avue-main > div.avue-tags > div > div.avue-tags__menu.el-dropdown > button > span").click()
            time.sleep(0.4)
            browser.find_element(By.XPATH, "/html/body/ul/li[2]").click()
            time.sleep(0.4)
            informationList.append( n + " " + t + " " + ad + " " + cd + "日" + "从" + cp + "来平，" + "行程信息：" + xc + "【健康码状态】：" + "【" + healthCode + "】" + "，请网格员联系报备")
            # print(informationList[i])
        for i in range(10):
            browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
            time.sleep(0.4)
            # 翻页2次
            browser.find_element(By.CSS_SELECTOR,"#app > div > div > div.avue-layout > div.avue-main > div.main-scroll-box.el-scrollbar > div.el-scrollbar__wrap > div > div > div > div.el-col.el-col-20 > div > div:nth-child(3) > div > button.btn-next").click()
            time.sleep(0.4)
            browser.find_element(By.CSS_SELECTOR, "#app > div > div > div.avue-layout > div.avue-main > div.main-scroll-box.el-scrollbar > div.el-scrollbar__wrap > div > div > div > div.el-col.el-col-20 > div > div:nth-child(3) > div > button.btn-next").click()
            time.sleep(0.4)
            browser.find_element(By.XPATH,str("//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr[" + str(i + 1) + "]/td[11]/div/div/div[2]/button")).click()
            time.sleep(0.4)
            n = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(1) > div > div > div > input").get_attribute(
                'value')
            t = browser.find_element(By.CSS_SELECTOR,
                                     "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            time.sleep(0.1)
            ad = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > input").get_attribute(
                'value')
            cd = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div > input').get_attribute(
                'value')
            time.sleep(0.1)
            cp = browser.find_element(By.CSS_SELECTOR,
                                      'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input').get_attribute(
                'value')
            xc = browser.find_element(By.CSS_SELECTOR,
                                      "body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(11) > div > div > div > textarea").get_attribute(
                'value')
            time.sleep(0.05)
            healthCode = browser.find_element(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(14) > div:nth-child(2) > div.el-form-item.el-form-item--medium > div > div > input").get_attribute('value')
            browser.find_element(By.CSS_SELECTOR,
                                 "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--default.el-button--medium").click()
            time.sleep(0.4)
            browser.find_element(By.CSS_SELECTOR,
                                 "#app > div > div > div.avue-layout > div.avue-main > div.avue-tags > div > div.avue-tags__menu.el-dropdown > button > span").click()
            time.sleep(0.4)
            browser.find_element(By.XPATH, "/html/body/ul/li[2]").click()
            time.sleep(0.4)
            informationList.append(n + " " + t + " " + ad + " " + cd + "日" + "从" + cp + "来平，" + "行程信息：" + xc + "【健康码状态】：" + "【"+healthCode+"】" + "，请网格员联系报备")
            # print(informationList[i])
        # browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[2]/ul/li[4]").click()
        # time.sleep(0.5)
        # # 翻页部分
        # browser.find_element(By.CSS_SELECTOR, "#app > div > div > div.avue-layout > div.avue-main > div.main-scroll-box.el-scrollbar > div.el-scrollbar__wrap > div > div > div > div.el-col.el-col-20 > div > div:nth-child(3) > div > button.btn-next").click()
        # time.sleep(0.5)
        # browser.find_element(By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__header > button").click()
        # time.sleep(0.5)

    for i in range(len(informationList)):
        title = '白银快办后台核查信息简报'
        # 格式化字符串还能这么用！
        with open("%s.txt" % title, "w") as f:
            f.write(str(informationList) + '\n')
    for i in range(len(informationList)):
        print(str(i+1)+"."+informationList[i])
if __name__ == '__main__':
    # try:
    #     # login3('18294888589', 'Aa123456?')
    #     login2('18294888589', 'Aa123456?')
    #     homework()
    # except Exception as e:41
    #     print('出现异常')
    #     print(e)
    #     browser.quit()
    global num
    num = input("请输入需要自动化操作系统的数字编号:\n"+"1.工信部甘肃省疫情协查系统\n"+"2.白银快办后台系统\n"+"3.白银快办系统后台防疫信息抓取\n"+"4.白银快办系统后台个人出行详细信息抓取\n")
    num = int(num)
    # print(num)
    while True:
    # for num in [1,2]:
        if int(num) == 1:
            try:
                #工信部甘肃省疫情协查系统自动化
                login2('18294888589', 'Aa123456?')
                homework()
                browser.quit()
            except Exception as e:
                print(e)
                browser.quit()
            break
        elif int(num) == 2:
            try:
                #白银快办系统后台自动化
                bykb('19994317972', 'bykb@2022!')
                login_pictrue()
                bykb_homework('bykb@2022!')
                browser.quit()
            except Exception as e:
                print(e)
                browser.quit()
            break
        elif int(num) == 3:
            try:
                #白银快办系统后台防疫信息抓取
                bykb_text()
                browser.quit()
            except Exception as e:
                print(e)
                browser.quit()
            break
        elif int(num) == 4:
            # 白银快办系统后台个人出行详细信息抓取
            page = input("请输入需要自动化抓取的页数，按回车键结束。\n")
            page = int(page)
            try:

                get_data(page)
                browser.quit()
            except Exception as e:
                print(e)
                browser.quit()
        elif ((int(num)!=1) and (int(num)!=4)) and ((int(num)!=2) and (int(num)!=3)):
            try:
                print("输入选项错误，请重新输入。")
            except Exception as e:
                print(e)
                browser.quit()
            continue
