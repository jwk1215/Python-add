#! /usr/bin/env python

f = 'sample.fasta'

temp = []
dic ={}
result = []
hi =""

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        for i in line:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] =1    

    for key,values in dic.items():
        temp.append([key,values])
        result = sorted(temp, key = lambda x : x[1], reverse=True)
        temp = result.copy()
    
    for i in range(5):
        print(temp[i][0],":",temp[i][1])




            

