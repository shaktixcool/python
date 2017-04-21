import requests
#import urllib2
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
#print (resp)

#def printResults():
    #jsonData = resp.replace("'", '"')
jsonData = simplejson.loads(resp)
    #print (jsonData['results
    #response = json.loads(response)
for doc in jsonData['resources']:
    metadata = str(print(doc['metadata']))
#print (metadata)
        #return metadata
    #print jsonToPython['name']

    #if "metadata" in jsonData["resources"]:
    #    resp1 = print(jsonData["resources"]["metadata"])
    #    print (resp1)
#meta = str(printResults())
#print (meta)
#metadata1 = metadata.text
with open("C:\shakti\python\json\cf.txt",'w') as f:
    f.write(str(metadata))
