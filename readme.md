瑜+app环境配置：

 

一、基础环境配置

1、Python3.7可从官网下载（https://www.python.org/getit/）

2、WampServer64或者MySQL数据库（环境安装文件夹中附带WampServer64安装包）

二、下载安装python运行环境（32或64位）

<https://www.python.org/downloads/release/python-372/>

下载：

![img](https://github.com/2689018679/yujia/blob/master/images/1.png)

安装：（请勾选“Add Python 3.7 to PATH”选项，之后一路确定即可）

![img](https://github.com/2689018679/yujia/blob/master/images/2.png)

 

三、win+R进入cmd命令窗口，输入python，出现“>>>”表示python环境变量安装成功。

 

1、Win+R    输入cmd   确定：

![img](https://github.com/2689018679/yujia/blob/master/images/3.png)

2、输入python 出现以下界面，即为成功。然后输入 exit() 

![img](https://github.com/2689018679/yujia/blob/master/images/4.png)

 

四、导入数据库以及项目中使用的包

1、先打开环境安装文件夹，安装其中的wamp64（按照安装说明顺序安装，之后一路确定即可）

![img](https://github.com/2689018679/yujia/blob/master/images/5.png)

2、打开wamp64，左键点击右下角图标，打开phpMyAdmin。 

![img](https://github.com/2689018679/yujia/blob/master/images/6.png)

 

3、创建瑜伽数据库，排序规则选择多语言不区分大小写，详见下图

![img](https://github.com/2689018679/yujia/blob/master/images/7.png)

 

3、选中创建好的yujia库，点击打开，右侧上方点击导入，如图选中mysql文件进行导入：

![img](https://github.com/2689018679/yujia/blob/master/images/8.png)

在导入界面选择sql文件（环境安装文件夹中附带），点击执行

4、导入包

打开项目文件夹，在地址栏输入cmd回车之后进入命令行，如下所示：

![img](https://github.com/2689018679/yujia/blob/master/images/9.png)



 

在命令行界面输入 python -m pip install -r pipinstallfile.text 命令，导入所需模块。

![img](https://github.com/2689018679/yujia/blob/master/images/10.png)

​    

五、运行程序

1、打开wamp64，保证数据库可连接(wamp64图标为绿色)

![img](https://github.com/2689018679/yujia/blob/master/images/11.png)

 

2、输入python manage.py runserver 命令，

![img](https://github.com/2689018679/yujia/blob/master/images/12.png)

3、在浏览器地址栏中输入 127.0.0.1:8000 即可访问。

![img](https://github.com/2689018679/yujia/blob/master/images/13.png)
