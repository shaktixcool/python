import requests
import simplejson
oauthTokenResponse = requests.post(
    'https://login.run.pivotal.io/oauth/token?grant_type=password&client_id=cf',
    data={'username': 'shaktixcool@gmail.com', 'password': 'Aachu98@', 'client_id': 'cf'},
    auth=('cf', '')
)
authorization = oauthTokenResponse.json()['token_type'] + ' ' + oauthTokenResponse.json()['access_token']
#print (authorization)
appsResponse = requests.get(
    "https://api.run.pivotal.io/v2/apps",
    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
)
resp = appsResponse.text
file = open("C:\shakti\python\json\cf1.txt",'w')
file.seek(0)
content2 = file.write(resp)
file.close()

jsonData = simplejson.loads(resp)
#print (resp)
for doc in jsonData['resources']:
    #for  doc1 in doc['entity']:
        #for name in doc1['name']:
        print(type(doc))
            #name = print (doc['entity']['name'])
            #bp = print (doc['entity']['name']['detected_buildpack'])
    #metadata = str(doc['name'])
    #print (metadata)
    #filemeta = open("C:\shakti\python\json\cf.txt",'a')
    #filemeta.seek(0)
    #contentmeta = filemeta.write(metadata)
    #filemeta.close()
#with open("C:\shakti\python\json\cf.txt",'w') as f:
#    f.write(str(metadata))
