# _*_coding:utf-8_*_

from __future__ import print_function

import logging

from stanfordcorenlp import StanfordCoreNLP

local_corenlp_path = r'../stanford-corenlp-full-2018-02-27/'
# Other human languages support, e.g. Chinese
sentence = '清华大学位于北京。'

with StanfordCoreNLP(local_corenlp_path, lang='zh', quiet=False) as nlp:
    print(nlp.word_tokenize(sentence))

