from django import forms
from django.contrib.auth import get_user_model
import re

User = get_user_model()


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'用户名长度至少为6个字符', 'required': 'required',}),
                               max_length=50, error_messages={'required': '账户不能为空'})
    email = forms.EmailField(label='Email',max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': '密码长度至少6个字符',
                                                                                    'required': 'required'}), max_length=20,
                                error_messages={'required':'密码不能为空'})
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': '重复输入密码',
                                                                                    'required': 'required'}), max_length=20,
                                error_messages={'required':'密码不能为空'})
    nickname = forms.CharField(label='昵称', max_length=8)
    first_name = forms.CharField(label='姓氏', max_length=30)
    last_name = forms.CharField(label='名字', max_length=30)
    mobile_phone = forms.CharField(label='手机号码', max_length=11)
    qq = forms.CharField(label='QQ', max_length=15)
    company = forms.CharField(label='工作单位', max_length=50)


    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError('你的账户长度至少6个字符.')
        elif len(username) > 50:
            raise forms.ValidationError('你的账户长度过长，请重新输入.')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('你的账户已被注册，请重新输入.')

        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_email = User.objects.filter(email__exact=email)
            if len(filter_email) > 0:
                raise forms.ValidationError('邮箱已被注册.')
        else:
            raise forms.ValidationError('请输入合法的邮箱地址')

        return email


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError('您的密码长度小于6字符')
        elif len(password1) > 20:
            raise forms.ValidationError('您的密码长度过长')

        return password1


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password mismatch.Please enter agin.')

        return password2




#登入表单 --账户/邮箱登入
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'用户名长度至少为6个字符', 'required': 'required',}),
                               max_length=50, error_messages={'required': '账户不能为空'})
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'placeholder': '密码长度至少6个字符',
                                                                                    'required': 'required'}), max_length=20,
                                error_messages={'required':'密码不能为空'})

    #验证邮箱/账户
    def clean_username(self):
        username = self.cleaned_data.get('username')

        # 优先判断username是否是邮箱格式
        if email_check(username):
            filter_result = User.objects.filter(email__exact=username)

            if not filter_result:
                raise forms.ValidationError('邮箱未注册')
        # 查询账户是否存在
        else:
            filter_result = User.objects.filter(username__exact=username)

            if not filter_result:
                raise forms.ValidationError('请输入正确的账户')

        return username












