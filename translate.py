# -*- coding: utf-8 -*-
# import matplotlib
# import matplotlib.pyplot as plt
import tensorflow as tf
import pickle as pk
import numpy as np
# import sklearn.manifold as man
from tensorflow.python.framework import ops

from model_ import Emoji2Vec, ModelParams
from phrase2vec import Phrase2Vec
# from utils import build_kb, get_examples_from_kb, generate_embeddings, get_metrics

"""# Initializations
This step takes a while to execute, wait for 'DONE'

## Constants and Hyperparameters
"""

# word2vec_path = 'data/word2vec/GoogleNews-vectors-negative300.bin'
mapping_path = 'emoji_mapping.p'
# data_folder = './data/training/'
# embeddings_file = 'generated_embeddings.p'

in_dim = 300   # Length of word2vec vectors
out_dim = 300  # Desired dimension of output vectors
pos_ex = 4
neg_ratio = 1
max_epochs = 40
dropout = 0.1

params = ModelParams(in_dim=in_dim, out_dim=out_dim, pos_ex=pos_ex, max_epochs=max_epochs,
                    neg_ratio=neg_ratio, learning_rate=0.001, dropout=dropout, class_threshold=0.5)


ckpt_path = params.model_folder('unicode') + '/model.ckpt'
# e2v_path = 'pre-trained/emoji2vec.bin'
# print(ckpt_path, e2v_path)

"""## Initialize models and mappings"""

# print('Initializing: reading embedding data from: ' + word2vec_path)
# get the vector for a phrase
# phraseVecModel = Phrase2Vec.from_word2vec_paths(params.in_dim, word2vec_path, e2v_path)
# pk.dump(phraseVecModel, open('phrase_vec_model.bin','wb'))
# RESET THE GRAPH
ops.reset_default_graph()
# mapping from id to emoji
mapping = pk.load(open(mapping_path, 'rb'))
phraseVecModel = pk.load(open('phrase_vec_model.bin', 'rb'))
model = Emoji2Vec(params, len(mapping), embeddings_array=None, use_embeddings=False)
session = tf.Session()
saver = tf.train.Saver()
saver.restore(session, ckpt_path)

"""# Top Emoji Query
Set `phr` as a phrase, and get the top `N` emojis correlating to that phrase.
"""

def phr_to_emoji(phr, N):
# get the vector representaiton
    vec = phraseVecModel[phr]
    emojis = []
# query the tensorflow model
    res = list()
    for colIx in range(0, len(mapping)):
        predict = session.run(model.prob, feed_dict={
            model.col: np.array([colIx]),
            model.orig_vec: np.array([vec])
            })
        res.append(predict)
# print the top N emoji
    for ind in sorted(range(len(res)), key=lambda i: res[i], reverse=True)[:N]:
        emojis.append(str(mapping[ind]) + ' ' + str(res[ind]) +'\n')
    return emojis

def phr_to_emojis(phr):
    # get the vector representaitons
    vecs = phraseVecModel.get_vecs(phr)
    emojis = []
    # query the tensorflow model
    for vec in vecs:
        res = list()
        for colIx in range(0, len(mapping)):
                predict = session.run(model.prob, feed_dict={
                        model.col: np.array([colIx]),
                        model.orig_vec: np.array([vec])
                })
                res.append(predict)
        ind = sorted(range(len(res)), key=lambda i: res[i], reverse=True)[0]
        if res[ind]>0.8:
                emojis.append(str(mapping[ind]) + ' ' + str(res[ind]) +'\n')
        else:
                emojis.append("unknown\n")
    return emojis

"""# Top Phrase Query
Set `em` as an emoji, and get the top `N` phrases correlating to that emoji.
"""

# input
def emoji_to_word(em, N):
# get the relevant vectors from tensorflow
    emoji_vecs = session.run(model.V)
    vec = emoji_vecs[inv_map[em]]

    # print top N phrases
    for word, score in phraseVecModel.from_emoji([vec], top_n=N):
        print(str.format("{}\t{}", word, score))

"""# Analogy Task
Set `base` as a base emoji, `minus` as an emoji to subtract from the base, `plus` as an emoji to add, and get the top `N` correlating phrases and emojis relating to this analogy.
"""

def print_analogy_result(base, minus, plus):
    emoji_vecs = session.run(model.V)
    total = phraseVecModel[base] - phraseVecModel[minus] + phraseVecModel[plus]

    res = list()
    for colIx in range(0, len(mapping)):
        predict = session.run(model.prob, feed_dict={
            model.col: np.array([colIx]),
            model.orig_vec: np.array([total / np.linalg.norm(total)])
        })
        res.append(predict)

    ems = sorted(range(len(res)), key=lambda i: res[i], reverse=True)[:5]
    print(str.format('{} - {} + {} = {}', base, minus, plus, [mapping[em] for em in ems]))

# print_analogy_result('👑', '🚹', '🚺')
# print_analogy_result('💵', '🇺🇸', '🇬🇧')
# print_analogy_result('💵', '🇺🇸', '🇪🇺')
# print_analogy_result('👦', '👨', '👩')
# print_analogy_result('👪', '👦', '👧')
# print_analogy_result('🕶', '☀️', '⛈')

# input
# base = '👑'
# # base = '👨'
# minus = '🚹'
# plus = '🚺'
# N = 10
#
# # get the relevant vectors from tensorflow
# emoji_vecs = session.run(model.V)
# total = emoji_vecs[inv_map[base]] - emoji_vecs[inv_map[minus]] + emoji_vecs[inv_map[plus]]
#
# # print the top N phrases
# print(str.format('Top {} mーーatching phrases:', N))
# print()
# for word, score in phraseVecModel.from_emoji([total], top_n=N):
#     print(str.format("{}\t{}", word, score))
#
# # query the tensorflow model
# res = list()
# for colIx in range(0, len(mapping)):
#     predict = session.run(model.prob, feed_dict={
#         model.col: np.array([colIx]),
#         model.orig_vec: np.array([total / np.linalg.norm(total)])
#     })
#     res.append(predict)
#
# # print the top N emoji
# print()
# print(str.format('Top {} matching emoji:', N))
# print()
# for ind in sorted(range(len(res)), key=lambda i: res[i], reverse=True)[:N]:
#     print(mapping[ind], res[ind])
