# coding:utf-8


import random
import string


def caculate_num(a, symbol, b):
    '''
    计算加减乘除
    '''
    if symbol == '+':
        return a+b
    elif symbol == '-':
        return a-b
    elif symbol == '*':
        return a*b
    elif symbol == '/':
        if b == 0:
            return '除数不能为0'
        else:
            return a/b
    else:
        return '请输入正确的符号'


def convert_string(strings, type):
    '''
    大小写转换
    '''
    if type == 'upper':
        return strings.upper()
    elif type == 'lower':
        return strings.lower()
    else:
        return 'type只允许为upper或lower'


def random_string(num):
    '''
    随机生成字符串
    '''
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(num))
    return a


if __name__ == '__main__':
    print(random_string(10))
    print(convert_string('abcd', 'upper'))
    print(caculate_num(14, '*', 12))

