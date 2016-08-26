#!/usr/bin/env python3
import requests
from utils import argParse

# Or choose an another mediawiki (mw) API: https://www.mediawiki.org/wiki/API:Client_code#Python

_USAGE = ''
baseurl = 'http://wikipedia.org/w/api.php'
params = {'prop': 'redirects',
          'action': 'query',
          'format': 'json',
}
params.update(argParse(_USAGE))

if params.get('lang'):
    baseurl = baseurl.replace('wikipedia', params['lang']+'.wikipedia')
    del params['lang']

resp = requests.get(baseurl, params = params)
data = resp.json()

try:
    redirects = [ii['title'] for i in data['query']['pages'].values() for ii in i['redirects']]
except KeyError:
    print ('No redirections')
    exit()

print('\n'.join(redirects))

