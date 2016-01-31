# encoding: utf-8
import urllib2

url = "http://www.besttour.com.tw/web/detail_page.asp?travel_no=CJU04GE160210JZ"
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")
response = urllib2.urlopen(request)
html = unicode(response.read(),'Big5','ignore').encode('utf8')

print html
