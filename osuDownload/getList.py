from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from selenium.webdriver.common.by import By


def getBeatmapList(download_station: int, urls: list, search_url: str, url_name: list) -> None:  # 网页抓取铺面信息

    emp_data = pd.DataFrame()

    options = webdriver.ChromeOptions()
    options.add_argument('-ignore-certificate-errors')
    options.add_argument('-ignore -ssl-errors')
    options.add_argument('-ignore -net_error')
    options.add_argument('--start-maximized')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(search_url)

    input('在网页上设置筛选参数（设置好要点一下search），在此页面Enter开始爬取谱面（后面还有一个要输入的参数）')
    elementNumber = input('（输入整数）设置爬取谱面数量：(X) *18倍，不可为0')
    while elementNumber == '':
        elementNumber = input('（输入整数）设置爬取谱面数量：(X) *18倍，不可为0')
    print('正在爬取谱面信息，切勿关闭网页以及进行其他操作直到网页关闭为止')

    for _ in range(int(elementNumber)):
        dom = etree.HTML(driver.page_source)
        link = dom.xpath('//*[@class="ten wide column beatmap-info"]//a/@href')
        beatmap_id = dom.xpath('//*[@id="beatmap-container"]//div/@data-id')
        message = dom.xpath('//*[@class="row truncate beatmap-title-row"]/div/@title')
        downLoadUrl = [urls[download_station] + _ for _ in beatmap_id]
        min_len = min(len(beatmap_id), len(link), len(message))
        if min_len == 0:
            print('当前页面未爬取到谱面数据，可能已到达最后一页')
            break
        save_link = pd.DataFrame({'beatmap_id': beatmap_id[:min_len],
                                  'link': link[:min_len],
                                  'message': message[:min_len],
                                  'downLoadUrl': downLoadUrl[:min_len]
                                  })
        emp_data = pd.concat([emp_data, save_link])

        try:
            next_page = driver.find_element(
                By.CSS_SELECTOR,
                '#beatmap-container > div.one.column.row.infinite-scroll > div > span > a:nth-child(3)')
            driver.execute_script('arguments[0].click()', next_page)
            time.sleep(5)
        except:
            break
    driver.close()

    fileName = input('自定义谱面信息文件名称（记录筛选信息）')
    while fileName.strip() == '':
        fileName = input('文件名称不能为空，请重新输入')
    emp_data = emp_data.drop_duplicates(['beatmap_id'])
    emp_data.to_excel(f'./download_xml/{fileName}.xlsx', index=False)
    emp_data['downLoadUrl'].to_csv(f'./download_xml/{fileName}_{url_name}.txt',
                                   index=False, header=False)
    print('已生成文档')
