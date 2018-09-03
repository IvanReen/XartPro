import json

from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin as admin

from art.models import Category, Art


def index(request):
    # 查询所有的一级分类
    cates = Category.objects.filter(parent=None).all()

    # 查询所有文章Art
    # 获取请求参数的p_cate  一级分类
    p_cate = request.GET.get('p_cate', '')
    if p_cate:
        p_cate = int(p_cate)
        arts = Art.objects.filter(category__parent_id=p_cate).all()
    else:
        arts = Art.objects.all()

    # 实现Art文章的分页
    # 获取请求参数的page页码
    page = request.GET.get('page', '1')

    paginator = Paginator(arts, 10)  # 分页器
    pager = paginator.page(int(page))  # 读取第一页的数据

    # 查询登录用户信息
    if 'login_user' in request.session:
        login_user = json.loads(request.session.get('login_user'))

    return render(request, 'index.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^art/', include('art.urls')),
    url(r'', index),
]
