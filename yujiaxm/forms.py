from django.forms import ModelForm,Form,CharField,PasswordInput,TextInput
from django.contrib.auth import models,authenticate
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Login(Form):
    name = CharField(label='账户名',widget=TextInput(attrs={'placeholder':"请输入您的账号或邮箱"}))
    password = CharField(widget=PasswordInput(attrs={'placeholder':"请输入密码"}),label='密码')
    class Meta:
        model = models.User
        fields = ['name','password']
        widgets = {
            'password': PasswordInput
        }
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name',None)
        password = cleaned_data.get('password',None)
        if name and password:
            user=authenticate(username=name,password=password)
            if not user:
                raise ValidationError('用户名密码错误')
            else:
                self.user=user

class Register(Form):
    name = CharField(label='账户名',widget=TextInput(attrs={'placeholder':"请输入您的账号或邮箱"}),error_messages={'required':u'账号重复'})
    password = CharField(widget=PasswordInput(attrs={'placeholder':"请输入验证码"}),label='验证码')
    class Meta:
        model = models.User
        fields = ['name','password']
        widgets = {
            'password': PasswordInput
        }
        labels = {
            'name': '用户名',
            'password': '验证码',
        }
    def clean(self):
        print('------------------')
        cleaned_data = super().clean()
        username = cleaned_data.get("name",None)
        username_list=models.User.objects.all().values_list('username')
        if username:
            for i in username_list:
                if username in i:
                    raise ValidationError(
                        '用户名已存在，请重新输入'
                    )
        return cleaned_data
















