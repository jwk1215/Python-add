#! /usr/bin/env python

#Palindromic sequence를 판별하는 프로그램을 작성하세요
#input()함수를이용해sequence를 입력받음


seq = input('서열을 입력하세요. :')

pal = ""

for i in seq:
    pal += i
if pal[::1]==seq[::-1]:
    print('회문구조 서열입니다.')
        


