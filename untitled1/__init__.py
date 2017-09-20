# import pymysql
# pymysql.install_as_MySQLdb()
#
# from django.db.models.signals import pre_save, post_save
# from mypizza import pizza_done
#
#
#
# def callback(sender, **kwargs):
#     print('xxoo_callback',sender, kwargs)
#
#
# pizza_done.connect(callback)
#
#
#
#
#
#
# def callback1(sender, **kwargs):
#     print('xxoo_callback',sender, kwargs)
#
# def callback2(sender, **kwargs):
#     print('xxoo_callback',sender, kwargs)
#
# def callback3(sender, **kwargs):
#     print('xxoo_callback',sender, kwargs)
#
# pre_save.connect(callback1)
# pre_save.connect(callback2)
# pre_save.connect(callback3)