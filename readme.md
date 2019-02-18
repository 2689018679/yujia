瑜+app环境配置：

 

一、基础环境配置

1、Python3.7可从官网下载（https://www.python.org/getit/）

2、WampServer64或者MySQL数据库（环境安装文件夹中附带WampServer64安装包）

二、下载安装python运行环境（32或64位）

<https://www.python.org/downloads/release/python-372/>

下载：

![img](https://github.com/2689018679/yujia/blob/master/images/1.png)

安装：（请勾选“Add Python 3.7 to PATH”选项，之后一路确定即可）

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png)

 

三、win+R进入cmd命令窗口，输入python，出现“>>>”表示python环境变量安装成功。

 

1、Win+R    输入cmd   确定：

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image006.jpg)

2、输入python 出现以下界面，即为成功。然后输入 exit() 

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)

 

四、导入数据库以及项目中使用的包

1、先打开环境安装文件夹，安装其中的wamp64（按照安装说明顺序安装，之后一路确定即可）

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

2、打开wamp64，左键点击右下角图标，打开phpMyAdmin。 

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)

 

3、创建瑜伽数据库，排序规则选择多语言不区分大小写，详见下图

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg)

 

3、选中创建好的yujia库，点击打开，右侧上方点击导入，如图选中mysql文件进行导入：

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg)

在导入界面选择sql文件（环境安装文件夹中附带），点击执行

4、导入包

打开项目文件夹，在地址栏输入cmd回车之后进入命令行，如下所示：

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image018.jpg)



 

在命令行界面输入 python -m pip install -r pipinstallfile.text 命令，导入所需模块。

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image020.jpg)

​    

五、运行程序

1、打开wamp64，保证数据库可连接(wamp64图标为绿色)

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image021.png)

 

2、输入python manage.py runserver 命令，

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image023.jpg)

3、在浏览器地址栏中输入 127.0.0.1:8000 即可访问。

![img](file:///C:/Users/qwer/AppData/Local/Temp/msohtmlclip1/01/clip_image025.jpg)
