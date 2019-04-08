#!/usr/bin/env python
# - *- coding: utf- 8 - *-

from word2word import Word2word

dict_path='/root/word2word'
en2fr = Word2word("en", "fr", dict_path=dict_path)
# out: ['pomme', 'pommes', 'pommier', 'tartes', 'fleurs']
print '%s' % ','.join(map(str, en2fr("apple")))

fr2en = Word2word("fr", "en", dict_path=dict_path)
print '%s' % ','.join(map(str, fr2en("pomme", n_best=2)))

# out: ['travaillé', 'travaillait']
print '%s' % ','.join(map(str, en2fr("worked", n_best=2)))

en2zh = Word2word("en", "zh_cn", dict_path=dict_path)
# out: ['老师', '教师', '学生', '导师', '墨盒']
print '%s' % ','.join(map(str, en2zh("teacher")))

zh2en = Word2word("zh_cn", "en", dict_path=dict_path)
print '%s' % ','.join(map(str, zh2en("老师")))

hi2en = Word2word("hi", "en", dict_path=dict_path)
print '%s' % ','.join(map(str, hi2en("मिलने")))