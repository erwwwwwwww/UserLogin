from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    nickname = models.CharField(max_length=8, null=True, blank=True, verbose_name='昵称', help_text='昵称最大长度为8字符')
    mobile_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码', help_text='手机号码')
    qq = models.CharField(max_length=15, null=True, blank=True, verbose_name='QQ', help_text='QQ')
    company = models.CharField(max_length=50, verbose_name='工作单位', help_text='工作单位')


# 文章
class Articles(models.Model):
    title = models.CharField(max_length=80, help_text='标题')
    add_time = models.DateTimeField(auto_now_add=True) # 创建时间
    edit_time = models.DateTimeField(auto_now=True)  # 修改时间
    author = models.ForeignKey(UserModel, verbose_name='作者', related_name='art_author')
    text = models.TextField(verbose_name='内容', help_text='内容')


#评论
# 不注册可以评论
class Comments(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称', help_text='名称')
    email = models.EmailField(verbose_name='邮件', help_text='邮件')
    obj = models.CharField(max_length=50, verbose_name='标题', help_text='标题')
    message = models.TextField(verbose_name='内容', help_text='内容')
    post = models.ForeignKey(Articles, related_name='post_comment') # 关联文章外键


