# -UBUNTU-
# 符号标注：
## "()"表示解释该命令，输入等作用和使用方法（个人用法）
## "[]"命令里表示可以不用添加的
### "[]"变量里表示匹配内包含的所有字符
## "-"表示添加的要求，是指令中要加的
## "."文件名前加，表示隐藏文件
## ".."命令中表示返回上一级
## "~"切换到当前用户主目录，当前目录家目录
## "/"表示分割目录途径下，下一个（子目录）目录
## ":"后面如果不是绝对路径默认家目录为参照路径
## "|"管道,左写右读,可以在执行一个命令的输出，给后面的一个命令
### 两者间未加“空格”表示或者
## "？"表示任意一个字符，至少一个
## "*"代表任何多个字符
### 表达式：*（文件名中个别字符）.(格式）
###          （文件名中个别字符）*
###         *（文件名中个别字符）*
### *文字*（在md文本格式中表示斜体字）
### **文字**（在md文本格式中表示加粗）
## "“”"表示特殊按键（个人用法）
## > 存放文件（表示输出文本）
## >>（表示追加）
# 常用代表词
## GID（组标识）
## r（可读权限）
## w（可写权限）
## x（可执行权限）
## RWX详细
## -i（覆盖文件前提示）
### R 4（可读权限代表4)
### W 2（可写权限代表2）
### X 1（可执行权限代表1）
  如果想要设置多个，数字相加就行了
### 表：
#### 
4 2 1 7 RWX
4 2 0 6 RW-
4 0 1 5 R-X
4 0 0 4 R--
0 2 1 3 -WX
0 2 0 2 -W-
0 0 1 1 --X
0 0 0 0 ---
## user（远程机器上用户名）
## remote（远程机器上的地址，ip/域名，或者其他别名）
## port（是ssh server监听的端口，默认222）
## passwd（表示用户权限目录）
## d（代表目录）
## u（代表主用户）
## g（代表组用户）
## o（代表其他用户）
## CMD（命令）
## dash（ubuntu默认的是dash（软件名））
## a（显示终端上的所有进程，包括其他用户的进程）
## U（显示进程的详细状态）
## X（显示没有控制终端的进程，所有正常执行的程序）
## MEM（表示内存占用率）
## PID（进程代号）
## USER（表示哪一个用户启动的程序）
## START（表示程序启动时间）
## COMMAND（运行的命令名称）
## itheina（用户名）
## name（指定搜索名字）
## Firstpython（软连接名）
## c（生成档案文件，创建打包文件）
## x（解开档案文件）
## v（列出归档解档的详细过程，显示进度
## f（指定档案文件名称，f后面一定是.tar文件，所以必须放选项最后）
## -C（解压缩到指定目录，注意解压缩的目录必须存在
# 命令要求
## command [-options] [parameter]
  命令名   选项（加一个-）   参数
