#!/usr/bin/env python3
import requests
from utils import argParse

# Or choose an another mediawiki (mw) API: https://www.mediawiki.org/wiki/API:Client_code#Python

_USAGE = ''
baseurl = 'http://en.wikipedia.org/w/api.php'
params = {'prop': 'redirects',
		   'action': 'query',
		   'format': 'json',
}
params.update(argParse(_USAGE))

resp = requests.get(baseurl, params = params)
data = resp.json()

redirects = [ii['title'] for i in data['query']['pages'].values() for ii in i['redirects']]

print('\n'.join(redirects))

