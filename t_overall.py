# encoding: utf-8
"""
@author: wuwei 
@contact: wu.wei@pku.edu.cn

@version: 1.0
@license: Apache Licence
@file: test_overall.py
@time: 18-12-18 下午4:59


"""
import json
import requests


sess = requests.Session()
url = F'http://localhost:9997/api/indicators'


def example_1_upload_file():
    filename = '1.pdf'
    with open(filename, 'rb') as fin:
        content = fin.read()

    res = sess.post(url=url, files={'pdf': content})
    if res.status_code == 200:
        content = json.loads(res.content)['content']
        for i in content:
            print(i, '\n')
    else:
        print(res.status_code)


if __name__ == '__main__':
    example_1_upload_file()
