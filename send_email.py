import smtplib
from email.mime.text import MIMEText
from email.header import Header

# QQ邮箱SMTP服务器地址及端口
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# 发件人和收件人地址
sender = 'sj396135505@gmail.com'
receiver = 'sj396135505@gmail.com'
# QQ邮箱授权码（不是QQ密码，需要在QQ邮箱设置中获取）
password = 'myjxmpjksgeulixm'

# 创建一封邮件
subject = 'Test email from QQ'
content = 'This is a test email sent from QQ email via Python.'
msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = Header(sender)
msg['To'] = Header(receiver)
msg['Subject'] = Header(subject)

print("Sending Email!")
# 使用SMTP_SSL连接到服务器并发送邮件
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender, password)
    server.sendmail(sender, [receiver], msg.as_string())

print("Email sent successfully!")
