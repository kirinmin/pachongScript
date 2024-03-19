@[TOC](Python爬虫获取接口数据)
获取静态网页数据的教程，适用于我们要爬取的数据在网页源代码中出现，但是还是有很多的数据是源代码中没有的，需要通过接口访问服务器来获得，下面我就来讲讲如何爬取这类数据。

以巨潮资讯网爬取比亚迪企业年报为例。

## 正常人的操作

 1. 打开巨潮资讯网官网 
 2. 找到比亚迪的公告 
 3. 在分类里面选择筛选信息，找到自己想要的信息
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/3ca1194a20084d5abce4207c07b29300.png#pic_center)
## ​​​​​​​​​​爬虫的思路

### 标题获取请求信息
在正常人的操作第三步，当我们选择一个类别时，毫无疑问浏览器肯定会对服务器发送请求信息，服务器返回信息后我们才能看到想要的信息，看一下怎么获取这个请求：
访问[巨潮资讯网](http://www.cninfo.com.cn/new/disclosure/stock?orgId=gshk0001211&stockCode=002594#financialStatements)
按下F12或者是右键检查，进入网络，先清空乱七八糟的网络信息
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/b3ce510d4c3d4f8e95606c938e648fd5.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/d128498695fa461e99b785530966f1d2.png#pic_center)
当我们选择一个类别时会看到右边多出一个query请求，这个就是我们向服务器发出的请求
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/23db8abb3f6240ad81b0b0086981da0b.png#pic_center)
我们可以查看query这条请求的信息
## 标题请求转换为代码
上一步我们获取到了请求信息，我们就可以使用python造一个请求头，主要包含请求头和请求负载，我们荡当然可以使用比较奔的方法一个一个的复制粘贴，把东西搬到代码上，这里推荐一个工具能自动帮我们把请求格式化我们想要的

把请求复制下来
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c07a15ef037247259316076aaeba4d72.png#pic_center)
​
在Curl命令转代码工具 (sbox.cn)这个在线网站[添加链接描述](https://sbox.cn/tool/curlconverter)可以直接转换为python代码
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/50354001704848c3bd189b4b7119559b.png#pic_center)
## 完整代码

```python
import requests

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

response = requests.post(
    'http://www.cninfo.com.cn/new/hisAnnouncement/query',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
```
## 请求返回信息
请求信息在调试窗口响应上查看，当然也可以通过上一步通过代码获取的返回打印出来查看。

可以看到，一个个报告主要是在"announcements"数组里，通过直觉"adjunctUrl"可能是报告的存放地址，来验证一下，随便打开一个报告，还是按照老方法查看网络请求，可以看到pdf的请求，是不是就是"adjunctUrl"加上前缀，通过查看多个报告，发现都是这个情况，就可以大胆地去操作了。

请求url为：'http://static.cninfo.com.cn/' + "adjunctUrl"
保存的文件名称：'tileSecName'+'-'+'announcementTitle'

有的分类不只有一页数据
可以看到"totalpages"这个字段跟页数有关，当只有一页的时候为0，两页的时候为1，请求头只有'pageNum'不一样，请求头'pageNum'与响应‘totalpages'是对应的，我们就可以这样写程序：

```python
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
```
## 执行程序
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/f0f59888075d4097aa1390e3acadf6bf.png#pic_center)

