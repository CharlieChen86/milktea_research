# 网红奶茶店代码与数据集

## 代码
### 测试环境及已安装模块
语言
- Python 3.6

模块
- selenium
- Requests
- lxml
- csv
- wordcloud
- jieba
- matplotlib
- re
- time 
- random

其他
- chromedriver & Chrome

### 代码简介及使用方法
#### rapid_req.py
##### 介绍
抓取微博特定用户的所有可见推文
##### 运行前
- 账号信息：username & password 两个变量  
- 爬取用户的ID：uid  
##### 运行后
1. 一个浏览器会自动打开，并输入账户和密码
2. 如果出现验证码，请手动点击验证码已通过验证
3. 浏览器将自动关闭
##### 保存的文件
- userinfo.txt：微博用户的基本信息
- weibocontent.txt 每条微博推文的信息
- status.txt 当前爬取状态信息，用于调试

#### data.py
##### 介绍
将抓取到的微博推文信息（txt文件）解析并输出为csv文件
##### 运行前
- fileobj：保存文件名（csv）
- f：读入文件名（txt）
##### 运行后
- 程序将自动运行
##### 保存的文件
- 运行前设定的文件名

#### word_cloud.py
##### 介绍
用于制作词云

## 数据
### 打开方式
建议使用记事本打开，用excel打开有可能乱码（处理乱码方式见网上资料）。
### xc_data.csv
喜茶的数据
### cy_data.csv
茶颜悦色的数据
