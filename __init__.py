from config.Setting import Config
from config.UrlFile import UrlSetting
from osuDownload.ChromedownloadLauncher import chromedownloadLauncher
from osuDownload.PythondownloadLauncher import pythonDownloadLauncher
from osuDownload.getList import getBeatmapList
from osuDownload.getListPP import getBeatmapListPP
from models.getLocalFileName import getLocalFileName
from models.deduplicate import Deduplicate
from models.concat import Concat
import pyttsx3
import os


def init():
    path_save = 'download_xml'
    if not os.path.exists(path_save):
        os.makedirs(path_save)
    path_save = 'beatmaps_save'
    if not os.path.exists(path_save):
        os.makedirs(path_save)

    downloadPath = os.path.join(os.getcwd(), path_save)

    engine = pyttsx3.init()
    engine.setProperty('rate', 120)

    Setting = Config()
    BaseInfo = UrlSetting()
    choice = input('输入0启动下载器\n'
                   '输入1启动谱面抓取\n'
                   '输入2启动谱面文件去重（减少重复下载，加快下载速度）\n'
                   '输入3启动谱面文件拼接（合并多次搜索结果一次性下载）\n')
    if choice == '1':

        if Setting.WebSelection == 1:
            getBeatmapList(download_station=Setting.DownloadStation,
                           urls=BaseInfo.Urls,
                           search_url=BaseInfo.SearchUrl[1],
                           url_name=BaseInfo.urlName[Setting.DownloadStation])
        elif Setting.WebSelection == 0:
            getBeatmapListPP(download_station=Setting.DownloadStation,
                             urls=BaseInfo.Urls,
                             search_url=BaseInfo.SearchUrl[0],
                             url_name=BaseInfo.urlName[Setting.DownloadStation])

    elif choice == '0':
        if Setting.DownloadStyle == 0:
            filename = getLocalFileName()
            chromedownloadLauncher(downloadPath=downloadPath,
                                   waitingTime=Setting.PauseTime,
                                   downloadStation=Setting.DownloadStation,
                                   fileName=filename,
                                   urls=BaseInfo.Urls)
            engine.say('下载完成')
            engine.runAndWait()

        elif Setting.DownloadStyle == 1:
            filename = getLocalFileName()
            pythonDownloadLauncher(fileName=filename,
                                   fileNumber=Setting.fileNumber,
                                   path=downloadPath)
            engine.say('下载完成')
            engine.runAndWait()

    elif choice == '2':
        Deduplicate()

    elif choice == '3':
        Concat()

    else:
        init()


if __name__ == '__main__':
    init()
