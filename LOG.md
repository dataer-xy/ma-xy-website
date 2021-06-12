
## 项目前期调研
* 设计前端界面 OK
* 依据前端界面考虑实现需要的技术 OK

## 开发
* 可以添加一些 表情符号 NO
* 简介 OK
* logo 说明 OK
* 每个part的 readme OK
* mcmc 添加 OK
* 添加部分 pdf OK
* 部分源码迁移到 next 中 OK
* 开发 -- QQ群 561043735 OK
* 用户 -- QQ群 1109375285 OK

* .gitignore 过滤掉资源 OK
* 发布到 github 上 OK
* github 页面描述 OK
* github README.md OK

* 首页 -- 推荐 dataset-xy 的描述再添加一些 OK
* 首页 -- FOOT 协议 以及 logo 版权 OK
* 首页 -- 站长信息 OK
* 首页 --  去掉dataset等信息 OK
* 首页 --  去掉MIT OK
* 首页 --  去掉广告改成商务 OK

* 章节 -- 作者调整（作者要详细分类）OK

* devexp -- 开发说明中的限制去掉 OK

* buildpdf -- 介绍 OK
* buildpdf -- 只重新编译pdf，不改变已有结构 OK


* pdf -- 每个 pdf 页面上设置一个超链接，全浏览器打开。OK
* pdf -- 每个 pdf 加上网址？ 嗯 latex 编译 OK
* pdf -- 每个 pdf 引用都没引用上？ 整体上也没有引用！ 要用BibTex编译bib文档！OK
* pdf -- 水印 OK
* pdf -- 修改整体tex的导言区 OK

<!-- --------------------------------------------------------- -->
## 需要处理的
* ssl 证书过期了
* pdf -- 封面作者调整
* pdf -- 每个 pdf 加上作者？ 嗯 是这样
* 下载整本 以及下载量 (使用第三方免费的) https://tongji.baidu.com/web/welcome/products
* 搜索框不好用了？
* 是否去掉作者 NO

* buildpdf -- 自动编译所有 pdf 并迁移
* script -- 初始化环境/部署 python


* tex 转 html 工具 deepleaning 书用的是什么工具？ OK
  - https://github.com/exacity/deeplearningbook-chinese
  - https://www.deeplearningbook.org/
  - OK https://github.com/coolwanglu/pdf2htmlEX

* pdf 改成 html
* nginx 缓存 html



<!-- --------------------------------------------------------- -->


## 部署

* scripts -- 项目结构说明，中添加项目文件/文件夹/note说明

* cl 在 git 提交之后，自动发布？
* git 之后，使用webhook 来进行自动发布
* readme 清理 OK


* 改为https，并测试移动端 OK
* nginx 单独文件夹 （部署脚本deploy.py也要改）OK
* ssl 证书 单独文件夹 （部署脚本deploy.py也要改）OK

* nginx 同端口 多 server (反向代理) OK?
* nginx https 协议 输入http:也会自动跳转至https页面 OK
* nginx 重启服务(注意kill nginx之后，不能 reload) OK?

* scripts -- 自动部署 fabic OK


# errors 
* nginx -error : OK 
  - nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in


## 疑难杂症
* pdf -- 整体上 pdf 没有引用
* pdf -- 整体编译引用bibtex时，报错 I found no database files---while reading file main.aux

## bib 要复制到 doc 和 main.tex 下


