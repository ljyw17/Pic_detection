import urllib.request
import re
import urllib
from .models import IMG
from .DealPic import Excel
#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')
def getImg(html):
    reg = r'src="(.*?\.(?:jpg|jpeg|gif|bmp|png))"' #有些情况可能需要修改正则表达式
    imgre = re.compile(reg) #转换成一个正则对象
    imglist = imgre.findall(html) #表示在整个网页中过滤出所有图片的地址，放在imglist中
    x = 0 #声明一个变量赋值
    # path = 'H:\\python lianxi\\zout_pc5\\test' #设置保存地址media\img\\
    path = 'media\img'
    paths = path+'\\'
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{0}{1}.jpg'.format(paths,x)) #打开imglist，下载图片保存在本地，
    #format格式化字符串
        new_img3 = IMG(
            img="img\\" + '{0}.jpg'.format(x),
            name='{0}.jpg'.format(x)
        )
        new_img3.save()
        Excel('{0}.jpg'.format(x))
        x = x + 1