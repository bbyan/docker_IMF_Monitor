#!/usr/bin/python
# coding:utf-8

import os
import django
from django.db import connection
import logging

import json
import requests

from requests.auth import HTTPBasicAuth

from ConfigParser import SafeConfigParser


config = SafeConfigParser()
config.read("post_zabbix_info.conf")

fmt = config.get('log', 'format', raw=True)
dateFmt = config.get('log', 'dateformat', raw=True)

logging.basicConfig(level=logging.DEBUG, format=fmt, datefmt=dateFmt)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
django.setup()


def execute_query(sql):
    cursor = connection.cursor()  # 获得一个游标(cursor)对象
    cursor.execute(sql)
    rawData = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]
    result = []
    for row in rawData:
        objDict = {}
        # 把每一行的数据遍历出来放到Dict中
        for index, value in enumerate(row):
            objDict[col_names[index]] = value
        result.append(objDict)
        # return json.dumps(result,sort_keys=True)
    return result


def generate_json(query_result):
    data_dict = {'ProvinceID': config.get('json', 'provinceId'), '_DATA_': query_result}
    return data_dict


if __name__ == '__main__':

    url = config.get('post', 'url')
    trigger_status_sql = config.get('json', 'query')

    trigger_status = json.dumps(generate_json(execute_query(trigger_status_sql)), sort_keys=True)
    logging.info(trigger_status)

    # post函数
    try:
        r = requests.post(url, data=trigger_status, timeout=5,
                          auth=HTTPBasicAuth(config.get('post', 'user'), config.get('post', 'password')))
        if r.status_code != 200:
            raise requests.HTTPError(r.text)
        else:
            logging.debug('Post Successful')
    except requests.ConnectionError:
        logging.debug('Connect Faild')
    except requests.HTTPError:
        logging.debug("Post Faild,the current satus is %d", r.status_code)
