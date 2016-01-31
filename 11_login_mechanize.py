# encoding: utf-8
import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open("https://www.linkedin.com/")
browser.select_form(nr=0)

browser["session_key"] = "帳號"
browser["session_password"] = "密碼"
response = browser.submit()

print response.read()