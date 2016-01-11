# encoding: utf-8
import urllib2
from lxml import etree

from HTMLParser import HTMLParser
class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	try:
		s = MLStripper()
		s.feed(html)
		return s.get_data()
	except:
		return html

request = urllib2.Request("http://blog.marsw.tw/2013/04/blog-post_9395.html")
response = urllib2.urlopen(request)
html = response.read()

page = etree.HTML(html)

fileout1 = file('06_v1.txt','w')
fileout1.write(("".join(page.xpath(u"//div[@class='post-body entry-content']/descendant::text()"))).encode('utf8'))
fileout1.close()

fileout2 = file('06_v2.txt','w')
fileout2.write(("".join(page.xpath(u"//div[contains(@class, 'post-body')]/descendant::text()"))).encode('utf8'))
fileout2.close()

raw_html = etree.tostring(page.xpath(u"//div[contains(@class, 'post-body')]")[0], pretty_print=True,encoding='UTF-8')
text = strip_tags(raw_html)
fileout3 = file('06_v3.txt','w')
fileout3.write(text)
fileout3.close()