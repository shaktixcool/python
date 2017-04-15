temperatures=[10,-20,-289,100]
def cTOf(t):
    if t < -273.15:
        print("This is not possible")
    else:
         f=t*9/5+32
         file =  open("C:\shakti\python\Tempexec.txt",'a')
         file.write(str(f)+"\n")
         return f
for t in temperatures:
    print(cTOf(t))
