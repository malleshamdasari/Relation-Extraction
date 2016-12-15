import pickle as pkl
import numpy as np

def init_weights(new, old, embeds, weights):
    global embeddings_size
    for word1 in new:
        for word2 in old:
            if word1.strip() == word2.strip():
                weights[new[word1]] = embeds[new[word1]]
            else:
                temp_row = np.random.uniform(-1, 1, embeddings_size)
                weights[new[word1]] = temp_row
    for i in range(len(new)+1, len(weights)):
        temp_row = np.random.uniform(-1, 1, embeddings_size)
        weights[i] = temp_row

word_dict = pkl.load(open("word_dict.pkl", "rb"))
rel_dict = pkl.load(open("rel_dict.pkl", "rb"))
embed_dict = pkl.load(open("embed_dict.pkl", "rb"))
embeddings = pkl.load(open("embeds.pkl", "rb"))
words_size, embeddings_size = embeddings.shape
weights = np.zeros((len(word_dict)+len(rel_dict), embeddings_size))
init_weights(word_dict, embed_dict, embeddings, weights)
pkl.dump(weights, open("weights.pkl","wb"))
