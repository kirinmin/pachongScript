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
def clean_text(text):
    # 清理和转换文本
    return normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
def paqu_infor(job_num_start,job_num_end):
    # driver.get("http://60.164.220.222:9620/tip/stdrg.do?method=fwdCurrentPage")
    driver.get("http://60.164.220.222:9620/tip/stdrg.do?method=fwdStdPositionStatisQuery&pcid=62924020110000000164")
    # if 'iframe' in driver.page_source:  # 替换'frame_name'为实际的iframe或frame名称
    # driver.switch_to.frame('iframe')
    # a_element=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/ul/li/dl/dd[2]/a')))
    # a_element.click()
    # time.sleep(1)
    # driver.switch_to.frame("LAY_main")
    # buttons = driver.find_element(By.XPATH, '/html/body/div[1]/div/table/tbody/tr/td[4]/button[2]')
    # buttons.click()
    # time.sleep(1)
    # 生成职位代码列表
    # job_codes = [str(i).zfill(4) for i in range(1, 4127)]
    job_codes = [str(i).zfill(4) for i in range(job_num_start, job_num_end)]
    # job_codes = [str(i).zfill(4) for i in range(1, 4)]
    # 准备一个列表来存储查询结果
    results = []
    # 循环遍历每个职位代码
    for job_code in job_codes:
        try:
            # 等待搜索框加载完成并输入职位代码
            search_input = driver.find_element(By.CSS_SELECTOR, '#searchTerm')
            search_input.clear()
            search_input.send_keys(job_code)
            time.sleep(0.2)
            # 等待查询按钮加载完成并点击
            search_button = driver.find_element(By.CSS_SELECTOR, '#searchBtn')
            time.sleep(0.3)
            search_button.click()
            time.sleep(0.2)
            # 等待表格加载完成
            table_body = driver.find_element(By.CSS_SELECTOR, '#tableBody')

            # # 等待搜索框加载完成并输入职位代码
            # search_input = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, '#searchTerm'))
            # )
            # search_input.clear()
            # search_input.send_keys(job_code)
            # # 等待查询按钮加载完成并点击
            # search_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchBtn'))
            # )
            # search_button.click()
            #
            # # 等待表格加载完成
            # table_body = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, '#tableBody'))
            # )

            time.sleep(0.4)
            # 抓取表格中的所有行数据
            rows = table_body.find_elements(By.TAG_NAME, 'tr')
            time.sleep(0.4)
            for row in rows:
                # 假设表格的第一行是标题行，从第二行开始抓取数据
                if row.find_elements(By.TAG_NAME, 'td'):  # 确保行中有数据
                # # 抓取单元格数据
                #     cells = row.find_elements(By.TAG_NAME, 'td')
                #     data = [cell.text for cell in cells]
                # #     # 将每个单元格的文本转换为字符串，并添加到结果列表中
                # #     # data = [str(cell.text) for cell in cells]
                # #     # data = [cell.text if index != 1 else '\'' + cell.text for index, cell in enumerate(cells)]
                #     results.append(data)

                    # 抓取单元格数据
                    try:
                        cells = row.find_elements(By.TAG_NAME, 'td')
                        data = [cell.text for cell in cells]
                        results.append(data)
                    except StaleElementReferenceException:
                        # 如果元素过时了，重新定位并尝试再次获取
                        cells = row.find_elements(By.TAG_NAME, 'td')
                        data = [cell.text for cell in cells]
                        results.append(data)
                    # 输出数据
            # for row in data:
            #     print(row)
            # print(results)
                    # # 抓取单元格数据
                #     cells = row.find_elements(By.TAG_NAME, 'td')
                #     data = [clean_text(cell.text) for cell in cells]
                #     results.append(data)
                # 可能需要添加一些延迟，以便为每个查询操作提供足够的时间
            time.sleep(0.2)  # 等待1秒
        except TimeoutException:
            print(f"Timeout waiting for element while inputting job code: {job_code}")
    # driver.quit()

    # 将结果写入CSV文件
    # with open('query_results.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    #     writer = csv.writer(csvfile)
    #     # 写入表头（如果表格结构固定，可以手动定义表头）
    #     writer.writerow(['招考单位', '职位代码', '职位名称', '计划招考人数', '审核通过人数', '缴费成功人数', '报名成功人数'])
    #     # 写入查询结果
    #     writer.writerows(results)

    # 将结果写入Excel文件
    wb = Workbook()  # 创建一个新的工作簿
    ws = wb.active  # 获取活动工作表
    # 写入表头
    headers = ['招考单位', '职位代码', '职位名称', '计划招考人数', '审核通过人数', '缴费成功人数', '报名成功人数']
    ws.append(headers)  # 将表头添加到工作表
    # 写入查询结果
    for row in results:
        ws.append(row)  # 将每行数据添加到工作表
    # 保存工作簿为Excel文件
    wb.save(f'query_results_{job_num_start}.xlsx'  )

    print("查询结果已保存到文件中。")

if __name__ == '__main__':
    login1("620403199911163116","123456am")
    time.sleep(1)
    # paqu_infor(1,501)
    # paqu_infor(500,1001)
    # paqu_infor(1000,1301)
    # paqu_infor(1300,1601)
    # paqu_infor(1600,1901)
    # paqu_infor(1900,2201)
    # paqu_infor(2200,2501)
    # paqu_infor(2500,2801)
    # paqu_infor(2800,3101)
    # paqu_infor(3100,3301)
    paqu_infor(3300,3501)
    paqu_infor(3500,3701)
    paqu_infor(3700,3901)
    paqu_infor(3900,4001)
    paqu_infor(4000,4127)
    driver.quit()

