# 定时获取拷贝漫画更新

[![check](https://github.com/caolib/check-manga-update/actions/workflows/check_update.yml/badge.svg)](https://github.com/caolib/check-manga-update/actions/workflows/check_update.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/caolib/check-manga-update?logo=github)
![GitHub Release](https://img.shields.io/github/v/release/caolib/check-manga-update?link=https%3A%2F%2Fgithub.com%2Fcaolib%2Fcheck-manga-update%2Freleases)
![GitHub License](https://img.shields.io/github/license/caolib/check-manga-update)

## 1.简介
## 1.简介

使用`Github Actions`定期执行python脚本检查拷贝漫画个人书架的漫画是否更新，并使用邮件通知更新

邮件提醒示例：

![image-20250307194544112](https://s2.loli.net/2025/03/07/dseWfJnl5L4KoaS.png)

## 2.怎么使用
## 2.怎么使用

### 2.1 本地使用

> [!note]
>
> 如果你并**不需要定时检查**，这种方式更适合你

1. clone仓库或下载[压缩包](https://github.com/caolib/check-manga-update/archive/refs/heads/main.zip)到本地

2. 在`data`文件夹下添加一个文件`var.json`，填写你的用户名和密码

   ```json
   {
       "token": "",
       "username": "拷贝的用户名",
       "password": "拷贝的密码",
       "from_email": "",
       "to_email": "",
       "email_token": ""
   }
   ```
   
3. 双击`main.py`即可启动

### 2.2 在github上使用

> 这种方法相对来说较为麻烦，但是可以定时检查并发邮件通知你，先决条件：
>
> 1. 一个开启了SMTP服务的邮箱，用于发送邮件通知你漫画更新了
> 2. 一个拷贝漫画的账号，用于检查你的个人书架是否有更新
> 3. 一个github仓库用于定期运行检查脚本

#### 1.开启邮件SMTP服务

此处使用QQ邮箱，可以参阅这篇文章[邮箱开启SMTP服务](https://clb.pages.dev/2024/12/27/开启SMTP服务/)获取邮箱授权码`EMAIL_TOKEN`

如果要使用其他邮箱服务，需要修改`main.py`文件中的对应邮箱服务的地址和端口，对应授权码如何获取可以上网查询，比如修改为Gmail：

```py
# server = EmailServer("smtp.qq.com", 465, email_token)    # QQ
server = EmailServer("smtp.gmail.com", 465, email_token)   # Gmail
```

#### 2.clone或fork

因为仓库中的`data/comics.json`文件保存了你的书架中最近更新的漫画(上限20个)，所以：

- 如果你不想让别人看到你的个人书架：你可以**Clone**本仓库到本地，然后再推送到你github的私人仓库中(先在github创建一个私有仓库，然后将clone下来的仓库绑定你刚创建的仓库，最后将代码推送上去)

- 如果你不介意别人看到的话：你可以直接**Fork**本仓库(~~我根本不介意的😋~~)

#### 3.添加Secrets

- 进入你的仓库，点击**Settings** 

![image-20241228123435863](https://s2.loli.net/2024/12/28/y2YDdAGHhiW3Bkg.png)

- 在左侧栏找到`Secrets`下的`Actions`，添加图中6个变量，下面有`TOKEN`的获取步骤,其他属性按自己的填就行

![image-20241228123648544](https://s2.loli.net/2024/12/28/CkFaXtLTQbRU5he.png)

| Key         | Value        |
|-------------|--------------|
| TOKEN       | 拷贝 token     |
| USERNAME    | 拷贝 用户名       |
| PASSWORD    | 拷贝 密码        |
| FROM_EMAIL  | 发件人邮箱        |
| TO_EMAIL    | 收件人邮箱，可以发给自己 |
| EMAIL_TOKEN | 邮箱授权码        |

快捷复制:)

```txt
TOKEN
```

```txt
USERNAME
```

```txt
PASSWORD
```

```txt
FROM_EMAIL
```

```txt
TO_EMAIL
```

```txt
EMAIL_TOKEN
```

> [!caution]
>
> 拷贝漫画的Token不是必要的，因为可以用账号发送请求获取Token，那为什么这里还建议用网站的Token呢？因为Actions中使用账号密码获取Token会导致你网站上的Token过期，你就需要在拷贝网站上重新登录才能看漫画
>
> - 如果你设置了正确的Token，会优先使用你设置的Token，否则才会使用账号密码
>
> - 如果你觉得在拷贝网站重新登录并不麻烦，你可以忽略下面获取Token步骤，`TOKEN`变量也无需设置值

获取拷贝漫画的Token：

- 前往[拷貝漫畫](https://www.mangacopy.com/)，登录你的账号

- 按`F12`或右键选择**检查**打开开发者工具

- 打开应用程序一栏，在左侧找到Cookie，复制token的值

- **其实token也不是必须的，只要有用户名和密码可以自动获取，但是自动获取的token会导致你的网站上的token失效，每次自动获取一次token，网站都需要重新登录**

  ![image-20241228124951850](https://s2.loli.net/2024/12/28/un3kYgVO5BENLvF.png)

#### 4.测试

你可以手动触发工作流测试是否能正常工作

![image-20250307200542211](https://s2.loli.net/2025/03/07/l1ZO7XqyFMRvt9J.png)

Actions启动后点击check查看工作流执行情况

![image-20250307200902406](https://s2.loli.net/2025/03/07/UHZo6lhFVT3DMX5.png)


## 3.其他配置

### 3.1 修改触发条件

> [!NOTE] 
>
> 触发条件默认是每隔一段时间触发一次，你可以修改仓库下`.github/workflows/check_update.yml`调整触发频率或时间段，例如修改为：
>
> `- cron: "0 * * * *"` : 每小时触发一次
>
> 最高触发频率是每五分钟一次，注意Actions每个月的[使用额度](https://docs.github.com/zh/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)是有限的，免费版2000分钟/月，一次任务大概20s左右，只要不是很频繁，这个免费额度还是绰绰有余的

```yml
on:
  # 定时触发
  schedule:
    # 每隔30分钟触发一次
    - cron: "*/30 * * * *"
    # 每小时整点触发
    # - cron: "0 * * * *"
```

## 4.计划
## 4.计划

- [x] 可以使用其他邮箱服务
- [x] 项目文件结构优化，抽取函数到多个py文件

**如果对你有帮助的话，不妨给个star⭐**

![](https://counter.seku.su/cmoe?name=check-manga-update&theme=r34)
