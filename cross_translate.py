import io
import pickle
import os
import numpy as np

def load_vec(emb_path, nmax=250000):
  vectors = []
  word2id = {}
  with io.open(emb_path, 'r', encoding='utf-8', newline='\n', errors='ignore') as f:
    next(f)
    for i, line in enumerate(f):
      word, vect = line.rstrip().split(' ', 1)
      vect = np.fromstring(vect, sep=' ')
      assert word not in word2id, 'word found twice'
      vectors.append(vect)
      word2id[word] = len(word2id)
      if len(word2id) == nmax:
        break
  id2word = {v: k for k, v in word2id.items()}
  embeddings = np.vstack(vectors)
  return embeddings, id2word, word2id

def get_nn(word, src_emb, src_id2word, tgt_emb, tgt_id2word, K=5):
  print("Nearest neighbors of \"%s\":" % word)
  word2id = {v: k for k, v in src_id2word.items()}
  word_emb = src_emb[word2id[word]]
  print('1')
  scores = tgt_emb.dot(word_emb)
  print('2')
  k_best = scores.argsort()[-K:][::-1]
  print('3')
  answer = []
  for i, idx in enumerate(k_best):
    answer.append('%.4f - %s' % (scores[idx], tgt_id2word[idx]))
  return answer

def translate(src_lang, tgt_lang, src_word):
  folder = 'pickle_emb/{}-{}-unsup/'.format(src_lang, tgt_lang)
  if not os.path.exists(folder):
    folder = 'pickle_emb5000/{}-{}-unsup/'.format(src_lang, tgt_lang)
  print("a")
  src_embeddings = np.load(folder+src_lang+'.npy')
  with open(folder+"src_id2word", 'rb') as f:
    src_id2word = pickle.load(f)
  # src_embeddings, src_id2word, src_word2id = load_vec(src_path, nmax)
  print("b")
  tgt_embeddings = np.load(folder+tgt_lang+'.npy')
  with open(folder+"tgt_id2word", 'rb') as f:
    tgt_id2word = pickle.load(f)
  # tgt_embeddings, tgt_id2word, tgt_word2id = load_vec(tgt_path, nmax)
  print("c")
  return get_nn(src_word, src_embeddings, src_id2word, tgt_embeddings, tgt_id2word, K=10)
# printing nearest neighbors in the target space

# def save(src, tgt, nmax):
#   # src_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src, tgt, src)
#   # tgt_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src, tgt, tgt)
#   src_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src, tgt, src)
#   tgt_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src, tgt, tgt)
#   # src_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src, tgt, src)
#   # tgt_joint_path = 'vectors/{}-{}-joint/{}_joint_embedding.90'.format(src, tgt, tgt)
#   if not os.path.isdir('pickle_emb{}'.format(nmax)):
#     os.mkdir('pickle_emb{}'.format(nmax))
#   folder = 'pickle_emb{}/{}-{}-unsup/'.format(nmax, src, tgt)
#   if not os.path.isdir(folder):
#     os.mkdir(folder)

#   emb, id2word, word2id = load_vec(src_unsup_path, nmax)
#   np.save(folder+src, emb/np.linalg.norm(emb, 2, 1)[:, None])
#   with open(folder+"src_id2word",'wb') as f:
#     pickle.dump(id2word, f)
#   with open(folder+"src_word2id",'wb') as f:
#     pickle.dump(word2id, f)

#   emb, id2word, word2id = load_vec(tgt_unsup_path, nmax)
#   np.save(folder+tgt, emb/np.linalg.norm(emb, 2, 1)[:, None])
#   with open(folder+"tgt_id2word",'wb') as f:
#     pickle.dump(id2word, f)
#   with open(folder+"tgt_word2id",'wb') as f:
#     pickle.dump(word2id, f)

# if __name__=='__main__':
#   for src in ['en','es','fr','it']:
#     for tgt in ['en','es','fr','it']:
#       if src==tgt:
#         continue
#       save(src, tgt, 5000)


