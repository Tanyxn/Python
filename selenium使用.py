# from selenium import webdriver
#
# #实例化一个浏览器驱动
# chrome = webdriver.Chrome()
#
# #访问页面
# chrome.get("https://www.baidu.com/")
# #捕获元素
# inputs = chrome.find_element_by_id("kw")
# #对元素进行操作
# inputs.send_keys("老边饺子")
# button = chrome.find_element_by_id("su")
# button.click()
# #关闭浏览器
# chrome.close()
##########################################################
from selenium import webdriver
import time
chrome = webdriver.Chrome()
def qqzone():
    #访问页面
    chrome.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=https%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=https%3A//z.qzone.com/download.html&pt_no_auth=0")
    time.sleep(1)
    #捕获元素
    button = chrome.find_elements_by_class_name("face")
    #对元素进行操作
    button[0].click()
    time.sleep(1)
    button1 = chrome.find_element_by_id("aAppstore")
    button1.click()
    button2 = chrome.find_elements_by_class_name("my-app-list-item")
    print(button2.text)
qqzone()
# nongchang()
# time.sleep(100)
#关闭浏览器
# chrome.close()
