# PKUelective
PKU选课自动刷新工具
### 用法
#### elective.py:

1、选课页面找到想抢的课->找到最右边的刷新按钮->右键->审查元素->右键选中的部分->Copy->Copy selector。赋给23行的refreshselector。  
2、填好校园门户的账号密码

#### mail.py:

1、填好自己邮箱(默认163)的账号密码  
运行：python PKUelective.py

#### 配置chromedriver:
1、参考https://blog.csdn.net/JavaLixy/article/details/77874715

程序调用chrome自动刷新，课有空位的时候向邮箱发送邮件  
使用python3 selenium库


