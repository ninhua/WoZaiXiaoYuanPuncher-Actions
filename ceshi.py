#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import os
import utils
from urllib.parse import urlencode
username, password = str(os.environ['WZXY_USERNAME']), str(os.environ['WZXY_PASSWORD'])
print(username + password)
