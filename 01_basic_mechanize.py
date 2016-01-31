# encoding: utf-8
import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
response = browser.open("http://blog.marsw.tw")
html = response.read()
print html

fileout = file("01_blog.html","w")
fileout.write(html)
fileout.close()
