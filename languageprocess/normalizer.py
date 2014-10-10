#!/usr/bin/env python3

import tokenizer
import re


'''
Normalize the given text
'''

def normalize(text):
    data = tokenizer.tokenize(text)
    for i,value in enumerate(data):
        if not re.match(r'^[A-Z]*$', value):
            data[i] = value.lower()

    return data


if __name__ == '__main__':
    s = normalize('Hello ThEre AKA Hahahah :,snF;JJk')
    print(s)

