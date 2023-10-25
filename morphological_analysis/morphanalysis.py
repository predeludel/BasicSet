import nltk
import pymorphy2
from collections import Counter
import operator


def get_words_text(name_text):
    with open(f'{name_text}.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    return nltk.tokenize.RegexpTokenizer(r"\w+").tokenize(text)


def get_tags(text_word):
    morph = pymorphy2.MorphAnalyzer()
    word_tags = []
    for token in text_word:
        tag = morph.parse(token)[0].tag.POS
        word_tags.append((token, morph.parse(token)[0].tag.POS))
    return word_tags


def analysis_lexical_usage(index, name_text):
    words = get_words_text(name_text)
    count = Counter(get_tags(words))
    sorted_x = sorted(count.items(), key=operator.itemgetter(1))
    list_tags = ["NOUN", "ADJF", "ADJS", "COMP", "VERB", "INFN", "PRTF", "PRTS", "GRND", "NUMR", "ADVB", "NPRO", "PRED",
                 "PREP", "CONJ", "PRCL", "INTJ"]
    words_all = []
    for tags in list_tags:
        count = 0
        word = ""
        for i in sorted_x:
            if i[0][1] == tags:
                if count < i[1]:
                    count = i[1]
                    word = i[0][0]
        words_all.append([index, name_text, count, word, tags])
    return words_all


if __name__ == '__main__':
    print(analysis_lexical_usage(1839, "ПриключенияОливераТвиста1839"))
    print(analysis_lexical_usage(1841, "БарнебиРадж1841"))
    print(analysis_lexical_usage(1844, "ЖизньИприключенияМартинаЧезлвита1844"))
    print(analysis_lexical_usage(1848, "ДомбиИсын1848"))
    print(analysis_lexical_usage(1853, "ХолодныйДом1853"))
    print(analysis_lexical_usage(1857, "КрошкаДоррит1857"))
