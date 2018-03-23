# -*- coding: utf-8 -*-
# @Time    : 11/16/17 10:20 AM
# @Author  : tyf_aicyber
# @Site    : 
# @File    : num2zh.py
# @Software: PyCharm

# from __future__ import print_function

number_to_Chinese = {"0": "零",
                     "1": "一",
                     "2": "二",
                     "3": "三",
                     "4": "四",
                     "5": "五",
                     "6": "六",
                     "7": "七",
                     "8": "八",
                     "9": "九", }

digit_in_Chinese = {"1": "十",
                    "2": "百",
                    "3": "千",
                    "4": "万",
                    "8": "亿",
                    "12": "兆"}  #此处：1兆 == 1万亿


################################################

def write_number_in_Chinese(number_input):  # translate number into Chinese
    if number_input == '0':
        return number_to_Chinese[number_input]
    number_len = len(number_input)
    outcome_str = ""
    four_digit_switch = False

    for i in range(number_len):
        digit = number_len - i - 1
        if number_input[i] == "0":
            if digit % 4 == 0 and digit != 0 and four_digit_switch == False:
                outcome_str += digit_in_Chinese[str(digit)]
                four_digit_switch = True
            continue
        else:
            four_digit_switch = False

        if i > 0 and number_input[i - 1] == "0" and (digit + 1) % 4 != 0:
            outcome_str += number_to_Chinese["0"]

        if digit % 4 != 1 or number_input[i] != "1" or i != 0:
            outcome_str += number_to_Chinese[number_input[i]]

        if digit % 4 != 0:
            outcome_str += digit_in_Chinese[str(digit % 4)]
        elif digit % 4 == 0 and digit != 0 and four_digit_switch == False:
            outcome_str += digit_in_Chinese[str(digit)]
            four_digit_switch = True

    return outcome_str


################################################

def is_tnum_valid(num_str):
    '''
    整数部分
    :param num_str: 
    :return: 
    '''
    if len(num_str) == 0:
        return False
    if num_str == '0':
        return num_str
    num_of_comma = 0
    outcome_num = ""
    no_number = True
    for char in num_str:
        if char.isdigit() == False and char != ',':
            return False
        if char == ',':
            num_of_comma += 1
        if char.isdigit() == True and char != '0':
            no_number = False
        if no_number == False and char.isdigit():
            outcome_num += char
    if no_number:
        return False

    if num_of_comma != 0:
        if (len(num_str) - num_of_comma) % 3 == 0 and (len(num_str) - num_of_comma) // 3 != num_of_comma + 1:
            return False
        elif (len(num_str) - num_of_comma) % 3 != 0 and (len(num_str) - num_of_comma) // 3 != num_of_comma:
            return False
        for i in range(len(num_str) - 4, 0, -4):
            if num_str[i] != ',':
                return False

    if len(outcome_num) > 16:
        raise ValueError("Out of Range")

    return outcome_num


def is_xnum_valid(num_str):
    for char in num_str:
        if char.isdigit() == False:
            return False
    return num_str

def xnun2zh(xnum):
    outnum = ''
    for char in xnum:
        outnum += number_to_Chinese[char]
    return outnum


#####################main###########################

# x = input("Please enter a number:")
# x = str(123)

def num2zh(x):
    if x[0] == '$':
        x = x[1:]
    assert len(x) > 0
    sp = x.split('.')
    if len(sp)>2:
        raise TypeError("Not string of number")
    elif len(sp) == 2:
        tnum = is_tnum_valid(sp[0])
        xnum = is_xnum_valid(sp[1])
        if xnum:
            outnum_str = write_number_in_Chinese(tnum) + '点' + xnun2zh(xnum)
        else:
            raise("Format error")
    else:
        tnum = is_tnum_valid(sp[0])
        if tnum == False:
            raise TypeError("Format error")
        outnum_str = write_number_in_Chinese(tnum)
    return outnum_str

if __name__ == '__main__':
    print num2zh('$10.12356888')
    print num2zh('2,000,000,000,000,200.12')
    print num2zh('2,001.1')

# outcome_number = if_number_valid(x)
# if outcome_number == False:
#     print("Format error")
# elif outcome_number == "Out of Range":
#     print("Out of Range")
# else:
#     print(write_number_in_Chinese(outcome_number))