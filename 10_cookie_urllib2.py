# encoding: utf-8
import cookielib, urllib, urllib2

cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
values = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}
form_data = urllib.urlencode(values)
request = urllib2.Request("https://www.ptt.cc/ask/over18", data=form_data)
response = urlOpener.open(request)  

response = urlOpener.open("https://www.ptt.cc/bbs/Gossiping/M.1453982899.A.494.html")  
html = response.read()
print html
