import urllib
import urllib2


url = "https://www.qiushibaike.com/hot/page/2/"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"
refer = ""
headers = {"User-Agent": user_agent,"Referer": refer}
values = {"username": "xxxxx", "password": "xxxxx"}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()
print page
