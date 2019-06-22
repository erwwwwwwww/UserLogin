from django.contrib import admin
from .models import UserModel

# Register your models here.
# 后台管理注册用户信息
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nickname', 'company', 'qq', 'mobile_phone')
    search_fields = ('username', 'email', 'mobile_phone')
    ordering = ('id', )

admin.site.register(UserModel, UserAdmin)
