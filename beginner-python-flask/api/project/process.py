'''
Functions for data processing.
'''

import json
import requests
from bs4 import BeautifulSoup
from project.db import *


#auth_host = 'https://os.ncuos.com'
lib_host = 'http://210.35.251.243'

#def GetAuth(username = '', password = ''): # Get token for authenticated uesr operations
#    url = auth_host + '/api/user/token'
#    req = requests.post(url = url, json = {'username': username, 'password': password})
#    auth = {}
#    if req.json()['status'] == 1:
#        auth['token'] = req.json()['token']
#        auth['status'] = 1
#    else:
#        auth['token'] = ''
#        auth['status'] = 0
#    return auth

def GetBookInfo(marc_no): # Get specific information about a book
    url = lib_host + '/opac/item.php?marc_no=' + marc_no
    res = requests.get(url)
    offset = 0
    soup = BeautifulSoup(res.content.decode(res.encoding), 'html.parser')
    raw_info = soup.findAll('div', attrs = {'id': 'item_detail'})
    soup = BeautifulSoup(str(raw_info), 'html.parser')
    info = soup.findAll('dl')
    ret = {
              'bookname': info[0].find('dd').get_text().split('/')[0],
              'author': info[0].find('dd').get_text().split('/')[1],
              'publisher': ''.join(info[1].find('dd').get_text().split(',')[:-1]),
              'pub_time': info[1].find('dd').get_text().split(',')[-1],
              'ISBN': info[2].find('dd').get_text().split('/')[0],
              'price': info[2].find('dd').get_text().split('/')[1]
          }
    return ret

def GetBookList(title = '', page = '1'): # Get the book list from the library
    url = lib_host + '/opac/openlink.php'
    params = {
                 'title':         title,
                 'page':          page,
                 'location':      'ALL',
                 'doctype':       'ALL',
                 'match_flag':    'forward',
                 'displaypg':     '40',
                 'showmode':      'table',
                 'onlylendable':  'no',
                 'with_ebook':    'off'
             }
    offset = 2
    res = requests.get(url = url, params = params)
    soup = BeautifulSoup(res.content.decode(res.encoding), 'html.parser')
    table = soup.findAll('table', attrs = {'id': 'result_content'})
    ret = {}
    soup = BeautifulSoup(str(table[0]), 'html.parser')
    items = soup.findAll('tr', attrs = {'bgcolor': "#FFFFFF"})
    for item in items:
        marc_no = item.find('a', attrs = {'target': '_blank'}) .attrs['href']
        item = item.get_text().split('\n')
        ret[len(ret) + 1] = {
                                'name': item[offset + 0],
                                'author': item[offset + 1],
                                'marc_no': marc_no.split('=')[-1],
                                'publisher': item[offset + 2],
                                'call_number': item[offset + 3]
                            }
    return ret