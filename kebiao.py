import requests
from bs4 import BeautifulSoup

login_url = "http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp"

username = ''
password = ''

headers = {	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate",
			"Accept-Language":"zh-CN,zh;q=0.8",
			"Cache-Control":"max-age=0",
			"Connection":"keep-alive",
			"Content-Type":"application/x-www-form-urlencoded",
			"DNT":"1",
			"Host":"ids.xidian.edu.cn",
			"Origin":"http://ids.xidian.edu.cn",
			"Referer":"http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp",
			"Upgrade-Insecure-Requests":"1",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"}

s = requests.Session()
r = s.get(login_url)
data = r.text
login = BeautifulSoup(data, "html.parser")

lt_ = 'input[name ="lt"]'
execution_ = 'input[name="execution"]'
_eventId_ = 'input[name="_eventId"]'
rmShown_ = 'input[name="rmShown"]'



lt = login.find(attrs={"name": "lt"})['value']
execution = login.find(attrs={"name": "execution"})['value']
_eventId = login.find(attrs={"name": "_eventId"})['value']
rmShown = login.find(attrs={"name": "rmShown"})['value']
params = {	'username': username, 
			'password': password,
			"submit": "", 
			"lt": lt, 
			"execution": execution,
			"_eventId": _eventId, 
			"rmShown": rmShown}

s.post('http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp', data=params, headers=headers)
s.get("http://jwxt.xidian.edu.cn/caslogin.jsp")
r = s.get("http://jwxt.xidian.edu.cn/xkAction.do?actionType=6")
lists = BeautifulSoup(r.text, "html.parser")

names = lists.findAll("tr", {"bgcolor":"#FFFFFF"})
print len(names)
n = 0
ll = [0,2,5,7,10]
#for x in xrange(1,10):
for x in ll:
	print names[x].get_text()
