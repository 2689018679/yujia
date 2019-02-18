from django import template

register = template.Library()

@register.filter(name='my_star')
def my_star(value,arg):
    str=''
    star='<img src="/static/hq/img/star.png">'
    for i in range(int(arg)):
        str+=star
    print(str)
    return str

@register.filter(name='jl')
def jl(value,arg):
    print(value,arg)
    return arg[value-1]

@register.filter(name='tese')
def tese(value,arg):
    str=''
    for item in arg.split(','):
        str+='<li>%s</li>'%item
    return str

@register.filter(name='fuwu')
def fuwu(value,arg):
    str=''
    for item in arg.split(','):
        str+="<li><img src='/static/dj/dj_img/xiang.png' alt=''style='width:0.44rem;height:0.5rem;' class='dj1'><p>%s</p></li>"%item
    return str
