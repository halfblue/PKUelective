import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "xxxxxxxxxxx@163.com"  # 用户名
mail_pass = ""  # 密码

sender = mail_user
sender_name = "xxxxxxxxxxx@163.com"  # 显示名称
receiver = 'xxxxxxxxxxx@163.com'  
# 自己给自己发，

# 邮件内容随意
message = MIMEText("https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=syllabus&appName=%E5%AD%A6%E7%94%9F%E9%80%89%E8%AF%BE%E7%B3%BB%E7%BB%9F&redirectUrl=http://elective.pku.edu.cn:80/elective2008/agent4Iaaa.jsp/../ssoLogin.do", 'plain', 'utf-8')
message['From'] = "{0}<{1}>".format(sender_name ,sender)
message['To'] = receiver
message['Subject'] = Header("选课", 'utf-8')
def sendmail():
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
        smtpObj.quit()
        smtpObj.close()
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)

