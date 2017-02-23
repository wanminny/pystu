




# 检查包的方式如下：
#
# >>> import email
# >>> dir(email)
# ['Charset', 'Encoders', 'Errors', 'FeedParser', 'Generator', 'Header', 'Iterator
# s', 'LazyImporter', 'MIMEAudio', 'MIMEBase', 'MIMEImage', 'MIMEMessage', 'MIMEMu
# ltipart', 'MIMENonMultipart', 'MIMEText', 'Message', 'Parser', 'Utils', '_LOWERN
# AMES', '_MIMENAMES', '__all__', '__builtins__', '__doc__', '__file__', '__name__
# ', '__package__', '__path__', '__version__', '_name', 'base64MIME', 'email', 'im
# porter', 'message_from_file', 'message_from_string', 'mime', 'quopriMIME', 'sys'
# ]
# >>>

## 检查 path    import sys    print(sys.path)



#coding=utf-8

#### 有一个错误容易犯;就是文件名称不能是 email.py 否则会报错
## 参考 http://blog.csdn.net/spring292713/article/details/45077649
# 该错误在IDE中导入包的时候就没有提示;这个时候就不寻常..呵呵.以后要注意类似的情况了~~


import smtplib
from email.mime.text import MIMEText
# import email


#发送邮件的列表 测试OK!
mailto_list=['41622358@qq.com']
mail_host="smtp.163.com"  #设置服务器
mail_user="wanminny"    #用户名
mail_pass="51dh123456"   #口令
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me="成长贴小助手"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')

    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False

send_mail(mailto_list,'python email demo',' email !!!!!')