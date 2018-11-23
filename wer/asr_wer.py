# -*- coding: utf-8 -*-
import re

def wer(ref, hyp, debug=False):
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
    return numSub, numDel , numIns,len(r)
    return (numSub + numDel + numIns) / (float)(len(r))
    # wer_result = round((numSub + numDel + numIns) / (float)(len(r)), 3)


    # return {'WER': wer_result, 'Cor': numCor, 'Sub': numSub, 'Ins': numIns, 'Del': numDel}


if __name__=='__main__':

    # l = []
    # f1 = open('../test/title_word', 'r')
    # lines1 = f1.readlines()
    # for line1 in lines1:
    #     line1 = line1.strip()
    #     words1 = re.split('	', line1)
    #     title1 = words1[0]
    #     # str1 = unicode(words1[1])
    #     str1 = words1[1].decode('utf8')
    #
    #     f2 = open('../test/yzs_cafe', 'r')
    #     lines2 = f2.readlines()
    #     for line2 in lines2:
    #         line2 = line2.strip()
    #         # words2 = re.split('_', line2)
    #         words2 = re.split('_', line2)
    #         title2 = words2[0] + '_' + words2[1]
    #         # title2 = words2[0]
    #         # str2 = unicode(words2[2])
    #         str2 = words2[2].decode('utf8')
    #         # str2 = words2[1].decode('utf8')
    #
    #         if cmp(title1,title2) == 0:
    #             # print str1 + '\n' +str2 + '\n'

    str1 = u'今天天气真好阿'
    str2 = u'今天气的好哈啊'

    s1= u' '.join([char for char in str1])
    s2= u' '.join([char for char in str2])
    ret = wer(s1,s2, debug=True)

    # l.append(ret)

    # s= reduce(lambda x,y:x+y,l)
    #
    # print (1-s/len(l))




