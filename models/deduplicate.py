import os
import pandas as pd


def Deduplicate() -> None:
    listName = os.listdir('./download_xml')
    listXlsx = [_ for _ in listName if 'xlsx' in _]
    dictXlsx = {_: listXlsx[_] for _ in range(len(listXlsx))}
    duplicateY = pd.DataFrame()

    print(dictXlsx)
    selectDataX = input('输入去重的文件X对应的号码（只能输入一个数字）')
    duplicateX = pd.read_excel(f'./download_xml/{dictXlsx[int(selectDataX)]}', sheet_name=0)
    print(dictXlsx)
    selectDataY = input('输入去重的文件Y对应的号码（可以输入多个数字，数字间用空格隔开或不隔开）')
    moreSelectDataY = list(selectDataY.replace(' ', ''))

    for _ in moreSelectDataY:
        duplicateCombine = pd.read_excel(f'./download_xml/{dictXlsx[int(_)]}', sheet_name=0)
        duplicateY = pd.concat([duplicateY, duplicateCombine])

    combineData = pd.concat([duplicateX, duplicateY, duplicateY])
    duplicateData = combineData.groupby('beatmap_id').filter(lambda x: len(x) == 1)

    if len(duplicateData) == 0:
        print('去重文件X已经空了！Y里面包含了X的所有谱面')
    else:
        fileName = input('输入新文件名')
        duplicateData[['beatmap_id', 'link', 'message', 'downLoadUrl']].to_excel(f'./download_xml/{fileName}.xlsx')
