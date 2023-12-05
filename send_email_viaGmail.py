import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_gmail(sender_email, sender_password, recipient_email, subject, message):
    # Gmail 的 SMTP 服务器设置
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # 使用 TLS

    # 创建 MIME 邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(message, 'plain'))

    # 建立安全的 SMTP 连接
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # 启动 TLS 加密
    server.login(sender_email, sender_password)  # 登录 Gmail
    server.send_message(msg)  # 发送邮件
    server.quit()  # 关闭连接

    print("Email sent successfully!")

# 使用示例
send_gmail('sj396135505@gmail.com',
           'myjxmpjksgeulixm',
           'sj396135505@gmail.com',
           'Test Email',
           'This is a test email sent via Gmail.')
