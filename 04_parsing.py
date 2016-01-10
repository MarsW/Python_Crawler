# encoding: utf-8
import urllib2
from lxml import etree

request = urllib2.Request("http://blog.marsw.tw")
response = urllib2.urlopen(request)
html = response.read()

page = etree.HTML(html)
for url in page.xpath(u"//img/@src"):
	if url.startswith("http:") and (url.endswith("JPG") or url.endswith("jpg") or url.endswith("png") or url.endswith("jpeg")) :
		print url
		
		try:
			img_request = urllib2.Request(url)
			img_response = urllib2.urlopen(img_request)
			img = img_response.read()
		except:
			continue

		count = count+1
		filename = str(count)+".jpg"
		pic_out = file(filename,'w')
		pic_out.write(img)
		pic_out.close()
