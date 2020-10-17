# Serverless为你写诗

## 前言

随着函数计算发展的速度越来越快，函数计算在更多领域都有着更加有价值的应用。在音视频离处理领域，函数计算凭借着强大的离线处理能力以及按量付费能力，对离线音视频处理有着非常友好的"态度"，在实时处理的场景中，函数计算凭借着超高的性能，极致的弹性，也有着非常傲人的成绩；在人工智能领域，阿里云函数计算虽然表面上和大多数的函数计算产品一样，但是实际上，阿里云的函数计算具有更好的兼容性和包容性，因为其拥有NAS挂载能力，通过NAS挂载，之前很多由于"模型太大"导致代码包无法放到函数计算中的问题，就迎刃而解了；在Web场景下，阿里云的函数计算，更是因为其本身拥有HTTP函数，而让更多的Web应用，变得非常简单，轻松的可以直接放进来。

本应用将会通过函数计算凭借着超高的工程效率，以及具有按量付费的极低的成本，可以让所有的程序员，通过简单的几行指令，部署一个自己的表白神器，用技术为心爱的人写诗，将诗句，整理成图片，发送给心爱的Ta，这是程序员的浪漫，更是技术赋予我们的能力，也是阿里云函数计算的浪漫，祝有情人，终成眷属。

## 下载命令行工具

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


## 开通函数计算并准备相关凭证

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

 初始化一个模版项目：`s init fc-poem -p alibaba`
    ![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_01.jpg)

- 进入项目：`cd fc-poem`


- 执行：`s deploy`即可进行部署：
    ![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_02.jpg)
    此处选择我们配置好的密钥，按回车继续部署：
    ![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_03.jpg)
    
- 至此，我们完成了简单的函数部署功能。

## 项目体验

在浏览器中打开我们的路径地址：
![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_04.jpg)

在输入框写入内容，然后点击生成古诗，稍等片刻（如果没有成功生成，或者长时间没结果，可以重新点击生成），然后即可看到生成的古诗，点击生成图片即可看到图片：

![](http://activity.serverlessfans.com/auto_poem/imgs/auto_poen_05.jpg)

## 思路拓展

这里面虽然说是生成了一个简单的图片，但是实际上，这个是一个人工智能+图像处理的项目。

其中关于人工智能部分：这里是通过对模型的训练，然后通过用户的输入，生成一段古诗词，这一部分的模型也跑在阿里云的函数计算上，但是由于模型太大可能需要NAS等，所以这里就没教大家如何部署这个模型，而是直接提供一个接口给大家使用。这样大家就可以通过最简单，最快速的方法体验到这个项目。

当然，大家在使用过程中，也可以自己对代码进行修改，对图片进行替换，这里只是一个抛砖引玉的过程。

古诗词仅仅是AI推理生成的，是否具有很高的文学价值等，这个我比较才疏学浅，不能判断，但是我相信，随着时代的发展，模型会越来越完善的。我也更相信，随着Serverless的不断发展，函数计算也会有更多，更有趣的小应用。这次是Serverless为你写诗，下次呢？期待每个小伙伴们的"脑洞"！


