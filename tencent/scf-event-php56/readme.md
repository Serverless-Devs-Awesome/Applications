# 腾讯云函数计算：Php5.6 Hello World

通过该应用，您可以简单快速的创建一个运行时为Python3的腾讯云函数计算服务。

- 下载命令行工具：`npm install -g @serverless-devs/s`

- 配置账号信息，以腾讯云为例。
    1. 获取账号信息： https://console.cloud.tencent.com/cam/capi
        ![](https://images.serverlessfans.com/scf-tencent/tencent-start-secret.jpg)
    2. 通过`s config add`进行项目配置
        ![](https://images.serverlessfans.com/scf-tencent/tencent-config.jpg)

- 初始化一个模版项目：`s init php56 -p tencent`
    ![](https://images.serverlessfans.com/s-tool/zh/start-4.jpg)

- 进入项目：`cd php56`

- 执行：`s deploy`即可进行部署：
    ![](https://images.serverlessfans.com/s-tool/zh/start-6.jpg)
    此处选择我们配置好的密钥，按回车继续部署：
    ![](https://images.serverlessfans.com/s-tool/zh/start-5.jpg)
    稍等片刻，即可看到成功部署，此时我们来到线上，即可看到我们的函数。
    
- 至此，我们完成了简单的函数部署功能。