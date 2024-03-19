# encoding=utf-8
# pip install selenium
# pip install baidu-aip
# pip install pillow
# pip install pandas and pip install lxml and pip install html5lib、BeautifulSoup4 (bs4)
import random
import time
import time
import pickle
import random
import pyautogui
import threading
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver_path = r'D:\software\python3.8\Scripts\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--no-sandbox");
Chrome_options.add_argument("--disable-dev-shm-usage");
Chrome_options.add_argument("--window-size=1920,1080"); # 建议设置窗口大小
Chrome_options.add_argument('--headless')

# browser = webdriver.Chrome(executable_path=driver_path)
# browser = webdriver.Chrome(service=Service(driver_path))
# service = Service(driver_path)
# browser = webdriver.Chrome(service=service, options=Chrome_options)


def login1(tel, pw):
    loginUrl="https://www.douyin.com/"
    browser.get(loginUrl)
    browser.maximize_window()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # 等待选择框出现
    wait = WebDriverWait(browser, 10)
    select_box = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/div/article/article/article/div/ul[1]/li[3]')))
    # 点击选择框
    select_box.click()
    tel_box=browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div/article/article/article/form/div[1]/div/input')
    time.sleep(0.4)
    tel_box.send_keys(tel)
    pw_box=browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div/article/article/article/form/div[2]/div/div/input')
    pw_box.send_keys(pw)

    loginButton=browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/div/article/article/article/form/div[5]/button')
    loginButton.click()


def loginn():
    # loginUrl = urltext
    # loginUrl="https://live.douyin.com/211444707101"
    loginUrl="https://live.douyin.com/93173086668"
    # browser.get(loginUrl)

    driver.get(loginUrl)

    # time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[1]/pace-island/div/div[1]/header/div/div/div[2]/div/div/div[5]/div/div[1]/button").click()
    # browser.maximize_window()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(30)
