# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:44:29 2017

@author: steven
"""

from __future__ import unicode_literals
import jieba
import sys
import codecs
import asr_wer
# import wer

# f1=sys.argv[1]
# f2=sys.argv[2]
def lcs(str_a, str_b):
    lensum = float(len(str_a) + len(str_b))
    # 得到一个二维的数组，类似用dp[lena+1][lenb+1],并且初始化为0
    lengths = [[0 for j in range(len(str_b) + 1)] for i in range(len(str_a) + 1)]

    # enumerate(a)函数： 得到下标i和a[i]
    for i, x in enumerate(str_a):
        for j, y in enumerate(str_b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    # 到这里已经得到最长的子序列的长度，下面从这个矩阵中就是得到最长子序列
    result = ""
    x, y = len(str_a), len(str_b)
    res_tuple=[]
    while x != 0 and y != 0:
        # 证明最后一个字符肯定没有用到
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:  # 用到的从后向前的当前一个字符
            assert str_a[x - 1] == str_b[y - 1]  # 后面语句为真，类似于if(a[x-1]==b[y-1]),执行后条件下的语句
            result = str_a[x - 1] + result  # 注意这一句，这是一个从后向前的过程
            print x,y
            res_tuple.append((x,y))
            print str_a[x-1],str_b[y-1]
            x -= 1
            y -= 1

            # 和上面的代码类似
            # if str_a[x-1] == str_b[y-1]:
            #    result = str_a[x-1] + result #注意这一句，这是一个从后向前的过程
            #    x -= 1
            #    y -= 1
    count=0
    length_max=len(str_a) if len(str_a)>len(str_b) else len(str_b)
    res_a=[-1 for i in range(length_max)]
    res_b=[-1 for i in range(length_max)]
    # res_tuple=res_tuple[::-1]
    res_a=res_b=''
    a_index=[i[0] for i in res_tuple]
    b_index=[i[1] for i in res_tuple]
    x=''
    y=''
    for i in range(len(a_index)-1):
        a=a_index[i]-a_index[i+1]
        b=b_index[i]-b_index[i+1]
        if a>b:
            str_b=str_b[:b_index[i+1]]+'&'*(a-b)+str_b[b_index[i+1]:]
        elif a<b:
            # print str_a[:a_index[i+1]]
            str_a=str_a[:a_index[i+1]]+ '&'*(b-a) +str_a[a_index[i+1]:]
            # print str_a[a_index[i+1]:]
            # print(str_a)


    if len(str_a)>len(str_b):
        str_b+='&'*(len(str_a)-len(str_b))
    for i in range(len(str_a)):
        print str_a[i],str_b[i]
    # print str_a
    # print str_b
    # for index,i in enumerate(a_index):
    #     x=a_index[index]
    #     y=b_index[index]
    #     print(a_index[index],b_index[index])
    #     # print(str_a)
    #     # print(res_a)
    #     # if a_index[index+1]==46:
    #     #     print(1)
    #     if a_index[index]<b_index[index]:
    #         if index==0:
    #             res_a+='&'*(b_index[index]-a_index[index])
    #             # str_a='&'*(b_index[index]-a_index[index])+str_a[0:a_index[index]]+str_a[a_index[index]:]
    #             res_a+=str_a[0:a_index[index]]
    #             res_b+=str_b[0:b_index[index]]
    #         else:
    #             res_a += '&' * (b_index[index] - a_index[index])
    #             # str_a='&'*(b_index[index]-a_index[index])+str_a[0:a_index[index]]+str_a[a_index[index]:]
    #
    #             res_a += str_a[a_index[index-1]:a_index[index]]
    #             res_b += str_b[b_index[index-1]:b_index[index]]
    #         update_list(a_index,index+1,b_index[index]-a_index[index])
    #     elif a_index[index]>b_index[index]:
    #         if index==0:
    #             res_b+='&'*(a_index[index]-b_index[index])
    #             # str_b=
    #             # str_b='&'*(a_index[index]-b_index[index])+str_b[0:b_index[index]]+str_b[b_index[index]:]
    #
    #             res_b+=str_b[0:b_index[index]]
    #
    #             res_a+=str_a[0:a_index[index]]
    #         else:
    #             res_b += '&' * (a_index[index] - b_index[index])
    #             # str_b='&'*(a_index[index]-b_index[index])+str_b[0:b_index[index]]+str_b[b_index[index]:]
    #
    #             res_b += str_b[b_index[index-1]:b_index[index]]
    #             res_a += str_a[a_index[index-1]:a_index[index]]
    #         update_list(b_index,index+1,a_index[index]-b_index[index])
    #     else:
    #         if index==0:
    #             res_b += str_b[0:b_index[index]]
    #             res_a += str_a[0:a_index[index]]
    #         else:
    #             res_b += str_b[b_index[index - 1]:b_index[index]]
    #             res_a += str_a[a_index[index-1]:a_index[index]]
    # print str_a
    print res_a
    # print str_b
    print res_b
def update_list(arr,i,t):
    for index,_ in enumerate(arr):
        if index<i:
            continue
        arr[index]+=t
    # longestdist = lengths[len(str_a)][len(str_b)]
    # ratio = longestdist / min(len(str_a), len(str_b))
    # return {'longestdistance':longestdist, 'ratio':ratio, 'result':result}
    # return ratio
f1= '/home/tyf/api/api_test/testdata/测试文书/传唤证/常玮平传唤通知.jpg_2018-08-15_15-37-23.txt'
f2= '/home/tyf/api/api_test/testdata/测试文书/传唤证/恥松.txt'
# f1='E:\项目\\18.7.16东大项目\测试文书\'
# f1='E:\项目\\18.7.16东大项目\测试文书\拘留证\陈鸿志-黑社会.txt'
# f2='E:\项目\\18.7.16东大项目\测试文书\拘留证\据留.txt'
fref=codecs.open(f1,'r',encoding='utf-8').readlines()
fpred=codecs.open(f2,'r',encoding='utf-8').readlines()
fref=[s.strip() for s in fref]
fpred=[s.strip() for s in fpred]

fref = ''.join(fref)
fpred = ''.join(fpred)
# print(fref)
# print(fref[0])
ret = asr_wer.wer(fref,fpred, debug=True)
# print lcs(fref,fpred)
# fref= u' '.join([char for char in fref])
# fpred= u' '.join([char for char in fpred])
#
# ret = asr_wer.wer(fref,fpred, debug=True)

#fref=[u' '.join(list(s.strip().replace(u' ',u''))) for s in fref ]
#fpred=[u' '.join(list(s.strip().replace(u' ',u''))) for s in fpred ]
# err_numSub, err_numDel , err_numIns,total_char=0,0,0,0
#
# sentcount=0
#
# for r,p in zip(fref,fpred):
#     numSub, numDel , numIns,tchars=wer.wer(r,p)
#     err_numSub+=numSub
#     err_numDel+=numDel
#     err_numIns+=numIns
#     total_char+=tchars
#     if r==p:
#         sentcount+=1
    
# print err_numSub, err_numDel , err_numIns,total_char
# print 1-(err_numSub+err_numDel +err_numIns)*1.0/total_char
# print 'sentance correct=',sentcount*1.0/len(fref)
