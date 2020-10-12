#! /usr/bin/env python
#pgm_id = kmer.py
#import sys

#in_pos=int(sys.argv[1]);
s_cnt=0


in_pos=3
with open('d:\\python_work\\text1.txt','r') as f:

    for line_value in f:
        str_len=len(line_value)
        str_val=line_value
        for i in range(0,len(str_val)-1):
            i_str1=""
            i_str2=""            
            i_str1=str_val[i:i+2]
            i_str2=str_val[i+4:i+5] 
            i_str2+=str_val[i+3:i+4]  
            search_str=str_val[i:i+5] 
#            print("str=",i_str1,i_str2)                                         
            if i_str1 == i_str2:
                print("search_str = ",search_str)    
                s_cnt += 1                
#                print("count= ",s_cnt)

print("") 
print("###############") 
print("## 작업결과 ##")                                             
print("## 검색수 = ",s_cnt)



