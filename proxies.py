import requests
try:
    from StringIO import BytesIO
except ImportError:
    from io import BytesIO
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
from time import sleep

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]

'''
http://www.proxz.com/proxy_list_fr_0.html
http://www.fastusproxies.tk
http://www.proxylist.ro/search-free-proxy.php?country=ALL&port=0&anon=Y&ssl=&start=4
http://www.proxylist.ro/search-free-proxy.php?country=ALL&port=0&anon=Y&ssl=&start=5
http://www.proxylist.ro/search-free-proxy.php?country=ALL&port=0&anon=Y&ssl=&start=6
http://www.proxylist.ro/search-free-proxy.php?country=ALL&port=0&anon=Y&ssl=&start=7
http://www.proxylist.ro/search-free-proxy.php?country=ALL&port=0&anon=Y&ssl=&start=8
http://www.proxylist.ro/search-free-proxy.php?country=ALL&port=0&anon=Y&ssl=&start=9
http://www.myiptest.com/staticpages/index.php/Free-Elite-Anonymous-Proxy-lists.html
http://free-proxy-list.net/anonymous-proxy.html
http://letushide.com/filter/all,ntp,all/list_of_free_None_Transparent_proxy_servers
http://letushide.com/filter/all,ntp,all/2/list_of_free_None_Transparent_proxy_servers
http://letushide.com/filter/all,ntp,all/3/list_of_free_None_Transparent_proxy_servers
http://letushide.com/filter/all,ntp,all/4/list_of_free_None_Transparent_proxy_servers
http://letushide.com/filter/all,ntp,all/5/list_of_free_None_Transparent_proxy_servers
http://www.samair.ru/proxy/time-01.htm
http://www.samair.ru/proxy/time-02.htm
http://www.samair.ru/proxy/time-03.htm
http://www.samair.ru/proxy/time-04.htm
http://www.samair.ru/proxy/time-05.htm
http://atomintersoft.com/high_anonymity_elite_proxy_list
http://atomintersoft.com/anonymous_proxy_list
http://www.proxynova.com/proxy-server-list/country-us/
http://www.proxynova.com/proxy-server-list/country-br/
'''

def getProxyList():
    # Retrieve latest proxies
    url = 'https://www.sslproxies.org/'
    header = {'User-Agent': str(ua.random)}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    proxies_table = soup.find(id='proxylisttable')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
        })

    return proxies

def getProxyList2(proxies):
    # Retrieve latest proxies
    try:
        url = 'https://free-proxy-list.net'
        header = {'User-Agent': str(ua.random)}
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'lxml')
        proxies_table = soup.find("table", {"class": "bg"})
        #print(proxies_table)
        # Save proxies in the array
        for row in proxies_table.find_all("tr", {"class": "cells"}):
            google = row.find_all('td')[5].string
            if google == "yes":
                #print(row.find_all('td')[1].string)
                proxies.append({
                    'ip': row.find_all('td')[1].string,
                    'port': row.find_all('td')[2].string
                })
    except:
        print("broken")
    # Choose a random proxy
    try:
        url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'
        header = {'User-Agent': str(ua.random)}
        response = requests.get(url, headers=header)
        textArray = response.text.splitlines()
        
        for row in textArray:
            items = row.split(":")
            
            proxies.append({
                'ip': items[0],
                'port': items[1]
            })
    except:
        print("broken")

    return proxies

def getProxy():
    proxies = getProxyList()
    proxies = getProxyList2(proxies)
    proxy = random.choice(proxies)
    print(proxies)
    return proxy

print(getProxy())
