from pydantic import BaseSettings


class UrlSetting(BaseSettings):
    Urls: list = ['https://chimu.moe/d/',
                  'https://kitsu.moe/api/d/',
                  'https://txy1.sayobot.cn/beatmaps/download/novideo/']

    SearchUrl: list = ['https://osu-pps.com/#/mania/maps',
                       'https://osusearch.com/']

    SampleUrl: str = 'https://txy1.sayobot.cn/beatmaps/download/novideo/952409?server=auto'

    urlName: list = ['Chimu', 'Kitsu', 'Sayo']
