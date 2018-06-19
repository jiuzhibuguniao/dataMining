import pickle
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures

import pymysql
import time


def storeDataToMysql():
    test = pymysql.connect(host='39.108.100.28', user='Rooobins', password='19910909kai', db='spiderData', port=3306)
    cursor=test.cursor()
    create_table="""set @sql_create_table=concat('CREATE TABLE IF NOT EXISTS operrecord_',date_format(NOW(),'%y%m%d%H'),
"(
    `distId` varchar(50),`distX` double,`distY` double,`distNum` int,`distance` varchar(50),`bikeIds` varchar(50),`biketype` varchar(50),`type` varchar(50),`boundary` varchar(50)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8");"""
    create_prepare="""PREPARE sql_create_table FROM @sql_create_table;"""
    create_execute="""EXECUTE sql_create_table;"""
    cursor.execute(create_table)
    cursor.execute(create_prepare)
    cursor.execute(create_execute)
    test.commit()
    cursor.close()








def load_url(url, params, timeout, headers=None):
    return requests.get(url, params=params, timeout=timeout, headers=headers).json()


def merge_dicts(*dict_args):
    """
    可以接收1个或多个字典参数
    :param dict_args:
    :return:
    """

    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def mobai1(loc):
    allmobai = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        url = "https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://servicewechat.com/wx80f809371ae33eda/167/page-frame.html"

        }
        data = {
            "longitude": "",
            "latitude": "",
            "citycode": "0351"
        }

        future_to_url = {
            executor.submit(load_url, url,
                            merge_dicts(data, {"longitude": i.split(",")[0]}, {"latitude": i.split(",")[1]}), 60,
                            headers): url for i in loc
        }

        for future in futures.as_completed(future_to_url):
            if future.exception() is not None:
                print(future.exception())
            elif future.done():
                data = future.result()["object"]
                allmobai.extend(data)
    inf = open("/root/end1.txt", 'w+')
    for dic in allmobai:
        for idic in dic:
            inf.write(str(dic[idic])+' ')
        inf.write('\n')
    inf.close()

def mobai2(loc):
    allmobai = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        url = "https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://servicewechat.com/wx80f809371ae33eda/167/page-frame.html"

        }
        data = {
            "longitude": "",
            "latitude": "",
            "citycode": "0351"
        }

        future_to_url = {
            executor.submit(load_url, url,
                            merge_dicts(data, {"longitude": i.split(",")[0]}, {"latitude": i.split(",")[1]}), 60,
                            headers): url for i in loc
        }

        for future in futures.as_completed(future_to_url):
            if future.exception() is not None:
                print(future.exception())
            elif future.done():
                data = future.result()["object"]
                allmobai.extend(data)
    inf = open("/root/end2.txt", 'w+')
    for dic in allmobai:
        for idic in dic:
            inf.write(str(dic[idic])+' ')
        inf.write('\n')
    inf.close()


def getloc1():
    allloc = []
    """利用高德地图API获取太原所有的小区坐标
    http://lbs.amap.com/api/webservice/guide/api/search/#text
    """

    with ThreadPoolExecutor(max_workers=5) as executor:
        url = "http://restapi.amap.com/v3/place/text"
        param = {
            "key": "84ca8f26444f041472f5edcf57272e5e",
            "keywords": "小区",
            "city": "0351",
            "citylimit": "true",
            "output": "json",
            "page": ""
        }

        future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in range(1, 46)}
        for future in futures.as_completed(future_to_url):
            if future.exception() is not None:
                print(future.exception())
            elif future.done():
                data = future.result()["pois"]
                allloc.extend([x["location"] for x in data])

        with open("/root/allloc1.pk", "wb+") as f:
            pickle.dump(allloc, f, True)


def getloc2():
    allloc = []
    """利用高德地图API获取太原所有的小区坐标
    http://lbs.amap.com/api/webservice/guide/api/search/#text
    """

    with ThreadPoolExecutor(max_workers=5) as executor:
        url = "http://restapi.amap.com/v3/place/text"
        param = {
            "key": "84ca8f26444f041472f5edcf57272e5e",
            "keywords": "公交车站",
            "city": "0351",
            "citylimit": "true",
            "output": "json",
            "page": ""
        }

        future_to_url = {executor.submit(load_url, url, merge_dicts(param, {"page": i}), 60): url for i in range(1, 46)}
        for future in futures.as_completed(future_to_url):
            if future.exception() is not None:
                print(future.exception())
            elif future.done():
                data = future.result()["pois"]
                allloc.extend([x["location"] for x in data])

        with open("/root/allloc2.pk", "wb+") as f:
            pickle.dump(allloc, f, True)


if __name__ == "__main__":
    var = 1
    while var == 1:
        getloc1()
        getloc2()

        inf1 = open("/root/allloc1.pk", "rb")
        allloc1 = pickle.load(inf1)
        inf1.close()

        inf2 = open("/root/allloc2.pk", "rb")
        allloc2 = pickle.load(inf2)
        inf2.close()

        mobai1(allloc1)
        mobai2(allloc2)
        storeDataToMysql()
        time.sleep(28800)