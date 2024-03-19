import requests
from openpyxl import Workbook
from tqdm import tqdm

cookies = {
    'JSESSIONID': 'BD7215C4C3AF54C6732BE7EA28B0DBBA',
    'SF_cookie_26': '46124957',
    'Hm_lvt_ac5110c8893f1f2e7a1be0acf395c2d5': '1709027460,1709028244,1709052585,1710690767',
    'Hm_lpvt_ac5110c8893f1f2e7a1be0acf395c2d5': '1710690778',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,de-DE;q=0.5,de;q=0.4',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=BD7215C4C3AF54C6732BE7EA28B0DBBA; SF_cookie_26=46124957; Hm_lvt_ac5110c8893f1f2e7a1be0acf395c2d5=1709027460,1709028244,1709052585,1710690767; Hm_lpvt_ac5110c8893f1f2e7a1be0acf395c2d5=1710690778',
    'Origin': 'http://60.164.220.222:9620',
    'Referer': 'http://60.164.220.222:9620/tip/stdrg.do?method=fwdStdPositionStatisQuery&pcid=62924020110000000164',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'method': 'queryPositionStatisticsData',
}

data = {
    'zwdm': '3967',
    'pcid': '62924020110000000164',
    'page': '1',
}

response = requests.post(
    'http://60.164.220.222:9620/tip/stdrg.do',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
# 初始的zwdm列表，你可以根据需要添加更多的值
# zwdm_list = ['0091', '0001', '0002']
zwdm_list = [str(i).zfill(4) for i in range(1, 4127)]


# 定义一个函数来发送请求并处理响应
def send_request(zwdm):
    data = {
        'zwdm': zwdm,
        'pcid': '62924020110000000164',
        'page': '1',
    }
    response = requests.post(
        'http://60.164.220.222:9620/tip/stdrg.do',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()


if __name__ == '__main__':
    response_data_list=[]
    # 主循环，遍历zwdm列表并发送请求
    # for zwdm in zwdm_list:
    for zwdm in tqdm(zwdm_list, desc="Processing zwdm_list", unit="request"):
        response_data = send_request(zwdm)
        response_data_list.append(response_data)
        # 处理响应数据，例如打印或保存到文件
        # print(response_data)
    # Initialize an empty list to store all results
    all_results = []

    for response_data in response_data_list:
        # Extracting the required information from response_data
        results = []
        for record in response_data.get('dstj', []):
            row = [record.get('dwmc', ''), record.get('zwdm', ''), record.get('zwmc', ''),
                   record.get('jhzkrs', ''), record.get('shtgrs', ''), record.get('jfcgrs', ''),
                   record.get('bmcgrs', '')]
            results.append(row)

        # Append results to all_results
        all_results.extend(results)

            # 将结果写入Excel文件
    wb = Workbook()  # 创建一个新的工作簿
    ws = wb.active  # 获取活动工作表

    # 写入表头
    headers = ['招考单位', '职位代码', '职位名称', '计划招考人数', '审核通过人数', '缴费成功人数', '报名成功人数']
    ws.append(headers)  # 将表头添加到工作表

    # 写入查询结果
    for row in all_results:
        ws.append(row)  # 将每行数据添加到工作表

    # 保存工作簿为Excel文件
    file_name = 'query_results1.xlsx'
    wb.save(file_name)

    print(f"查询结果已保存到文件 {file_name} 中。")
