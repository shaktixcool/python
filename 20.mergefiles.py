read=''
def merge_file(read):
    list = ["C:\\shakti\\python\\file1.txt","C:\\shakti\\python\\file2.txt","C:\\shakti\\python\\file3.txt"]
    for i in list:
        print(i)
        openfile =  open('%s' %i,'r')
        openfile.seek(0)
        read = openfile.readlines()
        openfile.close()
    print(read)
    return read
        #openfile.close()
#merge_file(read)

newfile = open("C:\\shakti\\python\\newfile123.txt",'a')
read1 = merge_file(read)
content = newfile.write(str(read1) + "\n")
newfile.close()
