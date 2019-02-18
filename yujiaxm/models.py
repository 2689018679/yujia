from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class info(models.Model):
    u=models.OneToOneField(to=User,on_delete=models.CASCADE)
    password = models.CharField(max_length=6, verbose_name='密码')
    distance=models.CharField(max_length=200)
    name=models.CharField(max_length=20,default='')

class Search(models.Model):
   time=models.DateTimeField(auto_now_add=True)
   times=models.IntegerField(default=0)
   con=models.CharField(max_length=100)

class Place(models.Model):
   class Meta:
      verbose_name = "场馆"
      verbose_name_plural = "场馆"

   name = models.CharField(max_length=30, verbose_name="所属区域")
   username = models.CharField(max_length=30, verbose_name="场馆名称", default="")
   img = models.ImageField(upload_to="img/", default="", verbose_name="场馆图片")
   place = models.CharField(max_length=50, verbose_name="地点", default="")
   distance = models.CharField(max_length=30, verbose_name="距离", default="")
   assess = models.IntegerField(default=1, choices=(
      (1, "一星"),
      (2, "二星"),
      (3, "三星"),
      (4, "四星"),
      (5, "五星"),
   ))


class Venue_details(models.Model):
    c_id = models.ForeignKey(to=Place, verbose_name="场馆id", on_delete=models.CASCADE)
    server = models.CharField(verbose_name="服务", max_length=20, default='')
    tese = models.CharField(verbose_name="场馆特色", max_length=20, default='')
    phnumber = models.CharField(max_length=200, verbose_name="联系电话", default="")
    class Meta:
        verbose_name_plural="场馆详情"

class Pinglun(models.Model):
    con = models.TextField(max_length=200,verbose_name="评论内容")
    author = models.ForeignKey(to=User,verbose_name="作者",on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    c_id = models.ForeignKey(to=Place,verbose_name="评价场馆",on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="评论"

class Xuanke(models.Model):
    riqi = models.DateField(verbose_name='有限日期', auto_now_add=False)
    shijianduan = models.CharField(verbose_name='时间段', max_length=100)
    didian = models.CharField(max_length=100, verbose_name='房间')
    neirong = models.CharField(max_length=100,verbose_name='授课内容')
    chance = models.CharField(max_length=10,verbose_name='场次',default="")
    price = models.CharField(max_length=100,verbose_name='金额')
    renshu = models.IntegerField(verbose_name="人数")
    c_id=models.ForeignKey(to=Place,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="选课"

class Dingdan(models.Model):
    name = models.ForeignKey(to=Place,max_length=30,verbose_name="场馆名称",on_delete=models.CASCADE)
    xuke_id = models.ForeignKey(to=Xuanke,verbose_name="选课id",on_delete=models.CASCADE)
    author = models.ForeignKey(to=User,verbose_name="创建人",on_delete=models.CASCADE)
    price = models.CharField(max_length=100,verbose_name="金额")
    type = models.IntegerField(verbose_name="支付状态",default=0)
    riqi = models.DateField(verbose_name="日期",auto_now_add=False)
    shijianduan = models.CharField(verbose_name="时间段",max_length=100,default='')
    chance = models.CharField(max_length=10, verbose_name='场次', default="")
    c_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    class Meta:
        verbose_name_plural="订单详情"

class Dongzuo(models.Model):
    name = models.CharField(verbose_name='动作名称',max_length=100)
    img = models.ImageField(verbose_name='动作图片',default="")
    class Meta:
        verbose_name_plural="动作"

class Dongzuo_details(models.Model):
    name = models.ForeignKey(to=Dongzuo,max_length=40,verbose_name="动作名称",on_delete=models.CASCADE)
    ke_time = models.CharField(max_length=40,verbose_name="课时")
    shi_time = models.CharField(max_length=40,verbose_name="时长")
    rank = models.CharField(max_length=40,verbose_name="难度等级")
    produce = models.CharField(max_length=400,verbose_name="介绍")
    people = models.CharField(max_length=400,verbose_name="人群")
    video_name = models.CharField(max_length=40,verbose_name="视频名称")
    class Meta:
        verbose_name_plural="动作详情"
class Category(models.Model):
    class Meta:
        verbose_name = "课程分类"
        verbose_name_plural = "课程分类"
    name = models.CharField(max_length=30,verbose_name="分类名称")
    title = models.CharField(max_length=30,verbose_name="标题")
    people = models.IntegerField(verbose_name="参加人数")
    img = models.ImageField(upload_to="img/",default="",verbose_name="分类图片")
class Music(models.Model):
    class Meta:
        verbose_name = "瑜伽音乐"
        verbose_name_plural = "瑜伽音乐"
    name = models.CharField(max_length=30,verbose_name="歌单分类名称")
    img = models.ImageField(upload_to="img/",default="",verbose_name="歌单分类背景图片")

class Act(models.Model):
    class Meta:
        verbose_name = "动作库"
        verbose_name_plural = "动作库"
    name = models.CharField(max_length=30,verbose_name="动作分类名称")
    img = models.ImageField(upload_to="img/",default="",verbose_name="动作分类背景图片")
class Song(models.Model):
    class Meta:
        verbose_name = "歌名"
        verbose_name_plural = "歌名"
    name = models.CharField(max_length=30,verbose_name="歌名")
    t = models.ForeignKey(to=Music,to_field='id',verbose_name="所属分类",on_delete=models.CASCADE)


class BankCard(models.Model):
    y = models.ForeignKey(to=User, on_delete=models.CASCADE)
    card = models.CharField(max_length=20, verbose_name='银行卡号')
    people = models.CharField(max_length=20, verbose_name='持有人')
    vest = models.CharField(max_length=100, verbose_name='银行卡归属')
    Type = models.CharField(max_length=100, verbose_name='类型')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    balance = models.IntegerField(verbose_name='余额')












