from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import re


def getBeatmapListPP(download_station: int, urls: list, search_url: str, url_name: list) -> None:

    options = webdriver.ChromeOptions()
    options.add_argument('-ignore-certificate-errors')
    options.add_argument('-ignore -ssl-errors')
    options.add_argument('-ignore -net_error')
    options.add_argument('--start-maximized')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(search_url)

    input('在网页上设置筛选参数，在此页面Enter开始爬取谱面（后面还有输入项）')
    beatMapCounts = input('（输入整数）设置爬取谱面数量：（大范围筛选会导致去重后谱面数量大幅减少）')
    while beatMapCounts == '':
        beatMapCounts = input('（输入整数）设置爬取谱面数量：（大范围筛选会导致去重后谱面数量大幅减少）')
    beatMapCounts = int(beatMapCounts)
    zoomRate = 8 / beatMapCounts
    print('正在爬取谱面信息，切勿关闭网页以及进行其他操作直到网页关闭为止')
    driver.execute_script(f"document.body.style.zoom='{zoomRate}'")
    time.sleep(beatMapCounts / 20)

    dom = etree.HTML(driver.page_source)
    title_links = dom.xpath('//a[starts-with(@href, "https://osu.ppy.sh/beatmaps/") and text()]')

    beatmap_ids = []
    link_hrefs = []
    messages = []

    for link in title_links:
        href = link.get('href')
        bm_id_match = re.search(r'/beatmaps/(\d+)', href)
        if bm_id_match:
            bm_id = bm_id_match.group(1)
            beatmap_ids.append(bm_id)
            link_hrefs.append(href)
            messages.append((link.text or '').strip())

    downLoadUrl = [urls[download_station] + bm_id for bm_id in beatmap_ids]

    min_len = min(len(beatmap_ids), len(link_hrefs), len(messages))
    if min_len == 0:
        print('未爬取到任何谱面数据，请检查网页结构或筛选条件')
        driver.close()
        return
    if min_len < beatMapCounts:
        print(f'实际爬取到的谱面数据不足：仅 {min_len} 个（目标 {beatMapCounts} 个）')

    save_link = pd.DataFrame({'beatmap_id': beatmap_ids[:min_len],
                              'link': link_hrefs[:min_len],
                              'message': messages[:min_len],
                              'downLoadUrl': downLoadUrl[:min_len]})

    fileName = input('自定义文件名称（记录筛选信息）')
    while fileName.strip() == '':
        fileName = input('文件名称不能为空，请重新输入')
    save_link = save_link.drop_duplicates(['beatmap_id'])
    save_link.to_excel(f'./download_xml/{fileName}.xlsx', index=False)
    save_link['downLoadUrl'].to_csv(f'./download_xml/{fileName}_{url_name}.txt',
                                    index=False, header=False)

    print('已生成文档')
    driver.close()
