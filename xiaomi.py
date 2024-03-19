import requests,json,time,base64,binascii,hashlib,datetime,sys
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cookie = {}
    def login(self):
        md5 = hashlib.md5()
        md5.update(self.password.encode())
        Hash = md5.hexdigest()
        sha1 = hashlib.sha1()
        url = 'https://account.xiaomi.com/pass/serviceLoginAuth2'
        headers = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 12; Redmi K20 Pro Build/SKQ1.211006.001) APP/xiaomi.vipaccount APPV/231026 MK/UmVkbWkgSzIwIFBybw== SDKV/5.1.0.release.13 PassportSDK/5.1.0.release.15 passport-ui/5.1.0.release.15'}
        data = {'callback':'https://api.vip.miui.com/sts','_json':'true','user':self.username,'hash':Hash.upper(),'sid':'miui_vip','_sign':'ZJxpm3Q5cu0qDOMkKdWYRPeCwps=','_locale':'zh_CN'}
        Auth = json.loads(requests.post(url=url,headers=headers,data=data).text.replace('&&&START&&&',''))
        if Auth['description'] == '登录验证失败':
            print('登陆验证失败')
            sys.exit()
        sha1.update(('nonce=' + str(Auth['nonce']) + '&' + Auth['ssecurity']).encode('utf-8'))
        clientSign = base64.encodebytes(binascii.a2b_hex(sha1.hexdigest().encode('utf-8'))).decode(encoding='utf-8').strip()
        nurl = Auth['location'] + '&_userIdNeedEncrypt=true&clientSign=' + clientSign
        self.cookie = requests.utils.dict_from_cookiejar(requests.get(url=nurl).cookies)
    def info(self):
        url = 'https://api.vip.miui.com/mtop/planet/vip/homepage/mineInfo'
        result = requests.get(url=url,cookies=self.cookie).json()
        print(f'昵称：{result["entity"]["userInfo"]["userName"]} 等级：{result["entity"]["userInfo"]["userGrowLevelInfo"]["showLevel"]} 积分：{result["entity"]["userInfo"]["userGrowLevelInfo"]["point"]} ')
    def check_in(self):
        url = f'https://api.vip.miui.com/mtop/planet/vip/user/getUserCheckinInfo?miui_vip_ph={self.cookie["miui_vip_ph"]}'
        result = requests.get(url=url,cookies=self.cookie).json()
        if result['entity']['checkin7DaysDetail'][datetime.date.today().weekday()] == 0:
            url = f'https://api.vip.miui.com/mtop/planet/vip/user/checkinV2'
            data = {'miui_vip_ph':self.cookie['miui_vip_ph'],'token':'lUyu4a4aDS2xHr9Wm3RecATnT+1eNx9hP6T53vEQ3BK6fl0sqy3OaF7RPisuuHcEd16hgmBEOnYXhpa7HXjEX493lVmNr2KJ/ShoW8maSlBkHW2BwdRqQU19HLXcuvn7Ydfc3hP/sVLvjIHTqRFuGNzQlmMUSxZrBJ+e1Jjy2PGbpE44NI/jmbIRDcCJeieVcr6RbVoVj3ljnYZ6bRELiljNMDBumvg3Y77tXv4pDkkLpcGv2ngIdRcn60/uhviO0PxsOe1/gteRqcaYBpQSfGFMp1Dx1RQpMWLlNX5+0WZPGmupI6jE'}
            result = requests.post(url=url,cookies=self.cookie,data=data).json()
            if 'success' not in result['message']:
                print(f'签到失败: {result["message"]}')
    def like(self):
        url = 'https://api.vip.miui.com/mtop/planet/vip/content/announceThumbUp'
        data = {'postId':'36625780','sign':'36625780','timestamp':int(round(time.time()*1000))}
        requests.get(url=url,cookies=self.cookie,data=data)
    def browse(self):
        url = f'https://api.vip.miui.com/mtop/planet/vip/member/addCommunityGrowUpPointByActionV2?miui_vip_ph={self.cookie["miui_vip_ph"]}'
        for action in ['BROWSE_POST_10S','BROWSE_SPECIAL_PAGES_SPECIAL_PAGE','BROWSE_SPECIAL_PAGES_USER_HOME']:
            data = {'action':action,'miui_vip_ph':self.cookie['miui_vip_ph']}
            requests.post(url,cookies=self.cookie,data=data)
    def carrot(self):
        url ='https://api.vip.miui.com/api/carrot/pull'
        requests.post(url=url,cookies=self.cookie,params={'miui_vip_ph': self.cookie['miui_vip_ph']})
    def check_status(self):
        url = f'https://api.vip.miui.com/mtop/planet/vip/member/getCheckinPageCakeList?miui_vip_ph={self.cookie["miui_vip_ph"]}'
        result = requests.get(url=url,cookies=self.cookie).json()
        for i in result['entity'][2]['data']:
            if i['jumpText'] == '已完成':
                print(i['title'],'√')
            elif i['jumpText'] == '':
                print(i['title'],'×')
    def run(self):
        self.login()
        self.info()
        self.check_in()
        self.like()
        self.browse()
        self.carrot()
        self.check_status()
# 创建多个账号
accounts = [
    Account("2463187658", "199911am")
    # Account("UID", "password")
]
# 登录并执行操作
for account in accounts:
    account.run()