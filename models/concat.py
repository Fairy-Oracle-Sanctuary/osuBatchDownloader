import os
import pandas as pd


def Concat() -> None:
    listName = os.listdir('./download_xml')
    listXlsx = [_ for _ in listName if 'xlsx' in _]
    dictXlsx = {_: listXlsx[_] for _ in range(len(listXlsx))}
    allData = pd.DataFrame()

    print(dictXlsx)
    concatData = input('输入拼接的文件对应的号码，数字间用空格隔开或不隔开')
    SelectData = list(concatData.replace(' ', ''))

    for _ in SelectData:
        tempData = pd.read_excel(f'./download_xml/{dictXlsx[int(_)]}', sheet_name=0)
        allData = pd.concat([allData, tempData])

    allData.drop_duplicates(subset=['beatmap_id'], keep='first', inplace=True)

    fileName = input('输入新文件名')
    allData[['beatmap_id', 'link', 'message', 'downLoadUrl']].to_excel(f'./download_xml/{fileName}.xlsx')
