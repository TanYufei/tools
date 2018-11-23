# -*- coding: utf-8 -*-
# @Time    : 18-9-5
# @Author  : baifendian_tyf
# @File    : alignement.py
# @Software: PyCharm

from __future__ import unicode_literals, print_function
import codecs

def alignment_fun1(ref, hyp, debug=True):
    r = ref.split()
    h = hyp.split()
    # costs will holds the costs, like in the Levenshtein distance algorithm
    costs = [[0 for inner in range(len(h) + 1)] for outer in range(len(r) + 1)]
    # backtrace will hold the operations we've done.
    # so we could later backtrace, like the WER algorithm requires us to.
    backtrace = [[0 for inner in range(len(h) + 1)] for outer in range(len(r) + 1)]

    OP_OK = 0
    OP_SUB = 1
    OP_INS = 2
    OP_DEL = 3

    # First column represents the case where we achieve zero
    # hypothesis words by deleting all reference words.
    for i in range(1, len(r) + 1):
        costs[i][0] = 1 * i
        backtrace[i][0] = OP_DEL

    # First row represents the case where we achieve the hypothesis
    # by inserting all hypothesis words into a zero-length reference.
    for j in range(1, len(h) + 1):
        costs[0][j] = 1 * j
        backtrace[0][j] = OP_INS

    # computation
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                costs[i][j] = costs[i - 1][j - 1]
                backtrace[i][j] = OP_OK
            else:
                substitutionCost = costs[i - 1][j - 1] + 1  # penalty is always 1
                insertionCost = costs[i][j - 1] + 1  # penalty is always 1
                deletionCost = costs[i - 1][j] + 1  # penalty is always 1

                costs[i][j] = min(substitutionCost, insertionCost, deletionCost)
                if costs[i][j] == substitutionCost:
                    backtrace[i][j] = OP_SUB
                elif costs[i][j] == insertionCost:
                    backtrace[i][j] = OP_INS
                else:
                    backtrace[i][j] = OP_DEL

    # back trace though the best route:
    i = len(r)
    j = len(h)
    numSub = 0
    numDel = 0
    numIns = 0
    numCor = 0
    if debug:
        print("OP\tREF\tHYP")
        lines = []
    while i > 0 or j > 0:
        if backtrace[i][j] == OP_OK:
            numCor += 1
            i -= 1
            j -= 1
            if debug:
                lines.append("OK\t" + r[i] + "\t" + h[j])
        elif backtrace[i][j] == OP_SUB:
            numSub += 1
            i -= 1
            j -= 1
            if debug:
                lines.append("SUB\t" + r[i] + "\t" + h[j])
        elif backtrace[i][j] == OP_INS:
            numIns += 1
            j -= 1
            if debug:
                lines.append("INS\t" + "****" + "\t" + h[j])
        elif backtrace[i][j] == OP_DEL:
            numDel += 1
            i -= 1
            if debug:
                lines.append("DEL\t" + r[i] + "\t" + "****")
    if debug:
        lines = reversed(lines)
        for line in lines:
            print(line)
        print("#cor " + str(numCor))
        print("#sub " + str(numSub))
        print("#del " + str(numDel))
        print("#ins " + str(numIns))
    # print ref
    # print hyp
    # print numSub, numDel , numIns,len(r),(numSub + numDel + numIns) / (float)(len(r))
    # return numSub, numDel, numIns, len(r), lines
    return numCor, lines

def alignment_fun2(str_a, str_b):
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
    res_tuple = []
    while x != 0 and y != 0:
        # 证明最后一个字符肯定没有用到
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:  # 用到的从后向前的当前一个字符
            assert str_a[x - 1] == str_b[y - 1]  # 后面语句为真，类似于if(a[x-1]==b[y-1]),执行后条件下的语句
            result = str_a[x - 1] + result  # 注意这一句，这是一个从后向前的过程
            # print x,y
            res_tuple.append((x, y))
            # print str_a[x-1],str_b[y-1]
            x -= 1
            y -= 1

            # 和上面的代码类似
            # if str_a[x-1] == str_b[y-1]:
            #    result = str_a[x-1] + result #注意这一句，这是一个从后向前的过程
            #    x -= 1
            #    y -= 1
    count = 0
    length_max = len(str_a) if len(str_a) > len(str_b) else len(str_b)
    res_a = [-1 for i in range(length_max)]
    res_b = [-1 for i in range(length_max)]
    # res_tuple=res_tuple[::-1]
    res_a = res_b = ''
    a_index = [i[0] for i in res_tuple]
    b_index = [i[1] for i in res_tuple]
    x = ''
    y = ''

    index_map = range(len(str_a))

    for i in range(len(a_index) - 1):
        a = a_index[i] - a_index[i + 1]
        b = b_index[i] - b_index[i + 1]
        if a > b:
            str_b = str_b[:b_index[i + 1]] + '&' * (a - b) + str_b[b_index[i + 1]:]
        elif a < b:
            # print str_a[:a_index[i+1]]
            str_a = str_a[:a_index[i + 1]] + '&' * (b - a) + str_a[a_index[i + 1]:]
            # print str_a[a_index[i+1]:]
            # print(str_a)

    if len(str_a) > len(str_b):
        str_b += '&' * (len(str_a) - len(str_b))

    for i in range(len(str_a)):
        if str_a[i] == str_b[i]:
            count += 1
        print(str_a[i], str_b[i])

    return count, str_a, str_b
    # print(res_a)
    # # print str_b
    # print(res_b)

def extract_info(ref, pre):

    numCor, str_a, str_b = alignment_fun2(ref, pre)
    print('numCor1: %d' % numCor)


if __name__ == '__main__':

    f1 = '/home/tyf/api/api_test/testdata/测试文书/传唤证/常玮平传唤通知.jpg_2018-08-15_15-37-23.txt'
    f2 = '/home/tyf/api/api_test/testdata/测试文书/传唤证/工红芬.txt'

    fref = codecs.open(f1, 'r', encoding='utf-8').readlines()
    fpred = codecs.open(f2, 'r', encoding='utf-8').readlines()
    fref = [s.strip() for s in fref]
    fpred = [s.strip() for s in fpred]

    str1 = ''.join(fref)
    str2 = ''.join(fpred)
    # str1 = u'天气真好阿'
    # str2 = u'今天天气真好阿'
    # numCor, str_a, str_b = alignment_fun2(str1, str2)
    # print('numCor1: %d' % numCor)

    extract_info(str1, str2)

    # s1 = u' '.join([char for char in str1])
    # s2 = u' '.join([char for char in str2])
    # numCor, lines = alignment_fun1(s1, s2)
    # print('numCor2: %d' % numCor)


