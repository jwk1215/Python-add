#! /usr/bin/env python

f = 'sample.vcf'

cnt = 0

with open(f,'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        if line.startswith('#'):
            header = line.strip().split('\t')
            filter_idx = header.index("FILTER")
            continue
        splitted =line.strip().split('\t')
        if splitted[filter_idx] == "PASS":
            cnt +=1

print(cnt)
