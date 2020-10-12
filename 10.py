#! /usr/bin/env python

f = 'gene_val.txt'

temp = []
cnt = 0

with open(f, 'r') as handle:
    for line in handle:
        gene = line.strip()
        temp.append(gene)
    result = set(temp)

    for i in result:
        cnt +=1

print(cnt)
        


