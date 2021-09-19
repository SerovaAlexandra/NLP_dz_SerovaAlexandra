import nltk
from nltk.tokenize import word_tokenize
from string import punctuation
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()


with open ('1_minus.txt', encoding='utf-8') as f1:
    text = f1.read().split('\n')
    minus_list = []
    for elem in text:
        tokenizer = word_tokenize(elem)
        list_of_lemms = []
        for some in tokenizer:
            if some not in punctuation:
                if some.isalpha:
                    some = some.lower()
                    some = morph.parse(some)[0].normal_form
                    list_of_lemms.append(some)
        minus_list.append(list_of_lemms)

first_minus = minus_list[0]
second_minus = minus_list [1]
third_minus = minus_list[2]
forth_minus = minus_list[3]
fifth_minus = minus_list [4]



with open ('1_plus.txt', encoding='utf-8') as f2:
    text = f2.read().split('\n')
    plus_list = []
    for elem in text:
        tokenizer = word_tokenize(elem)
        list_of_lemms2 = []
        for some in tokenizer:
            if some not in punctuation:
                if some.isalpha:
                    some = some.lower()
                    some = morph.parse(some)[0].normal_form
                    list_of_lemms2.append(some)
        plus_list.append(list_of_lemms2)

first_plus = plus_list[0]
second_plus = plus_list [1]
third_plus = plus_list[2]
forth_plus = plus_list[3]
fifth_plus = plus_list [4]