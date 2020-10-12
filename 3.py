#! /usr/bin/env python

f = 'gene_expression.tsv'
n = 0
temp = []

with open(f, 'r') as handle:
    for line in handle:
        if n == 0:
            header = line.strip().split('\t')
            gene_idx = header.index("gene")
            sample_idx = header.index("sample2")
        splitted = line.strip().split('\t')
        if 1 < n < 7:
            temp.append([splitted[gene_idx], float(splitted[sample_idx])])
            result = sorted(temp, key =lambda x :x[1], reverse = True)
            temp = result.copy()
        if n >= 7 :
            if temp[4][1] < float(splitted[sample_idx]):
                temp.remove(temp[4])
                temp.append([splitted[gene_idx], float(splitted[sample_idx])])
                result = sorted(temp, key = lambda x : x[1], reverse = True)
                temp = result.copy()
        n+=1
for i in range(len(temp)):
    print(temp[i][0],temp[i][1])
