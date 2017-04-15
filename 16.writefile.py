file = open("C:\shakti\python\example.txt",'w')
items = ["Line11","Line12","Line13"]
for j in items:
    content2 = file.write(j+"\n")
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    content = file.write("Line %d\n" %i)
file.close()
file1 = open("C:\shakti\python\example.txt",'r')
file1.seek(0)
content1 = file1.readlines()
print(content1)
file1.close()
