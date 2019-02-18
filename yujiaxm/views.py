from django.shortcuts import render,HttpResponse,redirect,reverse
from .forms import Login,Register
from django.contrib.auth import login as login1,models
from django.contrib.auth import authenticate,login as login1
from .models import *
from math import radians, cos, sin, asin, sqrt
from django.views.decorators.csrf import csrf_exempt
import json,re
# from geopy.distance import geodesic
# Create your views here.

def login(request):
    if request.method == "GET":
        form = Login()
        return render(request,'zzy/login.html/',{'form':form})
    else:
        form = Login(request.POST)

        if form.is_valid():
            # 成功
            login1(request, form.user)
            jd = request.POST['jd']
            wd = request.POST['wd']
            wz = request.POST['wz']
            if jd and wd and wz:
                if request.user.info:
                    print(123)
                    request.user.info.create(distance='%s,%s' % (jd, wd), name=wz)
                else:
                    request.user.update(distance='%s,%s' % (jd, wd), name=wz)
            return redirect(reverse('yujiaxm:order'))
        else:
            # 验证失败
            return render(request,'zzy/login.html',{'form':form})

def register(request):
    if request.method == 'GET':
        form = Register()
        form.fields['name'].help_text = None
        return render(request, 'zzy/register.html', {'form': form})
    else:
        form = Register(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            from django.contrib.auth.hashers import make_password
            models.User.objects.create(username=data['name'], password=make_password(data['password']))
            return redirect(reverse('yujiaxm:login'))
        else:
            return render(request, 'zzy/register.html', {'form': form})


def index(request):  # 个人中心
    return render(request, "hq/index.html")

def history(request):  # 历史搜索
    return render(request,"hq/history.html")

def search(request): # 搜索界面
    obj=Search.objects.all().order_by('-times')
    if len(obj)>4:
        obj=obj[0:4]
    return render(request,"hq/search.html",{'obj':obj})

def exploration(request,con): #　结果
    if request.method == 'GET':
        obj=Search.objects.filter(con=con)
        if obj:
            Search.objects.filter(con=con).update(times=Search.objects.filter(con=con)[0].times+1)
        else:
            Search.objects.create(con=con)
    obj=Place.objects.all()
    res=[]
    yjd,ywd=request.user.info.distance.split(',')
    jl_list=[]
    for i in obj:
        if con in i.username:
            xjd,xwd=i.distance.split(',')
            jl=round(haversine(float(yjd), float(ywd), float(xjd), float(xwd)),2)
            jl_list.append(jl)
            print(i)
            res.append(i)
    if len(res)==0:
        return redirect(reverse('yujiaxm:discovery'))
    lbt=[]
    if len(res)>3:
        lbt=res[0:3]
    return render(request,"hq/exploration.html",{'res':res,'num':len(res),'str':str,'lbt':lbt,'jl_list':jl_list})

# 计算距离
def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r

def discovery(request): # 无
    return render(request,"hq/Discovery.html")



def yyxq(request,d_id):
    if d_id:
        dd = Dingdan.objects.filter(id=d_id)[0]
        return render(request,'xing/xing-yyxq.html',{'i':dd})

def ddxq(request,id):
    xk = Xuanke.objects.filter(id=id)[0]
    dd=[]
    if id:
        Dingdan.objects.create(author=request.user,name=xk.c_id,xuke_id=xk,price=xk.price,riqi=xk.riqi,shijianduan=xk.shijianduan,chance=xk.chance)
        dd=Dingdan.objects.all().order_by('-c_time').first()
    print(dd)
    return render(request,'xing/xing-ddxq.html',{'dd':dd})

@csrf_exempt
def xk(request,c_id):

    xk = Xuanke.objects.filter(c_id=c_id)
    return render(request,'xing/scheduled.html',{'xk':xk})


def fabu(request):
    return render(request,'xing/xing-fabu.html')

def duihua1(request):
    return render(request,'xing/xing-duihua1.html')

def duihua2(request):
    return render(request,'xing/xing-duihua2.html')

def changguanxq(request,id):
    vd=[]
    pl=[]
    try:
        vd = Venue_details.objects.filter(c_id=Place.objects.filter(id=id)[0])[0]
        pl = Pinglun.objects.filter(c_id=Place.objects.filter(id=id)[0])
    except:
        pass
    print(pl)
    return render(request,'xing/dj_index.html',{'vd':vd,'pl':pl,'id':id})

def dj_swan(request):
    dd = Dongzuo_details.objects.all
    return render(request,'xing/dj_swan.html',{'dd':dd})


def ddxqb(request):
    if request.user:
        dd = Dingdan.objects.filter(author=request.user)
        return render(request,'xing/xing-ddxqb.html',{'dd':dd})
    else:
        return redirect(reverse('yujiaxm:login'))


@csrf_exempt
def order(request):
    list_order = list(Place.objects.all().values())
    place = request.POST.get('place')

    print(place)
    # lnglat = str(request.POST.get('lnglat'))
    # print(lnglat)
    # s = tuple(re.findall("\d+.\d+", lnglat))
    # print(s)
    # distance = list(Place.objects.all().values('distance'))
    # print(distance)
    # for item in distance:
    #     item_dis = item['distance']
    #     print(item_dis)
        # data4 = geodesic((s), (item_dis))
        # print(data4)
    # data4=geodesic((37.82851,112.55176),(37.82861,112.55256))
    # print(data4)
    try:
        data = request.POST.get('data')
        data1 = json.loads(data)['city']
        data2 = json.loads(data)['district']
        data3 = []
        data3.append(data1)
        data3.append(data2)

        message={
            # 'm':list_order,
            's':data3,
            # 'm':data4,
        }
        return HttpResponse(json.dumps(message,ensure_ascii=False))
    except:
        return render(request, 'yoga/order.html', {'list_order': list_order,'place':place})

def act(request):
    act = Act.objects.all().values()
    return render(request,'yoga/act.html',{'act':act})
def category(request):
    cate = Category.objects.all().values()
    return render(request,'yoga/category.html',{'cate':cate})
def music(request):
    music = Music.objects.all().values()
    return render(request,'yoga/music.html',{'music':music})
def find(request):
    list_order = list(Place.objects.all().values())
    print(list_order)
    assess = list(Place.objects.all().values('assess'))
    print(assess)
    for i, v in enumerate(list_order):
        v['assess'] = assess[i]['assess']
    print(list_order)
    return render(request,'yoga/find.html',{'list_order':list_order})
def songs(request,id):
    songs = Music.objects.filter(id=id).values()
    gq = Song.objects.filter(t_id=id).values()
    print(gq)
    return render(request,'yoga/songs.html',{'songs':songs,'gq':gq})
def position(request):
    return render(request, 'yoga/position.html')


# 郑博

# 选择付款方式
@csrf_exempt
def period(request,id):
    dd = Dingdan.objects.filter(id=id).first()
    price = Dingdan.objects.filter(id=id).first()
    return render(request, 'zb/Payments.html', {'price':price, 'dd':dd})

# 银行卡付款
@csrf_exempt
def bank(request,id):
    user_id = request.user.id
    yh = BankCard.objects.filter(y_id=user_id).all()
    price = Dingdan.objects.filter(id=id).first()
    dd = Dingdan.objects.filter(id=id).first()
    if request.method == "POST":
        fl=request.POST.get('pas',None)
        if fl:
            password = request.user.info.password
            if password == fl:
                user = request.user.username
                ye = request.POST.get('yue', None)
                xf = request.POST.get('xf', None)
                kh = request.POST.get('kahao', None)
                kou = int(ye)-int(xf)
                BankCard.objects.filter(card=kh).update(balance=kou)
                return HttpResponse('ok')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('网络连接中断')
    else:
        return render(request, 'zb/payment.html',{'yh':yh ,'price':price, 'dd':dd})

