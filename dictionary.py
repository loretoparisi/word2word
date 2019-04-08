#!/usr/bin/env python
# - *- coding: utf- 8 - *-

from word2word import Word2word

dict_path='/root/word2word'

with open('word2word/supporting_languages.txt') as f:
    lines = f.readlines()
    for dict_pair in lines:
        codes=dict_pair.strip('\n').split('-')
        print("getting dictionary %s-%s" % (codes[0], codes[1]) )
        w2w = Word2word(codes[0], codes[1], dict_path=dict_path)
