代码暂时没写注释！（咕咕咕）
代码暂时没写注释！（咕咕咕）
代码暂时没写注释！（咕咕咕）
osuBeatmapDownloader 是一个利用python爬取以下网站获得谱面信息：
https://osu-pps.com/#/mania/maps  ①
https://osusearch.com/  ②
随后调用以下镜像站进行下载：
https://chimu.moe/zh-CN/beatmaps  ③
https://kitsu.moe/  ④
http://v.osu.sh/home/new  ⑤

备注：请事先浏览①②网站，选择能够稳定使用的，以免程序调用浏览器时打不开。（上不去就用魔法）
          默认使用②和⑤的组合，仅在爬取信息时可能需要魔法，下载时国内网可以直连。

第一步：
       安装需求requirements.txt。

第二步：
       在 https://chromedriver.chromium.org/downloads
       下载您当前浏览器版本的chromedriver
       配置方法可以参照以下网址
        (https://blog.csdn.net/zhoukeguai/article/details/113247342)
       Chrome官方网站 
       (https://www.google.cn/chrome/)

第三步：
       首先进入config/setting.py，修改参数。
       然后运行__init__.py，输入1启动谱面抓取，然后会弹出的页面，然后设置网页上的筛选器。
       包括且不限于Gamemode模式、Star难度、Length长度（单位是秒）、CS / Mania keys（重要）、风格、语言等等。
       然后根据python的提示从头到尾完全运行程序。
       最后程序会将下载链接、铺面信息等信息保存至download_xml中，可以选择不同的镜像源下载。

下载1——使用自带下载器的办法：
       使用任意下载器的批量下载功能（推荐IDM：Internet Download Manager），
       选择download_xml文件夹中任意txt文件即可开始批量下载。
       下载完成后可以把所有谱面一口气拖入ous!/Songs/中，进入游戏后刷新即可。
       运行过init.py后，这个文件夹中会生成一个download_xml的文件夹，里面会保存您每次爬取的谱面的信息。
       当您想要重新下载以前筛选过的谱面数据或者运行了__init__.py但是没有立刻下载的时候，
       您可以用任意下载器重新开始下载。

下载2——使用Chrome网页下载的办法：
       config/setting.py中的PauseTime可以设置每个下载任务之间的添加间隔。
       更改config/setting.py中的选项DownloadStyle为该下载器，运行__init__.py，按照指示输入即可开始下载。
       下载好的谱面将会保存在beatmaps_save中。

下载3——使用Python程序下载的办法：
       fileNumber为此项下载专用，意思为同时开始下载的谱面数量。
       更改config/setting.py中的选项DownloadStyle为该下载器，运行__init__.py，按照指示输入即可开始下载。
       下载好的谱面将会保存在beatmaps_save中。

注意事项：
       使用下载2时候，判断下载是否完成的依据是beatmaps_save下是否存在''.crdownload''文件和''.tmp''文件,
       若要使用下载2请在下载前删除该路径下的这类文件（夹），
       下载路径中若存在包含这两个英文字段的文件/夹都会导致下载完成无法跳出（仍然可以手动关闭）。

       使用下载3时，如果将fileNumber的值设置的很大会占用很多内存，有可能会导致崩溃或者下载失败，请知悉。
       遇到任何问题可以使用Ctrl + C打断程序运行。


       
