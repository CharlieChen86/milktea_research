import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块
import  jieba                    #jieba分词

f=open('xc_data.csv','r',encoding='gb18030')
# 新店
# p=r'喜茶\S{2,3}[新]店'
#2019联名
ps=['太平鸟','BOBAROOM','Lee','缸鸭狗','老三祥','杜蕾斯','roseonly','电台巷火锅','美珍香','徐福记','柠檬美食',\
	'阿华田','美团外卖','oatly','七喜','新浪','芝麻街','微光','厦门晚报','科罗娜啤酒','平安信用卡','Stanley',\
	'养乐多','TRB西餐厅','太二','娇韵诗','广州大剧院','AAPE','奥利奥','出前一丁','国际爵士音乐节','buddyblue',\
	'简单生活节','nike','能猫商店','@百戏局BAIXIJU','kiehls','adidas','广州大剧院','草莓音乐节','cheery',\
	'红树林基金会','m豆','好利来','茶之路','文创里','妙手回潮','绿洲','木木艺术社区','中国邮政']
#2018联名
ps=['BDuck','澳大利亚昆士兰旅游','唐人街探案','emoji礼盒','nike','@木九十MUJOSH','倩碧','musicanvas',\
	'gk电子俱乐部','国际设计周','百雀羚','大英博物馆','乐事','广发信用卡','LCM','Lucky','INNERSECT','桂格']



count=0
s=''
dic={}
for line in f:
	if(len(line)<5 or line[0]=='like'): continue
	text=line.split(',')
	# print(text[4][0:4])
	# print(text[5])
	# print(p)
	if(text[4][0:4]=='2018'):
		for p in ps:
			# print(p)
			i=re.search(p,text[5])

			if (i): 
				count+=1

				print(i.group(0))
				s=s+i.group(0)+' '
				try:
					dic[i.group(0)]=dic[i.group(0)]+1
				except:
					dic[i.group(0)]=1
		# print(i)
print(count)
# print(dic)
# exit(1)
wordcloud = WordCloud(
   #设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
   font_path="C:/Windows/Fonts/simfang.ttf",
   #设置了背景，宽高
   background_color="white",width=1000,height=880).generate(s)
# plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
