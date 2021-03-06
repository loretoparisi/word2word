#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

from .utils import download_or_load

class Word2word:
    def __init__(self, lang1, lang2, dict_path=''):
        res = download_or_load(lang1, lang2, dict_path)
        if res is not None:
            self.word2x, self.y2word, self.x2ys = res

    def __call__(self, query, n_best=5):
        if self.word2x is None:
            return []
        query = query.decode('utf8')
        if query not in self.word2x:
            return []
        x = self.word2x[query]
        ys = self.x2ys[x]
        words = [self.y2word[y] for y in ys]
        return words[:n_best]
