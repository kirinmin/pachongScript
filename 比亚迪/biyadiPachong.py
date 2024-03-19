import requests
from urllib import request
import os

cookies = {
    'JSESSIONID': 'CAD9F65CD46FDD1F77B67CFC6402D040',
    'SF_cookie_4': '27783614',
    'insert_cookie': '37836164',
    '_sp_ses.2141': '*',
    'routeId': '.uc1',
    '_sp_id.2141': '1daed846-960d-4bc8-8264-49d6e32f05e9.1710837792.1.1710837937.1710837792.751f332b-bf90-48ab-b50a-bf568067731e',
    'SID': '44cda023-0192-4967-a51a-18a09faa35e7',
    'cninfo_user_browse': '002594,gshk0001211,%E6%AF%94%E4%BA%9A%E8%BF%AA',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=CAD9F65CD46FDD1F77B67CFC6402D040; SF_cookie_4=27783614; insert_cookie=37836164; _sp_ses.2141=*; routeId=.uc1; _sp_id.2141=1daed846-960d-4bc8-8264-49d6e32f05e9.1710837792.1.1710837937.1710837792.751f332b-bf90-48ab-b50a-bf568067731e; SID=44cda023-0192-4967-a51a-18a09faa35e7; cninfo_user_browse=002594,gshk0001211,%E6%AF%94%E4%BA%9A%E8%BF%AA',
    'Origin': 'http://www.cninfo.com.cn',
    'Referer': 'http://www.cninfo.com.cn/new/disclosure/stock?orgId=gshk0001211&stockCode=002594',
   #'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'stock': '002594,gshk0001211',
    'tabName': 'fulltext',
    'pageSize': '30',
    'pageNum': '1',
    'column': 'szse',
    'category': '',
    'plate': 'sz',
    'seDate': '',
    'searchkey': '',
    'secid': '',
    'sortName': '',
    'sortType': '',
    'isHLtitle': 'true',
}

proxies = {
    'http': 'http://60.182.197.86:8888',
    'https': 'https://60.182.197.86:8888'
}

response = requests.post(
    'http://www.cninfo.com.cn/new/hisAnnouncement/query',
    cookies=cookies,
    headers=headers,
    data=data,
#proxies=proxies,    #使用代理ip，防止反爬
    verify=False,
).json()
#print(response.find("totalRecordNum"))
# for i in response['announcements']:
#     reportName=i['tileSecName']+'-'+i['announcementTitle']
#     print(reportName)
#     reportUrl = 'http://static.cninfo.com.cn/' + i['adjunctUrl']
#     print(reportUrl)
#     request.urlretrieve(reportUrl, r'./AnnualReport/'+reportName+'.pdf')
print('总的页数：'+str(response['totalpages']))
print('总的数目：'+str(response['totalRecordNum']))
num=0
for i in range(1,2+response['totalpages']):
    #print(i)
    data['pageNum']=i
    response = requests.post(
        'http://www.cninfo.com.cn/new/hisAnnouncement/query',
        cookies=cookies,
        headers=headers,
        data=data,
        #proxies=proxies,  # 使用代理ip，防止反爬
        verify=False,
    )
    if response.status_code==200:
        print(response.text)
        response=response.json()
        # for j in response['announcements']:
        #     reportName=j['tileSecName']+'-'+j['shortTitle']
        #     #print(reportName)
        #     reportUrl = 'http://static.cninfo.com.cn/' + j['adjunctUrl']
        #     #print(reportUrl)
        #     request.urlretrieve(reportUrl, r'./AnnualReport/'+reportName.replace("/","-")+'.pdf')
        #     print(num)
        #     num=num+1
        #     print(r'./AnnualReport/'+reportName+'.pdf'+'下载完成')
        for j in response['announcements']:
            reportName = j['tileSecName'] + '-' + j['shortTitle']
            reportUrl = 'http://static.cninfo.com.cn/' + j['adjunctUrl']
            reportFilePath = r'./AnnualReport/' + reportName.replace("/", "-") + '.pdf'

            # 检查目录是否存在，如果不存在则创建
            directory = os.path.dirname(reportFilePath)
            if not os.path.exists(directory):
                os.makedirs(directory)
            # 下载文件
            request.urlretrieve(reportUrl, reportFilePath)
            print(num)
            num += 1
            print(reportFilePath + '下载完成')