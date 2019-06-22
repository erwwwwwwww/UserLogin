from django.shortcuts import render,get_object_or_404, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import get_user_model,authenticate,login
from django.http import HttpResponseRedirect


User = get_user_model()

# Create your views here.


def index(request):
    return render(request, 'test_index.html')


def user_register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password1']
            nickname = register_form.cleaned_data['nickname']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            mobile_phone = register_form.cleaned_data['mobile_phone']
            qq = register_form.cleaned_data['qq']
            company = register_form.cleaned_data['company']

            new_user = User.objects.create_user(username=username, email=email, password=password, nickname=nickname, mobile_phone=mobile_phone,
                            qq=qq, company=company, first_name=first_name, last_name=last_name)

            return redirect('/accounts/login/')
        # 注册失败
        else:
            # print(register_form.errors.as_data())
            return render(request, 'users/register_error.html')

    else:
        form = RegistrationForm()

        return render(request,'users/registration.html', {'register_form':form})


def user_login(request):
    empty_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'test_index.html')
            else:
                #登入失败
                # print('用户名:%s 密码:%s'%(username, password))
                return render(request, 'users/login.html',{'login_form': empty_form} )
        else:
            return render(request, 'users/login.html',{'login_form': empty_form})
    else:
        return render(request,'users/login.html', {'login_form': empty_form})


























