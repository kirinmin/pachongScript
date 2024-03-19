# encoding=utf-8
import csv
import time

#from unicodedata import normalize
from openpyxl import Workbook

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.common.keys import Keys
driver_path = r'D:\software\python3.8\Scripts\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--no-sandbox");
Chrome_options.add_argument("--disable-dev-shm-usage");
Chrome_options.add_argument("--window-size=1920,1080"); # 建议设置窗口大小
Chrome_options.add_argument('--headless')


def login1(id, pw):
    loginUrl="http://60.164.220.222:9620/tip/stdlogin.do?method=fwdLoginPage"
    driver.get(loginUrl)
    driver.maximize_window()

    tel_box=driver.find_element(By.ID,'std_yhbh')
    time.sleep(0.4)
    tel_box.send_keys(id)
    pw_box=driver.find_element(By.ID,'std_yhmm')
    pw_box.send_keys(pw)
    time.sleep(10)

    loginButton=driver.find_element(By.CSS_SELECTOR,'body > div.main > div > a.btn-dl')
    loginButton.click()


def paqu_infor(job_num_start, job_num_end):
    job_codes = [str(i).zfill(4) for i in range(job_num_start, job_num_end)]
    error_codes = []  # 用于记录出错的职位代码
    batch_size = 10  # 每次查询的职位代码数量

    start_code = job_num_start  # 初始化起始职位代码

    while start_code < job_num_end:
        batch_job_codes = [str(i).zfill(4) for i in range(start_code, min(start_code + batch_size, job_num_end))]
        results = []  # 每个小批次的结果

        for job_code in batch_job_codes:
            try:
                search_input = driver.find_element(By.CSS_SELECTOR, '#searchTerm')
                search_input.clear()
                search_input.send_keys(job_code)
                time.sleep(0.1)
                search_button = driver.find_element(By.CSS_SELECTOR, '#searchBtn')
                time.sleep(0.1)
                search_button.click()
                time.sleep(0.1)
                table_body = driver.find_element(By.CSS_SELECTOR, '#tableBody')
                time.sleep(0.2)
                rows = table_body.find_elements(By.TAG_NAME, 'tr')
                time.sleep(0.2)

                row_data = []  # 用于存储当前职位代码的数据
                for row in rows:
                    if row.find_elements(By.TAG_NAME, 'td'):  # 确保行中有数据
                        try:
                            cells = row.find_elements(By.TAG_NAME, 'td')
                            data = [cell.text for cell in cells]
                            row_data.append(data)
                        except StaleElementReferenceException:
                            cells = row.find_elements(By.TAG_NAME, 'td')
                            data = [cell.text for cell in cells]
                            row_data.append(data)

                results.extend(row_data)

            except TimeoutException:
                print(f"Timeout waiting for element while inputting job code: {job_code}")
                error_codes.append(job_code)  # 记录出错的职位代码

        # 写入Excel文件
        if results:
            wb = Workbook()  # 创建一个新的工作簿
            ws = wb.active  # 获取活动工作表
            headers = ['招考单位', '职位代码', '职位名称', '计划招考人数', '审核通过人数', '缴费成功人数', '报名成功人数']
            ws.append(headers)  # 将表头添加到工作表
            for row in results:
                ws.append(row)  # 将每行数据添加到工作表
            wb.save(f'query_results_{job_num_start}_{start_code}.xlsx')  # 按批次保存文件

        start_code += batch_size  # 更新起始职位代码

    # 如果还有出错的职位代码，返回出错点，以便下次从该点继续查询
    if error_codes:
        return error_codes[-1]  # 返回最后一个出错的职位代码
    else:
        return None


if __name__ == '__main__':
    login1("620403199911163116", "123456am")
    time.sleep(0.5)
    driver.get("http://60.164.220.222:9620/tip/stdrg.do?method=fwdStdPositionStatisQuery&pcid=62924020110000000164")

    # 假设从3300开始查询，到3500结束
    start_code = 3300
    end_code = 3500

    # 开始查询，并记录出错的职位代码
    error_code = None  # 用于记录上一次的错误代码
    while start_code is not None:
        try:
            # 调用函数进行查询，并接收可能出现的错误代码
            start_code = paqu_infor(start_code, min(start_code + 10, end_code))
        except Exception as e:
            # 如果在查询过程中出现其他异常，打印错误信息
            print(f"An error occurred: {e}")
            # 如果这是第一次出错，或者错误代码不是上一次的错误代码，记录错误代码
            if error_code is None or error_code != start_code - 1:
                error_code = start_code - 1
                # 如果出错，下次查询从出错点继续
            time.sleep(2)  # 暂停5秒，以便观察或处理错误
        else:
            # 如果没有错误，重置错误代码
            error_code = None
            # 关闭WebDriver
    driver.quit()
