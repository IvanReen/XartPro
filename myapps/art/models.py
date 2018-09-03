import uuid

import os
from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class Tag(models.Model):
    # name, describe, add_time
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='标题')
    describe = models.CharField(max_length=100,
                                verbose_name='描述')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:  # 元信息－描述模型类的信息(ORM)
        db_table = 't_tag'  # 类对应 数据库中表的名称
        verbose_name = '标签'  # 在后台显示模型类的名
        verbose_name_plural = verbose_name  # 后台复数的显示内容
        ordering = ['-add_time']


class Category(models.Model):
    title = models.CharField(max_length=20,
                             unique=True,
                             verbose_name='标题')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')

    # 父分类关系？未声明先引用： '类名' 或 'self'
    parent = models.ForeignKey('self',
                               verbose_name='所属分类',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)  # 后台管理页面中是否可以为空(验证)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_category'
        verbose_name = '小说分类'
        verbose_name_plural = verbose_name


def save_file_path(instance, filename):
    new_file_name = str(uuid.uuid4()).replace('-', '')+os.path.splitext(filename)[-1]
    return 'arts/{}'.format(new_file_name)


class Art(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='标题')
    summary = models.CharField(max_length=100,
                               verbose_name='描述')
    content = models.TextField(verbose_name='详细说明')

    author = models.CharField(max_length=20,
                              verbose_name='作者')

    publish_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='发布时间')

    # 文章的封面图片 cover
    # 依赖 pillow（PIL） 库: pip install pillow
    cover = models.ImageField(verbose_name='封面',
                              upload_to=save_file_path,  # 相对MEDIA_ROOT
                              null=True,
                              blank=True)  # ？上传的文件名如何重命名

    # 自定义upload_to函数
    # def user_directory_path(instance, filename):
    #      # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #      return 'user_{0}/{1}'.format(instance.user.id, filename)

    # class MyModel(models.Model):
    #     upload = models.FileField(upload_to=user_directory_path)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='分类名')

    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_art'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']


class RollSet(models.Model):

    free_levels = ((0, '免费'), (1, 'VIP'))

    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='名称')

    free_level = models.IntegerField(verbose_name='免费级别',
                                     choices=free_levels,
                                     default=0)
    art = models.ForeignKey(Art,
                            on_delete=models.CASCADE,
                            verbose_name='所属文章')

    @property
    def free_level_name(self):
        return self.free_levels[self.free_level][1]

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_roll'
        verbose_name = '卷集'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Chapter(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='名称')

    # 修改为UEditor的富文本字段
    content = UEditorField(verbose_name='内容',
                           width=600,
                           height=800,
                           imagePath='ueditor/art/images/',
                           toolbars='full')  # mini, normal, full

    publish_date = models.DateTimeField(verbose_name='发布时间',
                                        auto_now_add=True)

    roll = models.ForeignKey(RollSet,
                             on_delete=models.CASCADE,
                             verbose_name='所属卷集')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_chapter'
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        ordering = ['publish_date']