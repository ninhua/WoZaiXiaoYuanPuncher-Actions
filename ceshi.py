#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import os
import utils
from urllib.parse import urlencode
sign_data = {
            "answers": '["0"]',
            "latitude": os.environ['WZXY_LATITUDE'],
            "longitude": os.environ['WZXY_LONGITUDE'],
            "country": os.environ['WZXY_COUNTRY'],
            "city": os.environ['WZXY_CITY'],
            "district": os.environ['WZXY_DISTRICT'],
            "province": os.environ['WZXY_PROVINCE'],
            "township": os.environ['WZXY_TOWNSHIP'],
            "street": os.environ['WZXY_STREET'],
            }
print（sign_data）
url = ("http://43.252.209.207:5700/send_msg?user_id=2377950690&message=" + str（sign_data）)
res = requests.get(url)
print(res.text)
