# 系统(内置)模块
import os

import xadmin  # 第三方模块
from xadmin import views


from art.models import Tag, Category, Art, RollSet, Chapter  # 自定义模块

# Register your models here.


class BaseSettings:  # 设置admin的站点样式
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '创意小说'
    site_footer = '西安小城Py爱好者2<h4>联系方式：17791692095</h4>'
    menu_style = 'accordion'
    # global_search_models = (Tag,)
    apps_label_title = {
        'art': '文章管理'   # 应用名：'应用标题'
    }
    apps_icons = {
        'art': 'glyphicon glyphicon-book'
    }
    global_models_icon = {
        Tag: 'glyphicon glyphicon-tags'
    }


xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)


class TagAdmin:
    list_display = ('name', 'describe', 'add_time')
    list_per_page = 10  # 每页显示的记录数
    list_filter = ('add_time', )  # 过滤字段-查询数据的条件
    search_fields = ('name', 'describe')  # 搜索字段


class CategoryAdmin:
    list_display = ('title', 'add_time')
    list_per_page = 10  # 每页显示的记录数


class ArtAdmin:
    list_display = ('title', 'summary', 'author', 'category', 'tags')
    list_per_page = 10  # 每页显示的记录数


class RollAdmin:
    list_display = ('name', 'free_level_name', 'art')
    list_per_page = 10  # 每页显示的记录数


class ChapterAdmin:
    list_display = ('name', 'roll', 'publish_date')
    list_per_page = 10  # 每页显示的记录数

    # 设置指定字段的样式
    style_fields = {'content': 'ueditor'}


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Art, ArtAdmin)

xadmin.site.register(RollSet, RollAdmin)
xadmin.site.register(Chapter, ChapterAdmin)

