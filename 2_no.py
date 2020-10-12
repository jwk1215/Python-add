#! /usr/bin/env python

f1 = 'gene.txt'
f2 = 'data.txt'

temp = []
dic = {}

with open(f2, 'r') as handle:
    for line in handle:
        splitted = line.strip().split('\t')
        temp.append(splitted)
    for i in range(len(temp)):
        dic.setdefault(temp[i][0],temp[i][1])   

with open(f1, 'r') as handle:
    for line in handle:
        gene = line.strip()
        value = dic.get(gene)
        if value != None:
            print(gene, value)
        else:
            print(gene, 'NA')       
        
with open(f1, 'r') as handle:
    for line in handle:
        gene = line.strip()
        search = "N"
        for i in range(len(temp)):
            if gene == temp[i][0]:
                print(gene, temp[i][1])
                search = "Y"
        if search == "N":
            print(gene, "NA")

            

            
        
            
        