def pinglun():
    fayan_box=driver.find_element(By.CSS_SELECTOR,'#chat-textarea')

    time.sleep(1)
    fayan_box.click()
    time.sleep(1)

    comments = [
        "小师妹之容颜，宛如画中仙子，令人心驰神往。",
        "小师妹之姿色，犹如春日之花，娇艳欲滴。",
        "小师妹之风姿，宛如秋月之皎洁，清丽脱俗。",
        "小师妹之容貌，犹如夏日之莲，出淤泥而不染。",
        "小师妹之气质，宛如冬日之梅，傲骨铮铮。",
        "小师妹之容颜，犹如晨曦之光，温暖而明媚。",
        "小师妹之风姿，犹如晚霞之绚烂，美不胜收。",
        "小师妹之容貌，犹如夜空之星，璀璨夺目。",
        "小师妹之气质，犹如山川之秀丽，令人心旷神怡。",
        "小师妹之容颜，犹如江河之水，清澈见底。",
        "小师妹之风姿，犹如古木之苍劲，历久弥新。",
        "小师妹之容貌，犹如古画之精美，令人赞叹。",
        "小师妹之气质，犹如古琴之悠扬，令人陶醉。",
        "小师妹之容颜，犹如古诗之韵味，令人回味无穷。",
        "小师妹之风姿，犹如古风之典雅，令人心向往之。",
        "小师妹之容貌，犹如古建筑之宏伟，令人叹为观止。",
        "小师妹之气质，犹如古道之悠长，令人心旷神怡。",
        "小师妹之容颜，犹如古书之智慧，令人受益匪浅。",
        "小师妹之风姿，犹如古剑之锋利，令人敬畏。",
        "小师妹之容貌，犹如古镜之明澈，令人自省。",
        "小师妹之气质，犹如古钟之悠扬，令人心旷神怡。",
        "小师妹之容颜，犹如古桥之坚固，令人安心。",
        "小师妹之风姿，犹如古塔之高耸，令人仰望。",
        "小师妹之容貌，犹如古井之深邃，令人探寻。",
        "小师妹之气质，犹如古树之苍劲，令人敬仰。",
        "大爱小师妹，小师妹yyds",
        "妖女，毁我徒儿道心,看剑",
        "北宋嘉祐元年，小师妹被皇帝赐白绫三尺",
        "大胆妖孽，大威天龙",
        "今日，贫道就替天行道，收了你这妖孽",
        "降服你这妖孽",
        "小师妹的古风装扮真是美轮美奂，仿佛穿越了时空。",
        "这曲古筝弹奏，让人心旷神怡，仿佛置身于古代山水之间。",
        "小师妹的舞姿轻盈，宛如仙子下凡。",
        "小师妹的书法作品，笔力遒劲，颇有古风韵味。",
        "小师妹的古风妆容，精致而不失自然。",
        "小师妹的古风舞蹈，动作优雅，韵味十足。",
        "小师妹的古风配饰，精致而又不失古朴。",
        "小师妹的古风服饰，设计独特，尽显古风韵味。",
        "小师妹的古风发型，简单大方，又不失古风特色。",
        "小师妹的古风手工艺品，精致而又不失实用。",
        "小师妹的古风配饰，精致而又不失古朴。",
        "小师妹的古风舞蹈，动作优雅，韵味十足。",
        "小师妹的古风配饰，精致而又不失古朴。",
        "我怎知今晚月色有多美，眼里早已全是姑娘，哪还容得下月色。",
        "我贪恋的人间烟花，不偏不倚都是你。",
        "一生一世一双人，半醉半醒半浮生。",
        "用我三生烟火，换你一世迷离。",
        "山有木兮木有枝，心悦君兮君不知。",
        "山河远阔，人间烟火，无一是你，无一不是你。",
        "拱手江山，为君一笑。",
        "一袭红衣染天下，只道离人徒悲伤。",
        "我遇见你，如舟靠岸，如鹿归林",
        "风铃吹，故人归，我在等风，也在等你",
        "许我浮生一世安，还你笑颜承你欢。",
        "你本无意穿堂风，偏偏孤倨引山洪。",
        "遥闻海水梦幽幽，君愁相思我亦愁",
        "一夜，小王爷听到些动静，从梦中惊醒，一把匕首闪着寒光抵在他脖子上，背后传来一名年轻女子的声音“别出声，否则我杀了你！",
        "来时芳华，去时白头，忘你不舍，寻你不休。",
        "李承鄞也是穷尽后半辈子在寻找忘川，好像一切都只是一场虚无缥缈的梦，不复存在，梦醒之后只有他一个人记得",
        "盼你渡口 待你桥头",
        "生命中最深沉的爱恋，最终仍是抵不过时间",
        "我爱一个人，爱了三千六百四十三年。",
        "因为得到他的爱，我曾认定自己是世上最幸福的姑娘，任何人都不能跟我比。",
        "就是如此任性，就是如此自信。",
        "记得那年情至深处，我曾对天发誓，要与他白首偕老，共度此生。",
        "他小心翼翼地把我搂在怀里说，不仅此生，要生生世世。",
        "他说的每一个字，我都无条件地相信。",
        "他说会生生世世爱我，永远陪在我的身边，他不会走，也不会变的。",
        "真是有些遗憾。后来他变了。",
        "三里清风三里路，步步风里再无你；十里桃花十里情，世世桃花无你名",
        "水有舟可渡，山有径可寻；所爱隔山海，山海皆可平",
        "愿陪你三生三世，一世枕边书，一世怀中猫，一世意中人",
        "他日故里定逢春，你我山巅自相逢",
        "有人劈经济掌，有人耍政治刀，你来我往，各凭技艺，人在江湖，身不由己",
        "汝为山河过客 却总长叹伤离别",
        "柳叶儿弯弯拂水花儿转，水花儿转转着小船儿摇，小船儿摇摇过石桥南，石桥南她撑伞步款款，款款入我心尖",
        "若今生长剑浣花，生死无涯。便许你来世雪底封刀，结庐为家。你可愿荆钗绾发，为我煮茶，明朝江湖饮马",
        "城南以南不再蓝，城北以北不再美；城中从此不再挤，心中从此再无你；南墙已撞，故事已忘",
        "灼灼桃花，三千繁华，却似人间只有一个她",
        "人世间有百媚千红，唯独你是我情之所钟",
        "若他年，有幸再逢桃花人面，望春风，不计前嫌",
        "愿你霜尘梦不朽，也有白月牵衣袖，也有春秋抚眉头",
        "你说 繁华的城市里无从归家 江南的烟雨绕梦仍牵挂 城南溪下少年不觉已白发",
        "彼岸花开开彼岸，忘川河畔亦忘川。奈何桥头空奈何，三生石上写三生",
        "小女子日日思君 眼里心里 提笔颂诗都是公子 你看 眉宇间也有公子的影子",
        "楼外晚樱花满树，怀中枯木不逢春。若得青山邀几步，也无风月也无尘",
        # "多一字恐失言 少一句情不够 扰了一时清净 乱了心上秋 最美四个字不过 如愿以偿 最负人也不过 自作多情 欢安长乐 素昧平生",
        # "南方是才子佳人，墙里佳人墙外笑，草长莺飞，小桥流水，梦里的诗意；北方是豪情万丈，朔风满天古战场，大漠孤烟，长河落日，男儿的向往",
        "错失了长安古意，失约了洛阳花期；我在姑苏马蹄莲里，瞥见你兰舟涉水而去",
        "我曾见月色轻挽风尘，亦听闻星河孤舟失沉 想来是你无意谪落凡尘，一笑黯淡了日月星辰",
        # "小女无才，未获君睐，扰之良久，望勿怪。君赴北余赴南，此生别过，却难忘。愿君春冬安暖，暮拾灯火天雨而覆伞。愿君善其身逢良人，暖色浮余生，好人伴语。众眷且止于齿，掩于岁月匿于来日。今世无缘于君，勿念。雨于芭蕉，奈其何哉",
        "眼见你喜上眉梢，我便无限欢愉，深觉春花秋月不如你，夏雨冬雪无所侵",
        # "一声红叶一声愁，此愁拆作，故人心上秋。一缕云烟一续愁，此愁分作，远人心上秋。一行雁阵一行愁，此愁散作，旅人心上秋。一地残红一地愁，此愁化作，离人心上秋",
        "长安尽头无故里 故里从此别长安",
        "人生相知，如杏花遇雨，如浊酒遇歌",
        "岁月如梭两鬓风，流年胭脂眉间红 再捋青丝浓雪染，不悔经年此相逢",
        "秋千水，竹马道，一眼见你，万物不及；春水初生，春林初盛，春风十里不如你",
        "姑凉，姓甚、名谁？芳龄几许？可有中意人家？小生不才，想借菇凉一生说话。菇凉意下如何？",
        "可叹惊鸿一瞥，误入眉眼，欢喜多年……",
        "写意东风事，笔迟句稍顿，忽觉语罢寄无人",
        "情不敢至深，恐大梦一场 卦不敢算尽，畏天道无常",
        # "思君如杨柳，何处不依依；思君如风雨，撩乱几时休；思君如蔓草，绵延不可穷；思君如皓月，夜夜减清辉；思君如绛蜡，寸念总成灰",
        "我可否娶你，从拜堂之礼到举案齐眉，绾青丝镜前，愿永世不离，居世外桃源",
        "山水一程我披发行吟，朝夕之间又走过晓风残月",
        "一念清心静，莲花处处开",
        "去去重去去，来时是来时",
        "笑对运气，更笑看人情",
        "花有重开日，人无再少年",
        "处处是遗憾，放下即自在",
        "交往如饮酒，尽兴便好，真心相待，何必计较",
        "人生何处不相逢，怕只怕重逢不识",
        "古人留故事中，情感随之流转",
        "人生在世，皆需自渡难关",
        "眼中世界未必真，言不由衷有时难免",
        "不爱非错，无需自责",
        "阳光下必有阴影，人生常态",
        "一念清心静 莲花处处开",
        "去去重去去，来时是来时",
        "这笑运气更笑人情",
        "花有重开日 人无再少年",
        "本处处都是遗憾，没有什么放不下的，也更没有什么解不开的结",
        "人与人之间的交往，就像这喝酒，杯杯盏盏，你来我往，喝得尽兴就好。",
        "我却忘了，我与你李莲花，早就交付过真心了，又何必斤斤计较，杯杯见底干净呢？",
        "人生何处不相逢，怕只怕重见之时，故人对面不相识",
        "既是古人，便让他留在故事里",
        "人生在世，皆在自渡",
        "有时候人不一定想说假话，只不过眼睛里看到的事，未必是真的而已。",
        "不爱一个人了，这并不是错，也不是需要自责的事。",
        "人站在阳光下，怎么可能没有阴影呢。",
        "一曲肝肠断，天涯何处觅知音。",
        "江湖之远，天下之大，在下只想一亲姑娘芳泽。",
        #请勿刷礼物
        "铁子们，不要点关注不用点赞，小礼物不需要送，谢谢了",
        "文明观猴 请勿投喂"
    ]

    # 随机选取一条评论
    selected_comment = random.choice(comments)
    # print(selected_comment)
    biaoqing=[
        "[赞]",
        "[比心]",
        "[看]",
        "[呲牙]",
        "[舔屏]",
        "[可怜]",
        "[干饭人]",
        "[撇嘴]",
        "[逞强落泪]",
        "[躺平]",
        "[鞠躬]",
        "[大哭]",
        "[做鬼脸]",
        "[candy]",
        "[色]",
              ]
    fayan_box.send_keys(selected_comment+random.choice(biaoqing))
    # fayan_box.send_keys("新年快乐，淀粉肠好吃，静公主好看[比心]")
    time.sleep(0.5)
    fayan_box.send_keys(Keys.ENTER)
    # fasongButton=driver.find_element(By.CSS_SELECTOR,'#island_4a5da > div > div.rXSKGskq > div > div > div.webcast-chatroom___input-container > svg')
    # time.sleep(1)
    # fasongButton.click()

