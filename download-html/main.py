#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

URL = 'https://www.firmy.cz'

def with_javascript():
  session = HTMLSession()
  response = session.get(URL)
  response.html.render()
  print(response.html.html)

if __name__ == '__main__':
  with_javascript()
