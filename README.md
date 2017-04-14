## DjX

### Django xadmin demo project

通过使用xadmin替换django自带的admin管理模块，实现后台管理系统的搭建。

`在使用源码安装xadmin之时需要先于自定义的AUTH_USER_MODEL先执行makemigrations和migrate。`

在定制化后台显示的时候通过用户自定义的user的adminx.py中的BaseSetting和GloablSettings进行相关配置即可。
