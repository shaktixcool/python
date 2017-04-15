file = open("C:\shakti\python\list",'r')
content = file.read()
print (content)
file.seek(0)
content = file.readlines()
print (content)
content = [i.rstrip("\n") for i in content]
    #content1 = [i.rstrip("\n")]
print (content)
file.close()
