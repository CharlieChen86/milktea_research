import csv
import re
fileobj=open('.csv','w',encoding='gb18030')#保存文件名，后缀为.csv
cwriter=csv.writer(fileobj, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
cwriter.writerow(['like','for','com','sum','date','content'])
f=open('.txt','r',encoding='gb18030')#读取文件名，后缀为.txt
i=0
for line in f:
	if(len(line)<10): continue
	text=line.strip()
	text=text.replace('?','')
	text=text.replace('"','')
	text=text.replace(',',' ')
	like=re.compile(r'\b赞\[\d+\]').findall(text)
	forw=re.compile(r'\b转发\[\d+\]').findall(text)
	comm=re.compile(r'\b评论\[\d+\]').findall(text)
	if(len(like)+len(forw)+len(comm) < 3):
		print('unexpected text (like,forw,comm):',text)
		# 
		continue
	like=int(like[-1][2:-1])
	forw=int(forw[-1][3:-1])
	comm=int(comm[-1][3:-1])
	# print(like,forw,comm)
	if(-1 != text.find("抱歉")):
		continue
	text=text.replace('转发了','')
	text=text.replace('发布了','').strip()

	pos2 = len(text)
	# if(-1 != text.find("http")):
	# 	pos2 = text.find("http")        
	if(-1 != text.find("全文")):
		pos2 = text.find("全文")
	elif(-1 != text.find("[ 组图共")):
		pos2 = text.find("[ 组图共")
	elif(-1 != text.find("原图")):
		pos2 = text.find("原图")
	elif (-1 != text.find("赞")):
		pos2 = text.find("赞")
	elif(-1 != text.find("地址")):
		pos2 = text.find("地址")
	# exit(1)
	content = text[0 : pos2].strip()
	# print(content)
	# print()



	date=re.compile(r'\d{4}-\d{2}-\d{2}').findall(text)
	if(len(date)==1):
		date=date[0]
	elif(len(date)>1):
		print("find more than 1 date in yyyy/mm/dd")
		
	else:
		date=re.compile(r'\d{2}月\d{2}日').findall(text)
		if(len(date)==1):
			date='2020-'+date[0][0:2]+'-'+date[0][3:5]
		elif(len(date)>1):
			print("find more than 1 date in mm/dd")
			
		else:
			date=re.compile(r'今天').findall(text)

			if(len(date)==1):
				date='2020-04-09'
			elif(len(date)>1):
				print("find two dates in 今天")
			else:
				print('cannot find date')
	# print(date)

	wr=[like,forw,comm,like+forw+comm,date,content.strip('\n')]
	cwriter.writerow(wr)
	i+=1
	continue

print(i)
fileobj.close()