### 之间加空格(有中括可以不用加）
### 命令名：相应功能的英文单词或单词缩写
### 选项：可用来对命令进行控制，也可以省略
### 参数：传给命令的参数，可以是零个，一个或多个
### 不允许文件目录重名！！！！
### 文件名前加.为隐藏文件
### 更改用户的组之后需要重新登录才能生效 
### 使用kill最好只终止当前用户的进程，不要终止root身份开启的进程，那是系统进程。
### linux中**文件名**和**文件的数据**是分开储存的
：关系，列：软连接文件名-（访问）软连接文件数据-（访问）文件名-（访问)文件数据
### 硬链接相当于文件名,都可以直接访问文件数据
： 关系，列：文件名=硬链接-（访问）文件数据
### f后面一定是.tar文件，所以必须放选项最后
# 命令码
### clear（清屏）
## 基础文件和目录命令
### ls（查看文件下文件）
 后面可加文件名查看文件
 ：ls -a(查看隐藏文件）
  文件名前加.为隐藏文件
  加..为上一个文件
### rm（删除）（注：删除后不可恢复）
 ：-r（可以删除目录，可以递归删除多个目录）
  -f（强制删除）
### pwd(查看当前目录途径）
### mkdir（创建新的目录）
 ：-p a/b/c/d/(在当前文件下创建文件，串联）（递归创建目录）	
### cd（切换目录）
 ：~（切换到当前用户主目录，当前目录家目录）
  .（保持不变）
  ..（上级目录）
  -（在最近两次目录来回）
（相对文件，绝对文件）
### touch（创建空白文件）/（修改名字）
## 拷贝和移动命令
### cp 源文件 目标文件（复制）
：~/a/b ./a/b
    -i（覆盖文件前提示）
    -r（若给出的源文件是目录文件，
 则cp将递归复制该目录下的所有子目录和文件，
 目标文件必须为一个目录名）
### “ctrl” c（新行）
### tree[目录名]（递归查看目录）
：~（表示用户的家目录）
 -d（只显示目录）
### mv 源文件 目标文件（移动文件）
 :-i（覆盖提示）
## 查看文件内容命令
### cat 文件名（查看文件）
：-b（对非空行输出编号）
    -n（对所有行输出边号）
    常会用“：”分割信息。
### more 文件名（分屏显示文件内容）
### grep（查找，搜索工具）
：-n（显示匹配行及行号）
 -v（显示不包含匹配文本的所有行）
（相当于求反）
 -i（忽略大小写）
 ^（搜索行首字母，前加）
 $（搜索行尾字母，后加）
## 终端文字命令补充
### echo（文字内容）
：在终端中显示参数指定的文字，通常会和**重定向**联合使用
### 重定向>和>>（传递给终端显示）
：linux允许将命令执行结果**重定向**到另一个文件
 将文应显示在**终端的内容** **输出**/**追加**到**指定文件中**。
#### 数据 > 存放文件（表示输出文本）
#### >>（表示追加）
### |（管道）
：linux允许将**一个命令的输出**可以**通过管道**作为**另一个命令的输出**
 左写右读,可以在执行一个命令的输出，给后面的一个命令
 附加指令：
#### more（分屏显示内容）
#### grep（在命令执行结果基础色查下指定文本）
## 远程管理常用命令
### 关机/重启
#### shutdown 选项 时间（挂机/重启命令）
（默认一分钟重启）
 ：-c（取消关机指令）
 -r（重新启动）
 now（立即）
### 查看或配置网卡信息
#### ifconfig（查看/配置计算机当前网卡信息）
 ：ifconfig | grep inet（快速查看ip）
#### ping ip（检测到目标地址的链接是否正常）
#### ：ctrl c（取消查看）
  ping 127，0，0，1（是本地计算机） 
  端口（确认是否有图形软件运行）
  ssh 22
  web 80
  https 443
  ftp 21
## 远程登录复制文件
### 远程登录
#### ssh [-p port] user@remote
：user（远程机器上用户名）
  remote（远程机器上的地址，
  ip/域名，或者其他别名）
  port（是ssh server监听的端口，
  默认222）
##### ssh-keygen（生成ssh钥匙）
##### ssh-copyoid -p port user@remote（记住公钥）
##### ssh user@remote
#### 免密码登录
：步骤
 ssh itheima（用户名）@ip地址（使用ssh链接对方）
 exit
 cd ~/.shh
 shh-keygen
 shh-copy-id 用户名@ip地址
### 复制命令
#### scp（远程拷贝文件）
（格式与ssh基本一样）
：在指定端口-P（是大写）
 （注：“：”后面如果不是绝对路径默认家目录为参照路径）
 （注：csp命令只能在linux和unix可以使用）
 -r（可以传送文件夹，若给出的源文件是目录文件，则scp递归传复制目录下的所有子目录1和文件，目标必须有一个目录名）
 -P（若远程ssh服务器的端口不是22，则需要使用大写-P选择指定端口）
##### scp [-P port] 1.py(文件名) user@remote：Desktop(路径)/2.py
（把本地文件1复制到远程家目录下的路径/2文件）
##### scp [-P port] user@remote：Desktop/3.py 4.py 
（把远程家目录下的路径/3文件复制本地文件下的4文件）
##### scp -r demo user@remote：Desktop
（把当前目录下的demo文件夹复制到远程家目录文件的Desktop）
##### scp -r user@remote：Desktop demo
（把远程家目录下的Desktop复制到当前目录下的demo文件夹）
### 快捷匹配方式（别名使用）：
经常输入ssh -p port user@remote较麻烦，可以使用ssh-mac（别名）代替。
：步骤
 cd ~/.ssh
 touch config（创建的文件名）
 gedit config（文件名）
 （窗口打开文件）
 ：文件中输入
   Host myserver（使用的别名名称）
     HostName（名字） ip地址
     user itheina（登录计算机用户名）
     port 22
### 外加补充
#### group（组）
#### exit（退出远程登录）
#### Host 别名（创建别名）
#### chmod（修改用户/组对文件/目录的权限）
：chmod +/-rwx 文件名|目录名
#### sudo（表示超过用户权限）
：root 账号拥有所有权限，用来维护系统 
 系统创造的用户为标准用户，只能修改除系统文件外的文件
 一次拥有五分钟的权限
### 用户权限相关命令
 r（可读权限）
 w（可写权限）
 x（可执行权限）
 文件名:
（目录标记）
 d(代表是目录)
 -（代表文件）
   d（代表目录）
 第一个拥有者，
 第二个组
 第三个其他人
 (硬件链接数）有多少种方式可以访问到目录
 (大小）
 (时间)
 (名称)
## 组管理 终端命令
### groupadd 组名（添加组）
### groupdel 组名（删除）
### cat/etc/group(确认组信息)
### chgrp -R 组名 文件/目录名（修改文件/目录的所属组）
### useraddd -m -g 组 新创用户名（添加新用户）
：-m（自动建立用户家目录）
 -g(指定用户所在组，否则建立一个同名)
### userdel -r 用户名（删除用户）
：-r（自动删除家目录）
### passwd 用户名（设置用户密码）
：/stc/passwd(文件夹是存放用户信息，由六个分号组成7个信息)
1、用户名
2、密码（x，表示密码）
3、UID（用户标识）
4、GID（组标识）
5、用户全名或本地账号
6、家目录
7、登录使用的Shell，就是登录之后，使用的终端命令，ubuntu默认的是dash（软件名）
#### cat /etc/passwd | grep 用户名（确认/查看用户信息)
## 查看用户信息
### id [用户名]（查看用户代号（uid），组代号（gid））
：(不带用户名，查看当前目录的信息)
### who（查看当前所有登录的用户列表）
### whoami（查看当前登录用户的账号名）
### usermod（用来设置用户的主组/附加组花登录Shell）
：（主组：通常在新建用户时指定，在ect/passwd的是六列GID对应组）
（附加组：ect/group中最后一列表示该用户的用户列表，用于指定用户的附加权限）
 （更改用户的组之后需要重新登录才能生效)
#### usermod -g 组 用户名（修改用户的主组，passwd中的GID）
#### usermod -G 组 用户名（修改用户的附加组）
：G（指定附加组用）
#### usermod -s /bin/bash 用户名（修改用户的登录shell）
：bash（软件名）
### which（命令可以查看执行命令所在位置）
：/etc/passwd(是用于保存用户信息的文件)
 usr/bin/passwd（是用于修改用户的密码程序）
 指令可以用来查看执行命令所在位置，列
#### which ls()
 *#* 输出
 *#* /bin/ls
#### which useradd
 *#* 输出
 *#* /use/sbin/useraad
#### which passwd
 *#* 输出
 *#* /usr/bin/passswd
### bin、sbin（普通执行文件，系统管理执行文件）
： 在linux里，绝大部分可执行文件保存在/bin、/sbin、/usr/bin、/usr/sbin
  /bin（binary）是二进制执行文件目录，主要用于具体应用
 /sbin（system binary）是系统管理员专用的二进制代码存放目录，主要用于系统管理
 /usr/bin（user commands for applications)后期安装的一些软件
 /usr/sbin（super user commands for applications)超级用户的一些管理程序
## 切换用户
### su -用户名（切换用户，并切换目录，不加“-”不能切换到用户家目录，保持位置不变）
：su（不加用户名，可以切换到root，但是冰上推荐使用，因为不安全）
### exit（退出当前用户）
## 修改文件权限命令 
#### chown（修改拥有者）
##### chown 用户名 文件名|目录名（修改文件|目录的拥有者） 
#### chgrp（修改组）
##### chgrp -R 组名 文件名|目录名（递归修改文件|目录的组）
#### chmod（修改权限） 
##### chmod -R 755 文件名|目录名 （递归修改文件权限）
: 第1. 7（表示文件或者目录，拥有者的权限）
  第2. 5（表示文件或者目录，组成员的权限）
  第3. 5（表示文件或者目录，其他用户的权限）
  R 4（可读权限代表4)
  W 2（可写权限代表2）
  X 1（可执行权限代表1）
  如果想要设置多个，数字相加就行了
## 系统信息相关命令（远程维护服务器） 
### 时间和日期（远程维护）
#### date(查看湿贴时间)
#### cal（calendar查看日立）
：-y（可以查看一年的日历）
### 磁盘和目录空间
#### df -h（disk free显示磁盘剩余空间）
#### du -h [目录名]（disk usage显示目录下的文件大小）
：-h（以人性化的方式显示文件大小）
### 进程信息
#### ps aux（peocess status查看进程的详细状况）
：默认只会显示当前用户通过终端启动的应用程序
 CMD（命令）
 a（显示终端上的所有进程，包括其他用户的进程）
 U（显示进程的详细状态）
 X（显示没有控制终端的进程，所有正常执行的程序）
#### top（动态显示运行的进程并排序）
：退出直接输入“q” 
#### kill [-9] 进程代号（终止指定代号的进程）
：-9表示强行终止
 注：使用kill最好只终止当前用户的进程，不要终止root身份开启的进程，那是系统进程。
## 常用其他命令
### find（查找文件）
：find [路径] -name "*.py"(查找指定路径下扩展名是。py的文件，包括子目录中的文件）
 可用格式：
 find Desktop/ -name "*q*"(指定目录下搜索文件)
 name（指定搜索名字条件）
#### find -name "*1*"(搜索当前目录下，文件名包含去的文件)
#### find -name "*.txt"(搜索当前1目录下，所有以.txt为扩展名的文件)
#### find -name "1*"(搜索当前目录下，以数字1开头的文件)
### ln（软连接）
#### ln -s 源文件地址/文件名 快捷文件名（被链接的源文件链接文件）
：（类似于**windows**下的**快捷方式**）
 -s（没有选项建立的是一个**硬链接文件**
 注：（两个文件占用相同大小磁盘空间，**工作中几乎不会建立文件的硬链接**）
   （**源文件要使用绝对路径**，不能使用相对路径，这样可以方便移动链接文件后，仍然能够正常使用）
#### ln （没有-s）源文件/文件名 快捷文件名（建立一个硬链接）
：补充：linux中**文件名**和**文件的数据**是分开储存的
 软连接找的是完整的链接路径，并不是直接访问文件名和文件数据
   关系，列：软连接文件名-（访问）软连接文件数据-（访问）文件名-（访问)文件数据
 硬链接相当于文件名,都可以直接访问文件数据
   关系，列：文件名=硬链接-（访问）文件数据
 Firstpython（软连接名）
## 打包和压缩
### tar（打包） 
：不同操作系统中打包压缩方式不同
 列：windows常用RAR
 Mac常用Zip
 Linux常用tar.gz
   tar是linux中常用的**备份工具**，此命令可以把**一系列文件**打包到**一个大文件中**也可以把**一个打包的大文件**恢复成**一系列文件**（tar不负责压缩）
：c（生成档案文件，创建打包文件）
 x（解开档案文件）
 v（列出归档解档的详细过程，显示进度
 f（指定档案文件名称，f后面一定是.tar文件，所以必须放选项最后）
#### tar -cvf 打包文件名.tar 被打包文件/路径。。。（打包文件）
：-cvf是固定连续的条件，基本不会变动
（注：不加路径则打包到当前文件目录）
#### tar -xvf 打包文件名.tar（解包文件）
：-xvf一样是固定连续的条件，基本不会变动
### gzip（压缩）
：gizp压缩tar打包后的文件，扩展名一般用xxx.tar.gz
  linux中最常见的压缩文件就是xxx.tar.gz
在tar命令中-z条件选项可以调用gzip，可以方便实现压缩和解压的功能
#### tar -zcvf 打包文件名.tar.gz 被压缩的文件/路径。。。（压缩文件）
#### tar -zxvf 打包文件名.tar.gz（解压缩文件）
#### tar -zxvf 打包文件.tar.gz -C 目标文件（解压缩到指定目录文件夹）
：-C（解压缩到指定目录，注意解压缩的目录必须存在）
### bzip2（压缩）
：tar与bzip2也可以实现文件**打包和压缩**（用法和gzip一样）
扩展名为：xxx.tar.bz2
在tar命令中-j条件选项可以调用bzip2，可以方便实现压缩和解压的功能
#### tar -jcvf 打包文件名.tar.bz2 被压缩的文件/路径。。。（压缩文件）
#### tar -jxvf 打包文件名.tar.bz2（解压文件）
：同样-C条件选项也可以使用
## 通过apt安装/卸载软件
：apt（Advanced Packaging Tool）是linux下的一款安装包管理工具
 可以在终端中方便的**安装/卸载/更新软件包**
### apt-get（软件安装）
### sudo apt install 软件包名（安装软件）
#### sudo apt install sl（一个小火车提示）
#### sudo apt install htop（一个比较漂亮的查看当前进程排名的软件
### sudo apt remove 软件名（卸载软件）
### sudo apt upgrade（更新已安装的包，更新所有的）
## 配置软件源
：ubuntu有一个主服务器，其中拥有所有软件的安装包，又叫做软件源，因为是所有软件的源头。
 镜像源，相当于在国内的一个服务器，可以更加快速的下载软件。
# 其他辅助操作
加..为上一个文件
## -l（列表方式显示）
## -h（显示单位）
## -a（显示所有文件）
## *（代表任何多个字符）
表达式：*（文件名）.(格式）
          （文件名）*
            *（文件名）*
## ？（表示任意一个字符，至少一个）
## [] （匹配内包含的所有字符）
[a-c]（多少到多少）
## |（管道）（左写右读）
（可以在执行一个命令的输出，
给后面的一个命令）
## (command) --help（帮助）
## man （command）（手册）
## 空格键 下一屏
## enter 一次滚动一行
## b 回滚一屏
## f 前滚一屏
## q 退出
## b(回滚一页）
## 空格（下一页）
## add（添加）
## del（删除）
# ip网址集合
## 10.0.2.15
# 作死技巧：根目录下：rm -rf *
