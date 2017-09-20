from django.shortcuts import render,HttpResponse
from app01 import models
from django.views.decorators.cache import cache_page
import time


def index(request):
    # user_list = models.UserInfo.objects.all()
    # models.UserInfo.objects.create()
    # obj = models.UserInfo()
    # obj.save()
    # models.UserInfo.objects.create(name='alex',pwd='123')
    #
    # # 自定制操作，触发pizza_done信号
    # from mysignal import pizza_done
    # pizza_done.send(sender='seven', toppings=request, size=456)

    # ctime = time.time()

    # [obj,obj,obj]
    # 查询用户表models.UserInfo.objects.all() 1000
    # 把用户表中所有的ut_id拿到, 用户类型ID [1,2,3]
    # select * from UsetType where id in [1,2,3]
    # user_list = models.UserInfo.objects.all().prefetch_related('ut')
    # for row in user_list:
    #     print(row.name, row.pwd, row.ut.caption)



    # for row in user_list:
    #     print(row.name,row.pwd,row.ut.caption)
    #
    # # [{},{},{}]
    # user_list = models.UserInfo.objects.values('name','pwd','ut__caption')
    # for row in user_list:
    #     print(row['name'],row['pwd'],row['ut__caption'])

    # [obj,obj,obj]
    # user_list = models.UserInfo.objects.all().only('name')
    user_list = models.UserInfo.objects.all().defer('name')
    for row in user_list:
        print(row.pwd)


    return render(request,'index.html',{'user_list':user_list})

import json
def get_data(request):


    # 方案一：
    # queryset[UserInfo对象,]
    # user_list = models.UserInfo.objects.all()
    # from django.core import serializers
    # user_list_str = serializers.serialize("json", user_list)
    # return HttpResponse(user_list_str)
    # 方案二：
    # querset=[{},{},{}]
    user_list = models.UserInfo.objects.values('name','pwd')
    user_list = list(user_list)
    val = json.dumps(user_list,cls=json.JSONEncoder)
    return HttpResponse(val)


def test(request):
    # user_list = models.UserInfo.objects.all()
    ctime = time.time()
    return render(request,'test.html',{'ctime':ctime})

"""
# for i in range(300):
    #     models.UserInfo.objects.create(name='高旭%s' %i, pwd='gaoxu3714%s' %i)
    # return HttpResponse('...')
"""
from utils.page import Pagination
def users(request):
    current_page = int(request.GET.get('page',1))

    total_item_count = models.UserInfo.objects.all().count()
    # page_obj = Pagination(current_page,total_item_count,request.path_info)
    page_obj = Pagination(current_page,total_item_count,'/users.html')

    user_list = models.UserInfo.objects.all()[page_obj.start:page_obj.end]

    return render(request,'users.html',{'user_list':user_list,'page_html':page_obj.page_html()})


