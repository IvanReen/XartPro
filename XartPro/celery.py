from celery import Celery

import os

# 设置环境变量 DJANGO_MODULE_SETTINGS
from XartPro import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'XartPro.settings')

app = Celery('XArtCelery')

app.config_from_object('django.conf:settings')

# 从所有已配置的 app模块中扫描 task任务声明函数
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)



