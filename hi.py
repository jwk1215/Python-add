#! /usr/bin/env python

f = 'sequences.fasta'

l_seq = []

g_cnt = {"G":0}
c_cnt = {"C":0}

n = 0
A= []

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('>'):
            pass
        else:
            line = line.strip()
            for i in line:
                if i =="G" and n !=0:
                    g_cnt["G"] +=1
                    A.append(g_cnt["G"])
                    #g_cnt["G"] = 
                elif i =="C" and n !=0:
                    c_cnt["C"] +=1
                    #print(c_cnt)
            n +=1
            continue
            
print(g_cnt)
print(c_cnt)
print(A)

        


