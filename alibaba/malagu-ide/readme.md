# Cellbang IDE

Cellbang IDE 是 [Malagu](https://github.com/cellbang/malagu) + [Theia](https://theia-ide.org/) 实现的 Web IDE，可以部署在 Serverless 平台上。这是一个模板项目，使用该模板项目，我们可以快速部署一个运行在 Serverless 平台上的 Web IDE。本模板以默认部署到阿里云函数计算平台。

## 效果

在线演示网址：[http://ide.cellbang.com](http://ide.cellbang.com)。只有 `/tmp` 目录下可写，其他目录都是只读。

![ide.jpg](https://i.loli.net/2020/10/15/hm9lQHTwp3dLyJR.jpg)

## 原理

从效果图，可以发现我们的 Web IDE 与 Theia IDE 几乎一模一样。原因是我们采用 Theia + Malagu 实现的。Malagu 框架的前后端一体设计灵感来自 Theia IDE，所以 Malagu 可以无缝与 Theia IDE 进行融合。我们甚至可以使用 Malagu 作为基础框架开发 Theia IDE 的扩展。Theia IDE 的扩展与 Malagu 的组件几乎一样。

目前，Serverless 平台对长连接双向通信支持不是很友好，所以 Malagu 在集成 Theia IDE 的时候，将大部分长连接的实现替换了短连接单向通信。对于 Teminal 等对双向通信有强要求的模块，我们并没有适配。

## 使用

### 下载命令行工具

通过 npm 包管理安装：适用于已经预装了 npm 的 Windows、Mac、Linux 平台。

在 Windows、Mac、Linux 平台执行以下命令安装 Serverless Devs Tool工具。

```
$ npm install @serverless-devs/s -g
```

> 说明:   
>  - 如果在 Linux 或 MacOS 下执行该命令报错且报错信息为 Error: EACCES: permission denied，请执行命令 sudo npm install @serverless-devs/s -g。   
>  - 如果安装过程较慢，可以考虑使用淘宝 npm 源，安装命令为 npm --registry=https://registry.npm.taobao.org install @serverless-devs/s -g。

安装完成之后，在控制终端执行 s 命令查看版本信息。

```
s -v
```


### 开通函数计算并准备相关凭证

这一部非常重要，各位小伙伴们，可以前往：https://fc.console.aliyun.com/ ，来开通函数计算，开通之后，可以进行账号配置：

- 配置账号信息：
    1. 获取账号Id： https://account.console.aliyun.com/#/secure
        ![](https://images.serverlessfans.com/s-tool/zh/start-1.jpg)
    2. 获取密钥信息：https://ram.console.aliyun.com/manage/ak
        ![](https://images.serverlessfans.com/s-tool/zh/start-2.jpg)
    3. 通过`s config add`进行项目配置
        ![](https://images.serverlessfans.com/s-tool/zh/start-3.jpg)

> 重要提示: 云账号AccessKey是您访问阿里云API的密钥，具有该账户完全的权限，请您务必妥善保管！不要通过任何方式(eg, Github)将AccessKey公开到外部渠道，以避免被他人利用而造成 安全威胁 。强烈建议您遵循 阿里云安全最佳实践 ，使用RAM子用户AccessKey来进行API调用。

## 项目部署

 初始化一个模版项目：`s init fc-ide -p alibaba`
    ![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_01.jpg)

- 进入项目：`cd fc-ide`


- 执行：`s deploy`即可进行部署：
    ![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_02.jpg)
    此处选择我们配置好的密钥，按回车继续部署：
    ![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_03.jpg)
    
- 至此，我们完成了简单的函数部署功能。


![nas 演示.gif](https://i.loli.net/2020/10/15/AhUsFuBecJEyWIX.gif)
