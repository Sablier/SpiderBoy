import os
import urllib.request
import re


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html



def find_imgs(url):

    html = url_open(url)
    html = str(html)
    
    # img_addr_list = []

    # a = html.find('<a target="_blank" ')

    # while a != -1:
    #     b = html.find('.html',a,a+100)
    #     if b != -1:
    #         img_path = html[a+40:b+5]  
    #         img_des = html[a+48:a+58]# maybe 41
    #         img_addr_list.append([img_path,img_des])
    #     else:
    #         b = a + 10
    #     a = html.find('<a target="_blank" ',b) # 将b的位置向后移动一点，然后从b开始下一轮寻找

    # for each in img_addr_list:
    #     if each[0].startswith('/') == False:
    #         each[0] = '/' + each[0]
    #     if each[1].startswith('/') == True:
    #         each[1] = each[1][1:]
    

    # <a target="_blank" id="2880x1800" href="/showpic/2880x1800_92196_13.html">2880x1800</a>
    # <a target="_blank" id="1366x768" href="/showpic/1366x768_92196_13.html" class="current" title="您当前的屏幕分辨率是：1366x768">1366x768</a>
    
    # pattern = re.compile(r'<a.*?id="\d{3,4}x\d{3,4}" href="(.*?)".*?>.*</a>') 
    # img_addr = re.findall(pattern,html) 

    # 使用search方法，只返回找到的第一组值，即最大的分辨率
    pattern = re.compile(r'target=.*?id="(\d{3,4}x\d{3,4})" href="(.*?)".*?</a>')
    res = re.search(pattern,html)
    img_addr = res.group(1,2)
    print(img_addr)

    return img_addr



def find_imgs_2(img_addr):

    img_url = 'http://desk.zol.com.cn' + img_addr[1]
    img_page = url_open(img_url)
    img_page = str(img_page)
    # a = img_page.find('<img src="')
    # b = img_page.find('.jpg',a,a+500)
    # img_addr = img_page[a+10:b+4] # 可能是b+5 a+16
    pattern2 = re.compile(r'<img.*? src="(.*?)"')
    img_addr2 = re.findall(pattern2,img_page)
    img_addr_info = (img_addr[0],img_addr2[0])

    print(img_addr_info)
    return img_addr_info



def save_imgs(path,name,img_addr_info):

    picture = url_open(img_addr_info[1])
    print("saving picture %s" % img_addr_info[1])

    with open( path + str(name) + "_" + img_addr_info[0] + ".jpg" ,"wb") as file:
        file.write(picture)
    print()


def main():

    path = "C:/Users/BiaobiaoPeng/Desktop/spiderboy/imgs-neir-RE2/"
    
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        os.chdir(path)
		
    url_static = "http://desk.zol.com.cn/bizhi/7433_921"

    for number in range(83,97):
        page_url = url_static + str(number) + "_2.html"
        img_addr1 = find_imgs(page_url)
        img_addr_info = find_imgs_2(img_addr1)
        save_imgs(path, number, img_addr_info)

if __name__ == '__main__':
    main()