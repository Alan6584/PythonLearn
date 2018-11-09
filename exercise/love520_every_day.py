# import itchat
import time
import datetime
import requests
import re
import os

 
def send_news():
    # 计算相恋天数
    inLoveDate = datetime.datetime(2016, 3, 21) # 相恋的时间
    todayDate = datetime.datetime.today()
    inLoveDays = (todayDate - inLoveDate).days
 

    print inLoveDays
    print girlfriend
 
    '''
    itchat.auto_login(hotReload=True) # 热启动，不需要多次扫码登录
    my_friend = itchat.search_friends(name=u'你的好友名称')
    girlfriend = my_friend[0]["UserName"]
    print(girlfriend)
    message = """
    亲爱的{}:
 
    早上好，今天是你和 Alan 相恋的第 {} 天~
 
    今天他想对你说的话是：
 
    {}
 
    最后也是最重要的！
    """.format("你的好友名称", str(inLoveDays), love_word)
    itchat.send(message, toUserName=girlfriend)
 
    files = os.listdir(pic_path)
    file = files[inLoveDays]
    love_image_file = "D:\\img\\" + file
    try:
        itchat.send_image(love_image_file, toUserName=girlfriend)
    except Exception as e:
        print(e)
    '''
 
def main():
 
 '''
    with open(love_word_path, 'r') as file:
        if file.read():
            print("exit")
        else:
            crawl_Love_words()
 
    pic_path = os.getcwd() + '\img'

    print pic_path
    foler = os.path.exists(pic_path)
 
    if not foler:
        crawl_love_image()
    else:
        print("情话图片已存在")
    '''
    send_news()
 
 
if __name__ == '__main__':
    while True:
        curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        love_time = curr_time.split(" ")[1]

        print("爱你的每一天都是如此美妙，现在时间：" + love_time)
        main()
        '''
        if love_time == "22:46:01":
            main()
            time.sleep(60)
        else:
            print("爱你的每一天都是如此美妙，现在时间：" + love_time)
        '''