from django.shortcuts import render
from .models import *
from .DealPic import Excel
from .DealURL import getHtml
from .DealURL import getImg
from django.db import connection
def localDetect(request):
    if request.method == 'POST':
        global i #引入全局变量i来判断时机清空数据表，以便本地上传检测功能多次使用
        if i == 0:
            cursor = connection.cursor()
            # 要想使用sql原生语句，必须用到execute()函数
            # 然后在里面写入sql原生语句
            sql = "truncate table img_db_img"
            cursor.execute(sql)
            i = i + 1
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
        Excel(new_img.name)#  处理图片的方法  这里就是而接口，接入你的方法
        imgs = IMG.objects.all()
        content = {
            'imgs': imgs,
        }
        for i in imgs:
            print(i.img.url)
        return render(request, 'img_tem/localdetecting.html', content)
    if request.method =='GET':
        imgs = IMG.objects.all()
        content = {
            'imgs': imgs,
        }
        i = 0
        return render(request, 'img_tem/localdetected.html',content)
# @csrf_exempt
def homeIndex(request):
    cursor = connection.cursor()
    # 要想使用sql原生语句，必须用到execute()函数
    # 然后在里面写入sql原生语句
    sql = "truncate table img_db_img"
    cursor.execute(sql)
    return render(request, 'img_tem/homeIndex.html')
def crawlDetect(request):
    if request.method =='POST':
        cursor = connection.cursor()
        # 要想使用sql原生语句，必须用到execute()函数
        # 然后在里面写入sql原生语句
        sql = "truncate table img_db_img"
        cursor.execute(sql) #处理url路径之前，先清空数据表
        html = getHtml(request.POST.get('url'))
        getImg(html)
    imgs = IMG.objects.all()
    content = {
        'imgs': imgs,
    }
    return render(request, 'img_tem/crawldetected.html',content)