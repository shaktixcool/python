import requests
oauthTokenResponse = requests.post(
    'https://login.run.pivotal.io/oauth/token?grant_type=password&client_id=cf',
    data={'username': 'shaktixcool@gmail.com', 'password': 'Aachu98@', 'client_id': 'cf'},
    auth=('cf', '')
)
authorization = oauthTokenResponse.json()['token_type'] + ' ' + oauthTokenResponse.json()['access_token']
print (authorization)
appsResponse = requests.get(
    "https://api.run.pivotal.io/v2/apps",
    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
)
resp = str(appsResponse.text)
file = open("C:\shakti\python\cf.txt",'w')
content2 = file.write(resp)
