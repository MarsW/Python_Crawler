# encoding: utf-8
import urllib2
from lxml import etree

request = urllib2.Request("http://blog.marsw.tw")
response = urllib2.urlopen(request)
html = response.read()

page = etree.HTML(html)

print "v1-------"
for i in page.xpath(u"//h5/a"):
	print i.text

print "v2-------"
for i in page.xpath(u"//h5/a/text()"):
	print i

print "v3-------"
for i in page.xpath(u"//article/header/h5/a/text()"):
	print i

print "v4-------"
for i in page.xpath(u"//article"):
	print i.xpath(u"descendant::h5/a/text()")[0]
	