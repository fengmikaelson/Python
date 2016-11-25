﻿# -*- coding: utf-8 -*-
import string
import stringprep
import httplib2
import json
import sys

arr=[0,1,2,3,4,5,6,7,8,9]
num1=[6,0,8,7]
num2=[5,1,7,3]
num3=[1,3,5,8]
num4=[3,8,2,5]
num5=[2,5,3,1]
allnum=[num1,num2,num3,num4,num5]
print("原始输入:")
print(allnum)
print("\n")
#获取密码每一位的可能数字集合
r1=[]
r2=[]
r3=[]
r4=[]
real = [r1,r2,r3,r4]
#i=0;i<4;i++
for i in range(0, 4):
    for j in arr:
        if(j == num1[i]):
            continue
        if(j == num2[i]):
            continue
        if(j == num3[i]):
            continue
        if(j == num4[i]):
            continue
        if(j == num5[i]):
            continue
        real[i].append(j)
print("每一位密码可能的数字:")
print("real=",real)
print("\n")

#获取当前所有错误密码出现的数字
enumnums = list(set(num1+num2+num3+num4+num5))
print("输入的密码的所有数字集合:")
print("enumnums=",enumnums)
print("\n")

#对比每一位的可能数字 得到密码不可能的数字
'''
imp = []
for n in enumnums:
    bImp = True
    for r in real:
        for rr in r:
            if(n == rr):
                bImp = False
                break
        if(bImp == False):
           break
    if(bImp):
        imp.append(n)
'''
imp=[]
for n in real:
    for nn in n:
        if nn not in enumnums:
            imp.append(nn)

print("正确密码不可能出现的数字:")
print(imp)
print("\n")

#每个密码有两个正确数字 筛选出密码的4个数字（还无法确定顺序）每个输入密码于[3，5]求差集
final_arr=[]
for input_num in allnum:
    temp = list(set(input_num).difference(set(imp)))
    #得到两个数字的list说明这两个数字肯定是密码中的数字
    
    if(2 == len(temp)):
        final_arr = list(set(final_arr + temp))
print("密码的4位无顺序数字:")
print(final_arr)
print("\n")

#根据密码可能数字集合 在加上密码取值范围 整理出密码(确定顺序)
pass_word=[-1,-1,-1,-1]
get_real=0
while(1):
    if(4 == get_real):
        break
    index = 0
    for single_real in real:
        #如果交集只有一个元素 那说明这一个位置上肯定是这个数字
        check = list(set(single_real).intersection(set(final_arr)))
        if(1 == len(check)):
            get_real=get_real+1
            pass_word[index] = check[0]
            final_arr.remove(check[0])
            break
        index=index+1
print("正确密码:")
print(pass_word)