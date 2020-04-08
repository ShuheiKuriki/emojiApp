import io
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
    scores = (tgt_emb / np.linalg.norm(tgt_emb, 2, 1)[:, None]).dot(word_emb / np.linalg.norm(word_emb))
    print('2')
    k_best = scores.argsort()[-K:][::-1]
    print('3')
    answer = []
    for i, idx in enumerate(k_best):
        answer.append('%.4f - %s' % (scores[idx], tgt_id2word[idx]))
    return answer

def translate(src_path, tgt_path, nmax, src_word):
    print("a")
    src_embeddings, src_id2word, src_word2id = load_vec(src_path, nmax)
    print("b")
    tgt_embeddings, tgt_id2word, tgt_word2id = load_vec(tgt_path, nmax)
    print("c")
    return get_nn(src_word, src_embeddings, src_id2word, tgt_embeddings, tgt_id2word, K=5)
# printing nearest neighbors in the target space
