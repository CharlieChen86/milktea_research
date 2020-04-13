import requests
from selenium import webdriver
import time
from lxml import etree
import re
import random

def loginWeibo(username, password):
    driver.get('https://passport.weibo.cn/signin/login')
    time.sleep(3)

    driver.find_element_by_id("loginName").send_keys(username)
    driver.find_element_by_id("loginPassword").send_keys(password)
    driver.find_element_by_id("loginAction").click()
    time.sleep(15)
    
    cookies = driver.get_cookies()
    print(cookies)
    driver.close()
    return cookies
def visitUserInfo(userId):
    res=sess.get('http://weibo.cn/' + userId)

    print('********************')   
    print('用户资料')
    
    # 0.etree
    tree=etree.HTML(res.content)

    # 1.用户id
    print('用户id:' + userId)

    # 2.用户昵称
    strlist = tree.xpath("//div[@class='ut']//text()")
    nickname = strlist[0]
    print('昵称:' + nickname)
    
    # 3.微博数、粉丝数、关注数
    strCnt = ' '.join(tree.xpath("//div[@class='tip2']//text()"))
    pattern = r"\d+\.?\d*"      # 匹配数字，包含整数和小数
    cntArr = re.findall(pattern, strCnt)
    print(strCnt)
    print("微博数：" + str(cntArr[0]))
    print("关注数：" + str(cntArr[1]))
    print("粉丝数：" + str(cntArr[2]))
    
    print('\n********************')
    # 4.将用户信息写到文件里
    with open("userinfo.txt", "w", encoding = "gb18030") as file:
        file.write("用户ID：" + userId + '\r\n')
        file.write("昵称：" + nickname + '\r\n')
        file.write("微博数：" + str(cntArr[0]) + '\r\n')
        file.write("关注数：" + str(cntArr[1]) + '\r\n')
        file.write("粉丝数：" + str(cntArr[2]) + '\r\n')
        
    
def visitWeiboContent(userId):
    # 0.etree
    r=sess.get('http://weibo.cn/' + userId)
    tr=etree.HTML(r.content)

    pageList = ' '.join(tr.xpath("//div[@class='pa']//text()"))
    print(pageList)
    pattern = r"\d+\d*"         # 匹配数字，只包含整数
    pageArr = re.findall(pattern, pageList)
    totalPages = pageArr[1]     # 总共有多少页微博
    print(totalPages)
    
    pageNum =1                 # 第几页
    numInCurPage = 1            # 当前页的第几条微博内容
    curNum = 0                  # 全部微博中的第几条微博
    contentPath = "//div[@class='c'][{0}]//text()"
    #while(pageNum <= 3):   
    while(pageNum <= int(totalPages)):
        with open('status.txt','w',encoding='utf-8') as f:
            f.write('pageNum:'+str(pageNum)+'\nnumInCurPage: '+str(numInCurPage)+'\n curNum: '+str(curNum))
        try:
            contentUrl = "http://weibo.cn/" + userId + "?page=" + str(pageNum)
            res=sess.get(contentUrl)

            # 0.etree
            tree=etree.HTML(res.content)

            content = ' '.join(tree.xpath(contentPath.format(numInCurPage)))
            #print("\n" + content)                  # 微博内容，包含原创和转发
            if "隐私" not in content and '皮肤' not in content and '触屏' not in content and len(content)>5:
                numInCurPage += 1
                curNum += 1
                with open("weibocontent.txt", "a", encoding = "gb18030") as file:
                    file.write(str(curNum) + '\r\n' + content + '\r\n\r\n') 
            else:
                pageNum += 1                        # 抓取新一页的内容
                numInCurPage = 1                    # 每一页都是从第1条开始抓
                time.sleep(random.randrange(3,5))                      # 要隔20秒，否则会被封
        except Exception as e:
            print("curNum:" + str(curNum))
            print(e)
            time.sleep(random.randrange(10,30))
        finally:
            # print("unexpected error")
            pass
    print("Load weibo content finished!")       


driver = webdriver.Chrome()
# 打开网站
# 获取cookies
username = ''             # 输入微博账号
password = ''             # 输入密码
selenium_cookies = loginWeibo(username, password)      # 要先登录，否则抓取不了微博内容

sess = requests.session()

tmp_cookies = requests.cookies.RequestsCookieJar()

for item in selenium_cookies:
    tmp_cookies.set(item["name"], item["value"])

sess.cookies.update(tmp_cookies)

# 这时候使用的就是同一个cookies了。
# res=sess.get('http://weibo.cn/starbucks')
# with open('breq.html','wb') as f:
#     f.write(res.content)
#     print(res.text)
# with open('ureq.html','w',encoding='utf-8') as f:
#     f.write(res.content.decode('utf-8'))
#     print(res.text)

uid = ''                       # 爬取微博用户的ID
visitUserInfo(uid)                  # 获取用户基本信息
visitWeiboContent(uid)              # 获取微博内容