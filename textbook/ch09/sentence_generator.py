import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

adjectives = ['happy', 'sad', 'bright', 'dark']
nouns = ['dog', 'cat', 'car', 'house']
adverbs = ['quickly', 'slowly', 'eagerly', 'lazily']
verbs = ['run', 'jump', 'swim', 'drive']

pos_dict = {
    'JJ': adjectives,  # 形容詞
    'NN': nouns,       # 名詞
    'RB': adverbs,     # 副詞
    'VB': verbs        # 動詞
}

def replace_words(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    return ' '.join([random.choice(pos_dict.get(tag[:2], [word])) for word, tag in tagged_words])

input_text = "The quick brown fox jumps over the lazy dog."
print("Original Text: ", input_text)
print("Generated Text: ", replace_words(input_text))
