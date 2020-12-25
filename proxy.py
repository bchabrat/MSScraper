from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

def get_proxies():
    driver = webdriver.Firefox(executable_path='/home/bastien/geckodriver')
    driver.get("https://free-proxy-list.net/")
    time.sleep(20)

    proxies_to_return = []
    proxies = driver.find_elements_by_css_selector("tr[role='row']")
    for p in proxies:
        result = p.text.split(" ")

        if result[-1] == "yes":
            proxies_to_return.append(result[0]+":"+result[1])

    driver.close()
    return proxies_to_return


def proxy_driver(pxy):
    proxy = Proxy({
        'proxy_type' : ProxyType.MANUAL,
        'http_proxy' : pxy,
        'ssl_proxy' : pxy
    })
    driver = webdriver.Firefox(proxy=proxy, executable_path='/home/bastien/geckodriver')
    return driver
