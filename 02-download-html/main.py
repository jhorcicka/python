#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

URL = 'http://localhost:8080/python/index.html'

def without_javascript():
  response = requests.get(URL)
  soup = BeautifulSoup(response.text)
  result = soup.find(id="intro-text")
  print(result)

def with_javascript():
  session = HTMLSession()
  response = session.get(URL)
  response.html.render()
  print(response.html.html)

if __name__ == '__main__':
  with_javascript()