def dianzan():
    # dianzanBox=driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[2]/div/div/div/div/div[1]/div/div[1]/div")
    # ActionChains(driver).double_click(dianzanBox).perform()
    for i in range(300):
        x = random.randrange(300, 550)
        y = random.randrange(400, 550)
        pyautogui.click(x, y)
        time.sleep(0.2)

if __name__ == '__main__':
    # num = input("请输入需要自动化操作的发送表情数:\n")
    # num = int(num)
    # print(num)
    # url="https://live.douyin.com/93173086668"

    # browser = webdriver.Chrome(executable_path=driver_path)
    # browser = webdriver.Chrome(service=service, options=Chrome_options)
    # urltext = "https://live.douyin.com/118502374491"
    # login2(urltext)
    # 加载之前保存的Cookie
    with open("douyin_cookie.pickle", 'rb') as file:
        cookies_list = pickle.load(file)
    # 打开抖音网站
    driver.get('https://www.douyin.com/')

    # 添加Cookie以实现持久登录
    for cookie in cookies_list:
        driver.add_cookie(cookie)
    driver.get('https://live.douyin.com/93173086668')
    # loginn()
    time.sleep(20)
    for i in range(1000):
        # driver_path = r'D:\software\python3.8\Scripts\chromedriver.exe'
        pinglun()
        # time.sleep(1)
        # dianzan()

        # driver.quit()

