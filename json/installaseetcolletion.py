#install asset collection

import requests
import simplejson
#import urllib3
#from urllib.parse import urljoin

oauthTokenResponse = requests.post(
    'https://login.run.pivotal.io/oauth/token?grant_type=password&client_id=cf',
    data={'username': 'shaktixcool@gmail.com', 'password': 'Aachu98@', 'client_id': 'cf'},
    auth=('cf', '')
)
authorization = oauthTokenResponse.json()['token_type'] + ' ' + oauthTokenResponse.json()['access_token']

orgsResponse = requests.get(
    "https://run.pivotal.io/api/v0/installation_asset_collection",
    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
)
orgsresp = orgsResponse.text
print (orgsresp)
