# encoding: utf-8
import urllib2

request = urllib2.Request("http://blog.marsw.tw")
response = urllib2.urlopen(request)
html = response.read()
print html

fileout = file("01_blog.html","w")
fileout.write(html)
fileout.close()
