import requests
import simplejson

oauthTokenResponse = requests.post(
    'https://login.run.pivotal.io/oauth/token?grant_type=password&client_id=cf',
    data={'username': 'shaktixcool@gmail.com', 'password': 'Aachu98@', 'client_id': 'cf'},
    auth=('cf', '')
)
authorization = oauthTokenResponse.json()['token_type'] + ' ' + oauthTokenResponse.json()['access_token']

orgsResponse = requests.get(
    "https://api.run.pivotal.io/v2/organizations",
    headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
)
orgsresp = orgsResponse.text
file = open("C:\\shakti\\python\\json\\files\\cforgs1.txt",'w')
file.seek(0)
orgscontent = file.write(orgsresp)
file.close()

jsonorgs = simplejson.loads(orgsresp)
for o in jsonorgs['resources']:
    forgs = open("C:\\shakti\\python\\json\\files\\cforgs2.txt",'w')
    nameorgs = o['entity']['name']
    guidorg = o['metadata']['guid']
    #forgs.write(nameorgs + "       " +spaceurl+'\n')
    forgs.write(guidorg+'\n')
    #print (spaceurl)
    file.close()
    forgs1 = open("C:\\shakti\\python\\json\\files\\cforgs2.txt",'r')
    #file.seek(0)
    content = forgs.readlines()
    #print (content)
    for i in content:
        #print (i)
        #j = "http://api.run.pivotal.io" + urllib3.quote(i)
        #j = ("https://api.run.pivotal.io/v2/organizations/{0}/spaces".format(i.strip('\n')))
        #print (j)
        #print (type (i))
        spacesResponse = requests.get("https://api.run.pivotal.io/v2/organizations/{0}/spaces".format(i.strip('\n')),
            headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
        )
        spacesresp = (spacesResponse.text)
        #print (spacesresp)
        file = open("C:\\shakti\\python\\json\\files\\cfspaces1.txt",'a')
        spacescontent = file.write(spacesresp)
        file.close()
        jsonspaces = simplejson.loads(spacesresp)
        for s in jsonspaces['resources']:
                fspaces = open("C:\\shakti\\python\\json\\files\\cfspaces2.txt",'a')
                namespaces = s['entity']['name']
                guidspace = s['metadata']['guid']
                #fspaces.write(namespaces + "       "+appsurl +'\n')
                fspaces.write(guidspace+'\n')
                #print (guidspace)
                fspace1 = open("C:\\shakti\\python\\json\\files\\cfspaces2.txt",'r')
                content1 = fspace1.readlines()
                for j in content1:
                        #print (j)

                        appsResponse = requests.get(
                        "https://api.run.pivotal.io/v2/spaces/{0}/apps".format(j.strip('\n')),
                        headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': authorization}
                        )
                        appsresp = appsResponse.text
                        #print (appsResponse)

                        file = open("C:\\shakti\\python\\json\\files\\cfapps1.txt",'a')
                        file.seek(0)
                        appscontent = file.write(appsresp)
                        file.close()
                        jsonapps = simplejson.loads(appsresp)
                        for a in jsonapps['resources']:
                                fapps = open("C:\\shakti\\python\\json\\files\\cfapps2.txt",'a')
                                nameapps = a['entity']['name']
                                bp = a['entity']['detected_buildpack']
                                #fapps.write(nameapps + "       "+bp +'\n')
                    #forgs.write(nameorgs + "       " +namespaces+"          "+nameapps+"       "+bp +'\n')
                                if bp == None:
                                    bp = "default"
                                    fapps.write(nameorgs + "       " +namespaces+"          "+nameapps+"       "+bp +'\n')
                                else:
                                    fapps.write(nameorgs + "       " +namespaces+"          "+nameapps+"       "+bp +'\n')


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
