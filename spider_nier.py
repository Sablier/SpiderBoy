import os
import urllib.request


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def find_imgs(url):

    html = url_open(url)
    html = str(html)
    img_addr_list = []

    a = html.find('<a target="_blank" ')

    while a != -1:
        b = html.find('.html',a,a+100)
        if b != -1:
            img_path = html[a+40:b+5]  
            img_des = html[a+48:a+58]# maybe 41
            img_addr_list.append([img_path,img_des])
        else:
            b = a + 10
        a = html.find('<a target="_blank" ',b) # 将b的位置向后移动一点，然后从b开始下一轮寻找

    for each in img_addr_list:
        if each[0].startswith('/') == False:
            each[0] = '/' + each[0]
        if each[1].startswith('/') == True:
            each[1] = each[1][1:]
        
    print(img_addr_list)
    return img_addr_list


def find_imgs_2(img_addr_list):
    img_addr_list2 = []
    for each in img_addr_list:
        img_url = 'http://desk.zol.com.cn' + each[0]
        img_page = url_open(img_url)
        img_page = str(img_page)
        a = img_page.find('<img src="')
        b = img_page.find('.jpg',a,a+500)
        img_addr = img_page[a+10:b+4] # 可能是b+5 a+16
        img_addr_list2.append([img_addr,each[1]])
    print(img_addr_list2)
    return img_addr_list2



def save_imgs(path,name,img_addr_list2):
    for each in img_addr_list2:
        img_url = each[0]
        picture = url_open(img_url)
        print("saving picture %s" % str(each[0]))
        with open( path + str(name) + '_'+ each[1] + ".jpg" ,"wb") as file:
            file.write(picture)
    print()


def main():

    path = "C:/Users/BiaobiaoPeng/Desktop/spiderboy/imgs-neir/"
    os.chdir(path)
    url_static = "http://desk.zol.com.cn/bizhi/7433_921"

    for number in range(83,97):
        page_url = url_static + str(number) + "_2.html"
        img_addr_list = find_imgs(page_url)
        img_addr_list2 = find_imgs_2(img_addr_list)
        # save_imgs(path, number, img_addr_list2)

if __name__ == '__main__':
    main()