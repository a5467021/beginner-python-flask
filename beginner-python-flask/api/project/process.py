'''
Functions for data processing.
'''

import json
import requests
from bs4 import BeautifulSoup


auth_host = 'https://os.ncuos.com'
lib_host = 'http://210.35.251.243'

def GetAuth(username = '', password = ''): # Get token for authenticated uesr operations
    url = auth_host + '/api/user/token'
    req = requests.post(url = url, json = {'username': username, 'password': password})
    auth = {}
    if req.json()['status'] == 1:
        auth['token'] = req.json()['token']
        auth['status'] = 1
    else:
        auth['token'] = ''
        auth['status'] = 0
    return auth

def GetBookList(title = '', page = '1'): # Get the book list from the 
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
        item = item.get_text().split('\n')
        ret[len(ret) + 1] = {
                                'name': item[offset + 0],
                                'author': item[offset + 1],
                                'publisher': item[offset + 2],
                                'call_number': item[offset + 3]
                            }
    return ret