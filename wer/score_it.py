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

f1= '/home/tyf/api/api_test/testdata/测试文书/传唤证/常玮平传唤通知.jpg_2018-08-15_15-37-23.txt'
f2= '/home/tyf/api/api_test/testdata/测试文书/传唤证/恥松.txt'

fref=codecs.open(f1,'r',encoding='utf-8').readlines()
fpred=codecs.open(f2,'r',encoding='utf-8').readlines()
fref=[s.strip() for s in fref]
fpred=[s.strip() for s in fpred]

fref = ''.join(fref)
fpred = ''.join(fpred)

fref= u' '.join([char for char in fref])
fpred= u' '.join([char for char in fpred])

ret = asr_wer.wer(fref,fpred, debug=True)

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
