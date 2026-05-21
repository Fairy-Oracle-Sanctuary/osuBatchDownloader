import os


def getLocalFileName() -> str:
    getName = os.listdir('./download_xml')
    xlsxData = [_ for _ in getName if 'xlsx' in _]

    xlsxDict = {}
    for _ in range(len(xlsxData)):
        xlsxDict[_] = xlsxData[_]
    print(xlsxDict)

    selectData = input('输入需要下载的文件对应的号码')
    return xlsxDict[int(selectData)]
