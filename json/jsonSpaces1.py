import requests
import simplejson
oauthTokenResponse = requests.post(
    'https://login.run.pivotal.io/oauth/token?grant_type=password&client_id=cf',
    data={'username': 'shaktixcool@gmail.com', 'password': 'Aachu98@', 'client_id': 'cf'},
    auth=('cf', '')
)
authorization = oauthTokenResponse.json()['token_type'] + ' ' + oauthTokenResponse.json()['access_token']
#print (authorization)
orgsResponse = requests.get(
    "https://api.run.pivotal.io/v2/organizations",
    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
)
spacesResponse = requests.get(
    "https://api.run.pivotal.io/v2/spaces",
    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
)
appsResponse = requests.get(
    "https://api.run.pivotal.io/v2/apps",
    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
)
orgsresp = orgsResponse.text
file = open("C:\shakti\python\json\cforgs1.txt",'w')
file.seek(0)
orgscontent = file.write(orgsresp)
file.close()
spacesresp = spacesResponse.text
file = open("C:\shakti\python\json\cfspaces1.txt",'w')
file.seek(0)
spacescontent = file.write(spacesresp)
file.close()
appsresp = appsResponse.text
file = open("C:\shakti\python\json\cfapps1.txt",'w')
file.seek(0)
appscontent = file.write(appsresp)
file.close()

jsonorgs = simplejson.loads(orgsresp)
for o in jsonorgs['resources']:
    forgs = open("C:\shakti\python\json\cforgs2.txt",'a')
    nameorgs = o['entity']['name']

    jsonspaces = simplejson.loads(spacesresp)
    for s in jsonspaces['resources']:
        #fspaces = open("C:\shakti\python\json\cfspaces2.txt",'a')
        namespaces = s['entity']['name']
        #fspaces.write(namespaces + "       " +'\n')


        jsonapps = simplejson.loads(appsresp)
        for a in jsonapps['resources']:
            #fapps = open("C:\shakti\python\json\cfapps2.txt",'a')
            nameapps = a['entity']['name']
            bp = a['entity']['detected_buildpack']
            #forgs.write(nameorgs + "       " +namespaces+"          "+nameapps+"       "+bp +'\n')
            if bp == None:
                bp = "default"
                forgs.write(nameorgs + "       " +namespaces+"          "+nameapps+"       "+bp +'\n')
            else:
                forgs.write(nameorgs + "       " +namespaces+"          "+nameapps+"       "+bp +'\n')


    #fo.write(doc['entity']['name']+ "       " + doc['entity']['detected_buildpack']+'\n')
    #fo.write(doc['entity']['detected_buildpack'])

    #fo.write("names")
    #fo.close()
    #for  doc1 in doc['entity']:
        #for name in doc1['name']:
        #print(type(doc))
            #name = print (doc['entity']['name'])
            #bp = print (doc['entity']['name']['detected_buildpack'])
    #metadata = str(doc['name'])
    #print (metadata)
    #filemeta = open("C:\shakti\python\json\cf.txt",'a')
    #filemeta.seek(0)
    #contentmeta = filemeta.write(metadata)
    #filemeta.close()
#with open("C:\shakti\python\json\cf.txt",'w') as f:
#    f.write(str(metadata))"""
