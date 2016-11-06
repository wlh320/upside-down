# -*- coding:utf-8 -*-
# author: W0h
# Not for use. just for fun!
ori = 'zyxwvutsrqponmlkjihgfedcbaVRFBCDEFJMW.?!,\'><(){}^;_'
ud = 'zʎxʍʌnʇsɹbdouɯןʞɾıɥbɟǝpɔqɐɅᴚℲᗺƆᗡƎᖵſWM˙¿¡\',<>)(}{ᵥ؛‾'
same = ' HIOXS(|:#=+-*~/\\'
s = input('input a string:')
s = s[-1::-1]
res = ''
for i in s:
    if i in same:
        res += i
    elif i in ori:
        res += ud[ori.index(i)]
    else:  # cannot transform
        res += '#'
print(res)
