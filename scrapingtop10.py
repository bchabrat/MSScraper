from selenium import webdriver
import time
import pandas as pd
from proxy import proxy_driver



def scrapingtop10(cat_id,list_proxies,funds_ids):
    i = 0
    data = []

    for fund in funds_ids:
        print("working on " + fund['name'] + ". Loop number: " + str(i))
        urlPage = f'https://www.morningstar.co.uk/Common/funds/snapshot/PortfolioSAL.aspx?Site=uk&FC={fund["id"]}&IT=FO&LANG=en-GB'

        try:
            driver = proxy_driver(list_proxies)
            driver.get(urlPage)
            time.sleep(15)
            results = driver.find_element_by_xpath("//html//body//div//sal-components-mip-holdings//div//div[2]//div//div[2]//div[2]//div[1]//div[1]//table[1]//tbody")
            stocks = results.find_elements_by_tag_name("td")
            for stock in stocks:
                data.append({'fund': fund['name'], 'stock': stock.text})
            i += 1
            driver.close()
            print(fund['name'] + ". Loop number: " + str(i) + " done!")
        except Exception as ex:
            print("an exception occured: ", ex)

    df = pd.DataFrame(data)
    df.to_csv("./final_data/final_data_"+cat_id)
