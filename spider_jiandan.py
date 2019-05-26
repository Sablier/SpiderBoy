"""使用面向对象思想编程。使用selenium包获取html内容，使用BeautifulSoup解析网页"""

import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


class GetJandan(object):
    def __init__(self, path, page=10):
        self.start_url = 'http://jandan.net/ooxx'
        self.url = ""
        self.save_path = path
        self.page = page

    def get_html(self, url):
        browser = webdriver.Chrome()
        browser.get(url)
        print("get", url)
        return browser.page_source

    def get_1stpage(self):
        "打印首页用来测试选择器，获取页码数，所以直接使用selenium包手写元素获取代码"
        browser = webdriver.Chrome()
        browser.get(self.start_url)
        target = browser.find_element_by_xpath('//span[@class="current-comment-page"]')
        first_page = target.text
        first_page = eval(first_page)[0]
        print("first page is %s" % first_page)
        browser.close()
        return first_page

    def search_img_url(self, html):
        url_list = []
        soup = BeautifulSoup(html, 'lxml')
        # for img_url_tag in soup.find_all('img'):
        #     img_urls = img_url_tag.find_all(atrrs={"referrerpolicy": "no-referrer"})
        #     for each in img_urls:
        #         img_url = each.img['src']
        #         print(img_url)
        #         url_list.append(img_url)
        tags = soup.find_all(name='img', attrs={"referrerpolicy": "no-referrer"})
        for tag in tags:
            url = tag.get('src')
            url_list.append(url)
        return url_list

    def visit_page(self, first_page):
        url_list = []
        for i in range(self.page):
            page_num = first_page - i
            url = "http://jandan.net/ooxx/page-" + str(page_num) + "#comments"
            print('start getting page: ', url)
            html = self.get_html(url)
            list = self.search_img_url(html)
            url_list += list
        return url_list

    def get_img(self,url_list):
        file_num = 0
        for url in url_list:
            file_name = str(file_num) + ".jpg"
            url = "http:" + url
            response = requests.get(url)
            picture = response.content
            self.save(picture,file_name)
            file_num += 1


    def save(self, file, name):
        with open(path + name, "wb") as f:
            f.write(file)
        print("save picture %s" % name)

    def run(self):
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)
        else:
            os.chdir(self.save_path)

        first_page = self.get_1stpage()
        url_list = self.visit_page(first_page)
        self.get_img(url_list)


if __name__ == '__main__':
    path = "C:/Users/BiaobiaoPeng/Desktop/python/projects/demoHTTP/images-jandan/"
    page = 3
    jandan = GetJandan(path, page)
    jandan.run()
