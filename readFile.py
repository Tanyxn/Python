
# from time import sleep
# from selenium import webdriver
#
# def getFile(url):
#     #实例化一个浏览器驱动
#     chrome = webdriver.Chrome()
#
#     #访问页面
#     chrome.get(url)
#     #捕获元素
#
#     texts = chrome.find_elements_by_xpath("//div[@class='content']/p")
#     for t in texts:
#         print(t.text)
#     sleep(1)
#     next_url = chrome.find_elements_by_xpath("//a[@class='nextchapter']")
#     if next_url:
#         next_urls = next_url[0].get_attribute("href")
#         getFile(next_urls)
#     else:
#         chrome.close()
#         return
#     #关闭浏览器
##################################################################

from time import sleep
from selenium import webdriver

def getFile(chrome, url):
    #实例化一个浏览器驱动
    #访问页面
    chrome.get(url)
    #捕获元素
    texts = chrome.find_elements_by_xpath("//div[@class='bg']/h1")
    textcont = chrome.find_elements_by_xpath("//div[@class='content-body']/p")
    # print(texts,textcont)
    with open("1.txt","a") as f:
        f.write(texts[0].text+"\n")
        for i in textcont:
            f.write(i.text + "\n")
    sleep(1)
    next_url = chrome.find_elements_by_xpath("//a[@id='xiayipian']")
    if next_url:
        next_urls = next_url[0].get_attribute("href")
        # print(next_urls)
        getFile(chrome,next_urls)
    else:
        chrome.close()
        return
    #关闭浏览器
if __name__ == '__main__':
    chrome = webdriver.Chrome()
    getFile(chrome, "http://seputu.com/biji2/127.html")
