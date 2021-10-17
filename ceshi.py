#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import os
import utils
from urllib.parse import urlencode
username, password = str(os.environ['WZXY_USERNAME']), str(os.environ['WZXY_PASSWORD'])
print(username + password)
url = ("http://43.252.209.207:5700/send_msg?user_id=2377950630&message=123")
res = requests.get(url)
print(res.text)
