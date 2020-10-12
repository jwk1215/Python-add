#! /usr/bin/env python

f = "sequences.fasta"

dic={"C":0 , "G":0 , "total":0 , "ratio":0}
temp=[]
result=[]

n=0

def calc(n):
    if n!=0:
        dic["ratio"]=(dic["C"] + dic["G"]) / dic["total"]                   
        result.append(dic["ratio"])  
        dic["C"]=0
        dic["G"]=0       
        dic["total"]=0
        dic["ratio"]=0             

with open(f,'r') as handle:
    for line in handle:
        seq = line.strip()
        if line.startswith('>'):          
            temp.append(seq)
            calc(n)
            n +=1
            continue                              

        for i in seq:
            dic["total"] += 1             
            if i in dic: 
                dic[i] += 1       
calc(n)
for i in result:
    print(round(i*100,2))

print(dic)

