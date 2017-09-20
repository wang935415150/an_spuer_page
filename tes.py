from django.db.models.signals import pre_save, post_save


def callback1(sender, **kwargs):
    print('xxoo_callback',sender, kwargs)

def callback1(sender, **kwargs):
    print('xxoo_callback',sender, kwargs)
pre_save.connect()