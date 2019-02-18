from django.urls import path
from .views import *

app_name='yujiaxm'

urlpatterns = [
    path('',login,name='login'),
    path('register/',register,name='register'),
    path("index", index), # 我的
    path('history/',history),
    path('search/',search),
    path('discovery/',discovery,name='discovery'),
    path('exploration_<con>/',exploration),
    
    path('yyxq_<d_id>/', yyxq,name="yyxq"),
    path('ddxq_<id>/', ddxq,name="ddxq"),
    path('fabu/', fabu,name="fabu"),  # 发布
    path('duihua1/', duihua1, name="duihua1"),  # 聊天
    path('duihua2/', duihua2, name="duihua2"),  # 聊天
    path('changguanxq_<id>/',changguanxq,name="changguanxq"),
    path('dongzuoxq/',dj_swan,name="dongzuoxq"),
    path('xk_<c_id>/',xk,name="xk"),
    path('ddxqb/',ddxqb,name='ddxqb'),

    path('order/',order,name='order'),
    path('act/',act,name='act'),
    path('category/',category,name='category'),
    path('find/',find,name='find'),
    path('music/',music,name='music'),
    path('songs<id>/',songs,name='songs'),
    path('position/', position, name='position'),

    path('bank_<id>/', bank, name='bank'),
    path('period_<id>/', period, name='period'),
]