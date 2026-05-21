from pydantic import BaseSettings


class Config(BaseSettings):
    WebSelection: int = 0
    DownloadStation: int = 2
    DownloadStyle: int = 0
    PauseTime: int = 5
    fileNumber: int = 8

    #  抓取谱面信息的修改项
    #  '''WebSelection（）： 0(PP图搜索)——https://osu-pps.com/#/mania/maps，1(全图搜索)——https://osusearch.com/'''

    #  文件保存项（设置保存谱面url的镜像站与下载所使用的镜像站url）
    #  '''DownloadStation： 0——chimu.moe，1——kitsu.moe，2——sayobot.cn'''

    #  下载方式选择（下载器下载专用设置）
    #  '''DownloadStyle： 0——启动Chrome网页下载，1——启动程序下载器'''

    #  页面下载器修改项（Chrome网页下载专用）
    #  '''PauseTime：可以基于您当前的网速适当减小，但是建议保持在3秒以上，表示的是创建下载任务之间的时间间隔'''

    #  程序下载器修改项（程序内部下载专用）
    #  '''fileNumber：同时下载任务的数量'''
    #  '''程序下载默认会保存在文件夹内的beatmaps_xml子文件夹下'''
