import multitasking
import signal
import requests
from tqdm import tqdm
import pandas as pd
import time
import os


@multitasking.task
def download(url: str, file_name: str, download_path: str) -> None:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers, stream=True)
    # 一块文件的大小
    chunk_size = 1024
    with open(os.path.join(download_path, file_name), mode='wb') as f:
        # 写入分块文件
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)


def pythonDownloadLauncher(fileName: str, fileNumber: int, path: str) -> None:
    signal.signal(signal.SIGINT, multitasking.killall)
    beatmapData = pd.read_excel(f'./download_xml/{fileName}', sheet_name=0)
    beatmap_id = beatmapData['beatmap_id']
    downLoadUrl = beatmapData['downLoadUrl']

    start_time = time.time()
    for _ in tqdm(range(len(beatmap_id))):
        download(url=downLoadUrl[_], file_name=str(beatmap_id[_]) + '.osz', download_path=path)
        if _ % fileNumber == 0:
            multitasking.wait_for_tasks()

    end_time = time.time()
    print(f'耗时:{int((end_time - start_time) // 60)}分:{int((end_time - start_time) % 60)}秒')
    print('下载结束，谱面已经保存在beatmaps_save文件夹中')
