import random, string
vowel = [a,e,i,o,u,y]
consonants = [b,c,d,i,j,k,l,m,n,p,q,r,s,t,v,w,x,z]
letter=vowel+consonants

a = input("Enter either vowel(V)/consonant(C)/letter(L): ")
b = input("Enter either vowel(V)/consonant(C)/letter(L): ")
c = input("Enter either vowel(V)/consonant(C)/letter(L): ")

def generator():
    if a =='V' or a =='v':
