#!/usr/bin/env python3

import re

'''
Tokenizes the string input coming from web app. Any irrelevent special character
is removed.
'''

def tokenize(text):
    data = text
    data = data.split(' ')
    
    for index,word in enumerate(data):
        if ("'" not in word and '.' not in word) and re.match('[a-z]+(?i)(\W|[0-9])+[a-z]+(?i)', word):
            # removing all the special characters and numbers from the given input
            data[index] = word.replace(word, re.sub('\W+', '', word))
            data[index] = word.replace(word, re.sub('[0-9]+', '', data[index]))

    data = ' '.join(data)
    data = data.replace('\n','`').replace('\t','`').replace('-','`').replace(':','`').replace(';','`').replace('. ', '`').replace('.', '`').replace(' ', '`').replace(',','`').split('`')
    data = list(filter(None, data))
    return data

if __name__ == '__main__':
    data = "insert int:o amit (name) values ('aaa')"
    print(data)
    textlist = tokenize(data)
    textlist = [txt for txt in textlist]
    print(textlist)
