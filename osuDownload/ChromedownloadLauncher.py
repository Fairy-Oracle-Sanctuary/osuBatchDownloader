import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from tqdm import tqdm


def chromedownloadLauncher(downloadPath: str, waitingTime: int, downloadStation: int, fileName: str,
                           urls: list) -> None:
    beatmap_id = pd.read_excel(f'./download_xml/{fileName}', sheet_name=0)['beatmap_id']

    option = webdriver.ChromeOptions()
    prefs = {"download.default_directory": f"{downloadPath}"}
    option.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.minimize_window()
    start_time = time.time()

    for beatmap in tqdm(beatmap_id):
        driver.get(urls[downloadStation] + str(beatmap))
        time.sleep(waitingTime)
    getName = os.listdir(f'{downloadPath}')

    while 'crdownload' in str(getName) or 'tmp' in str(getName):
        time.sleep(waitingTime)
        getName = os.listdir(f'{downloadPath}')
        print('暂停：下载中')

    driver.close()

    end_time = time.time()
    print(f'耗时:{int((end_time - start_time) // 60)}分:{int((end_time - start_time) % 60)}秒')
    successCounter = str(os.listdir(f'{downloadPath}'))
    print(
        f'下载成功{successCounter.count(".osz")}个谱面，下载失败{len(beatmap_id) - successCounter.count(".osz")}个谱面')
    print('下载结束')
