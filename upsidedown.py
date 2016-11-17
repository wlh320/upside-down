#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""make a sentence upside-down"""

ORIGIN = 'zyxwvutsrqponmlkjihgfedcbaVRFBCDEFJMW.?!,\'><(){}^;_'
NEW = 'zʎxʍʌnʇsɹbdouɯןʞɾıɥbɟǝpɔqɐɅᴚℲᗺƆᗡƎᖵſWM˙¿¡\',<>)(}{ᵥ؛‾'
SAME = ' HIOXS(|:#=+-*~/\\'

def transform(src):
    """upside-down a sentence"""

    src = src[-1::-1] # reverse
    res = ''
    for i in src:
        if i in SAME:
            res += i
        elif i in ORIGIN:
            res += NEW[ORIGIN.index(i)]
        else:  # cannot transform
            res += '#'
    return res


if __name__ == '__main__':
    s = input('input a string:')
    result = transform(s)
    print('upside-down:', result)
