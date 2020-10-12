#! /usr/bin/env python

f = 'refGene.txt'

result = []

with open(f, 'r') as handle:
    for line in handle:
        header = line.strip().split('\t')
        gene = header[1]
        exonstartcol = header[9].split(',')
        exonendcol = header[10].split(',')
        exonstartcol.pop(-1)
        exonendcol.pop(-1)
        exonstart = list(map(int, exonstartcol))
        exonend = list(map(int, exonendcol))
        sumvalue = 0
        while exonend:
            exon = exonend[0]-exonstart[0]
            exonstart.pop(0)
            exonend.pop(0)
            sumvalue += exon
        result.append([gene,sumvalue])
    maxValue = result[0][1]
    for i in range(len(result)):
         if maxValue < result[i][1]:
            maxValue = result[i][1]
            temp = []
            temp.append([result[i][0],result[i][1]]) 

print(temp[0][0],'\t',temp[0][1])
                  
           
