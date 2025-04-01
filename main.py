from utils.init import init
from utils.run import run
from utils.send_email import EmailServer

vars = 'var.json'
salt = "123456" # 盐
username, password, from_email, to_email,token,email_token= init(vars,salt)
server = EmailServer("smtp.qq.com", 465, email_token) # 邮件服务

run(username, password, salt, vars,from_email, to_email, server,token)

# input("按回车键退出...")
