#! /usr/bin/env python

f = 'sample.vcf'

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        if line.startswith('#'):
            header = line.strip().split('\t')
            chrom_idx = header.index("#CHROM")
            pos_idx = header.index("POS")
            genotype_idx = header.index("SRR000982")
            ref_idx = header.index("REF")
            alt_idx = header.index("ALT")
            continue
        splitted = line.strip().split('\t')
        temp = []
        temp.append(splitted[ref_idx])
        temp.extend(splitted[alt_idx].split(','))
        A = int(splitted[genotype_idx][0])
        B = int(splitted[genotype_idx][2])
        print(splitted[chrom_idx],'\t', splitted[pos_idx], '\t', splitted[genotype_idx][0:3], '\t', temp[A]+"/"+temp[B])

       


