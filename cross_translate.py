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
  try:
    tgt_embeddings = np.load(folder+tgt_lang+'.npy')
    with open(folder+"tgt_id2word", 'rb') as f:
      tgt_id2word = pickle.load(f)
  except:
    tgt_embeddings = src_embeddings
    tgt_id2word = src_id2word
  # tgt_embeddings, tgt_id2word, tgt_word2id = load_vec(tgt_path, nmax)
  print("c")
  if src_lang != tgt_lang:
    return get_nn(src_word, src_embeddings, src_id2word, tgt_embeddings, tgt_id2word, K=10)
  else:
    return get_nn(src_word, src_embeddings, src_id2word, tgt_embeddings, tgt_id2word, K=11)[1:]
# printing nearest neighbors in the target space

# def make_folder(folder):
#   if not os.path.isdir(folder):
#     os.mkdir(folder)

# def save(lang, tgt, emb_path, output_path, nmax=250000):
#   emb, id2word, word2id = load_vec(emb_path, nmax)
#   np.save(output_path+lang, emb/np.linalg.norm(emb, 2, 1)[:, None])
#   if not tgt:
#     with open(output_path+"src_id2word",'wb') as f:
#       pickle.dump(id2word, f)
#     with open(output_path+"src_word2id",'wb') as f:
#       pickle.dump(word2id, f)
#   else:
#     with open(output_path+"tgt_id2word",'wb') as f:
#       pickle.dump(id2word, f)
#     with open(output_path+"tgt_word2id",'wb') as f:
#       pickle.dump(word2id, f)

# if __name__=='__main__':
#   src = 'ja'
#   tgt = 'en'
#   nmax = 5000
#   make_folder('pickle_emb{}'.format(nmax))

#   folder = 'pickle_emb/{}-{}-unsup/'.format(src, tgt)
#   folder2 = 'pickle_emb{}/{}-{}-unsup/'.format(nmax, src, tgt)
#   make_folder(folder)
#   make_folder(folder2)

#   emb_path = 'vectors/wiki.{}.vec'.format(src)
#   save(src, False, emb_path, folder)
#   save(src, False, emb_path, folder2, nmax)

#   emb_path = 'vectors/wiki.{}.vec'.format(tgt)
#   save(tgt, True, emb_path, folder)
#   save(tgt, True, emb_path, folder2, nmax)
  # src_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src, tgt, src)
  # tgt_sup_path = 'vectors/{}-{}-super/vectors-{}.txt'.format(src, tgt, tgt)
  # src_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src, tgt, src)
  # tgt_unsup_path = 'vectors/{}-{}-unsup/vectors-{}.txt'.format(src, tgt, tgt)
      


