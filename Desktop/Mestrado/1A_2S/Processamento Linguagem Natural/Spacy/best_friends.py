#! /usr/bin/env python3

import spacy
import re
from collections import Counter
import sys

import itertools

def generate_pairs(lista):
    pairs = []
    t = len(lista)
    i = 0
    while i < t-1:
        k = t-1
        while k != i:
            pairs.append((lista[i], lista[k]))
            k -= 1
        i += 1
    return pairs

file = sys.argv[1]

file = open(file, 'r', encoding='utf8')
book = file.read()

nlp = spacy.load('pt_core_news_md')
# nlp.max_length = 1300000
av = nlp(book)

amiguinhos = []

for s in av.sents:
    amigos_frase = []
    for ent in s.ents:
        if ent[0].ent_type_ == 'PER' or ent.text == 'Harry' and ent.text not in amigos_frase:
            amigos_frase.append(ent.text)
    if len(amigos_frase) > 1:
        amigos_frase.sort()
        pairs = generate_pairs(amigos_frase)
        for pair in pairs:
            amiguinhos.append(pair)

best_friends = Counter(amiguinhos)
print(f'Best friends: f{best_friends.most_common(10)}')
