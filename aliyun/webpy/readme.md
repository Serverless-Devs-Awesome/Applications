# 阿里云函数计算：Web.Py

通过该应用，您可以简单快速的创建一个Web.Py框架到阿里云函数计算服务。

- 下载命令行工具：`npm install -g @serverless-devs/s`

- 配置账号信息，以阿里云为例。
    1. 获取账号Id： https://account.console.aliyun.com/#/secure
        ![](https://images.serverlessfans.com/s-tool/zh/start-1.jpg)
    2. 获取密钥信息：https://ram.console.aliyun.com/manage/ak
        ![](https://images.serverlessfans.com/s-tool/zh/start-2.jpg)
    3. 通过`s config add`进行项目配置
        ![](https://images.serverlessfans.com/s-tool/zh/start-3.jpg)

- 初始化一个模版项目：`s init webpy -p alibaba`
- 进入项目：`cd webpy`

- 执行：`s deploy`即可进行部署：
    ![](https://images.serverlessfans.com/s-tool/zh/start-6.jpg)
    此处选择我们配置好的密钥，按回车继续部署：
    ![](https://images.serverlessfans.com/s-tool/zh/start-5.jpg)
    稍等片刻，即可看到成功部署，此时我们来到线上，即可看到我们的函数，例如：
    ![](https://images.serverlessfans.com/s-tool/zh/start-7.jpg)
    
- 至此，我们完成了简单的函数部署功能。