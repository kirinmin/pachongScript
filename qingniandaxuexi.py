# encoding=utf-8
# pip install selenium
# pip install baidu-aip
# pip install pillow
# pip install pandas and pip install lxml and pip install html5lib、BeautifulSoup4 (bs4)
import csv
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--no-sandbox");
Chrome_options.add_argument("--disable-dev-shm-usage");
Chrome_options.add_argument("--window-size=1920,1080"); # 建议设置窗口大小
Chrome_options.add_argument('--headless')
driver_path = r'D:\software\python3.8\Scripts\chromedriver.exe'
# browser = webdriver.Chrome(executable_path=driver_path)
# browser = webdriver.Chrome(service=Service(driver_path))
# service = Service(driver_path)
# browser = webdriver.Chrome(service=service, options=Chrome_options)


def login1(name, Stu_id, tel, major):
    loginUrl="https://jinshuju.net/f/qgHRVA"
    browser.get(loginUrl)
    browser.maximize_window()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # 学院、支部
    # 等待选择框出现
    wait = WebDriverWait(browser, 10)
    select_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select-selector']")))
    # 点击选择框
    select_box.click()
    # move1=browser.find_element(By.XPATH,"//div[@class='rc-virtual-list-scrollbar-thumb']")
    time.sleep(0.4)
    # browser.set_window_size(1280, 800)
    # move2 = wait.until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@class='rc-virtual-list-scrollbar-thumb']"))
    # )
    move2=browser.find_element(By.XPATH, "//div[@class='rc-virtual-list-scrollbar-thumb']")
    time.sleep(0.4)
    actions = ActionChains(browser)
    # actions.move_to_element(move1).click_and_hold().move_by_offset(0, 40).release().perform()
    actions.move_to_element(move2).click_and_hold().move_by_offset(0, 130).release().perform()

    # 选择选项
    option = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@title='软件学院团委']")))
    actions.click(option).perform()
    # # 移动鼠标到目标元素上方并单击
    # hover = ActionChains(browser).move_to_element(br3)
    # hover.perform()

    # 等待选择框出现
    wait = WebDriverWait(browser, 10)
    select_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dropdown-field field field_4']")))#这个地方需要修改
    # 点击选择框
    select_box.click()
    # move1=browser.find_element(By.XPATH,"//div[@class='rc-virtual-list-scrollbar-thumb']")
    time.sleep(0.5)
    # browser.set_window_size(1280, 800)
    # move2 = wait.until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@class='rc-virtual-list-scrollbar-thumb']"))
    # )
    # 选择选项
    # option = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//div[@title='20级研究生']")))
    # time.sleep(0.4)
    # option.click()

    #姓名、学号、电话
    # name_field = wait.until(EC.presence_of_element_located((By.ID, "TextInputfield_1")))
    # name_field = wait.until(EC.presence_of_element_located((By.ID, "TextInputfield_1")))
    # 在姓名字段中输入值
    print(name,Stu_id,tel,major)

    name_field = browser.find_element(By.CSS_SELECTOR,"#TextInputfield_1")
    name_field.send_keys(name)
    br2 = browser.find_element(By.CSS_SELECTOR,"#TextInputfield_2")
    # br1.send_keys(name)
    br2.send_keys(Stu_id)
    # br4=browser.find_element(By.CSS_SELECTOR,"#root > div > form > div.published-form__body > div > div:nth-child(6) > div > div > div.ant-col.ant-form-item-control > div.ant-form-item-control-input > div > div > div > div > span > input")
    br4=browser.find_element(By.CSS_SELECTOR,"#root > div > form > div.published-form__body > div > div.ant-col.field-container.field.MobileField.ant-col-xs-24.ant-col-sm-24.ant-col-md-24 > div > div > div.ant-col.ant-form-item-control > div.ant-form-item-control-input > div > div > div > div > span > input")
    br4.send_keys(tel)
    time.sleep(0.5)
   #专业
    browser.find_element(By.CSS_SELECTOR,"#TextInputfield_34").send_keys(major)
    browser.find_element(By.CSS_SELECTOR,"#root > div > form > div.published-form__footer.center > div > button").click()
    # 提交表单
    submit_button = browser.find_element_by_css_selector("button[type='button']")
    submit_button.click()
    time.sleep(1)


if __name__ == '__main__':
    # num = input("请输入需要自动化操作的人数:\n")
    # num = int(num)
    # # print(num)
    personInfor = []
    title = '20研究生'
    try:
        with open('%s.csv' %title, 'r+', encoding='utf-8-sig', newline='') as fp:
            for row in csv.reader(fp,skipinitialspace=True):
                personInfor.append(row)

        name, Stu_id,tel,major = zip(*personInfor)
        # result = [item for sublist in personInfor for item in sublist]
        # 将每个列表中的每一项拆分开来
        # names = [names.split('\ufeff')[1] for name in names]  # 去掉名字中的 \ufeff 字符
        # Stu_id = [Stu_id.split() for Stu_id in Stu_id]
        # tel = [tel.split() for tel in tel]
        # major = [major.split() for major in major]

        # print(name)
        # for i in range(9):
        #     print(name[3*(i-1)])
        # print(Stu_id)

    except Exception as e:
        print(e)
    # for i in range(2):
    #     try:
    #         # driver_path = r'D:\software\python3.8\Scripts\chromedriver.exe'
    #         browser = webdriver.Chrome(executable_path=driver_path)
    #         # browser = webdriver.Chrome(service=service, options=Chrome_options)
    #         login1(name[i], Stu_id[i],tel[i],major[i])
    #         # login1(result[0+3*(i-1)], result[1+3*(i-1)],result[2+3*(i-1)],result[3+3*(i-1)])
    #         # browser.close()
    #         browser.quit()
    #     except Exception as e:
    #         print(e)
    #         browser.quit()
    #         break
    for i in range(2):
        # driver_path = r'D:\software\python3.8\Scripts\chromedriver.exe'
        browser = webdriver.Chrome(executable_path=driver_path)
        # browser = webdriver.Chrome(service=service, options=Chrome_options)
        login1(name[i], Stu_id[i],tel[i],major[i])
        # login1(result[0+3*(i-1)], result[1+3*(i-1)],result[2+3*(i-1)],result[3+3*(i-1)])
        # browser.close()
        time.sleep(5)
        browser.quit()
    fp.close()

# 王杰,12020210021,18869736668,电子信息
# 麦嘉成,12020210022,13164188813,电子信息
# 林钰尧,12020210023,13420110146,电子信息
# 陈施宇,12020210024,15520737867,电子信息
# 王佳能,12020210025,15898579129,电子信息
# 韩立飞,12020210026,13125999138,电子信息
# 沙聪,12020210027,13526051352,电子信息
# 王泽深,12020210028,13726265068,电子信息
# 艾合买提尼牙孜·阿不力米提,12020210029,18487152024,电子信息
# 焦雨露,12020210030,18314406776,电子信息
