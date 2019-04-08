#!/usr/bin/env python
# - *- coding: utf- 8 - *-

from word2word import Word2word

en2fr = Word2word("en", "fr")
# out: ['pomme', 'pommes', 'pommier', 'tartes', 'fleurs']
print '%s' % ','.join(map(str, en2fr("apple")))

# out: ['travaillé', 'travaillait']
print '%s' % ','.join(map(str, en2fr("worked", n_best=2)))

en2zh = Word2word("en", "zh_cn")
# out: ['老师', '教师', '学生', '导师', '墨盒']
print '%s' % ','.join(map(str, en2zh("teacher")))