import json
import random


class Reader:

    def __init__(self):

        self.words = 'json_files/words.json'
        self.sentences = 'json_files/sentences.json'

        self.list_words = []
        self.list_sentences = []

        self.result_units_choosen = {}

    def read_json_words(self, lang_1, lang_2):

        self.list_words = []

        with open(self.words, encoding='utf8') as file:
            pairs = json.load(file)
            try:
                for i in range(1,20): # Prevision de un maximo de 20 temas
                    list = []
                    for pair in pairs['words_unit_' + str(i)]:
                        for j in range(1,4): # Prevision de maximo 3 posibles respuestas validas por pregunta
                            try:
                                t = (pair[lang_1 + '_1'],pair[lang_2 + '_' + str(j)])
                                list.append(t)
                            except:
                                pass
                    self.list_words.append(list)
            except:
                pass

    def read_json_sentences(self, lang_1, lang_2):

        self.list_sentences = []

        with open(self.sentences, encoding='utf8') as file:
            pairs = json.load(file)
            try:
                for i in range(1,20): # Prevision de un maximo de 20 temas
                    list = []
                    for pair in pairs['sentences_unit_' + str(i)]:
                        for j in range(1,4): # Prevision de maximo 3 posibles respuestas validas por pregunta
                            try:
                                t = (pair[lang_1 + '_1'],pair[lang_2 + '_' + str(j)])
                                list.append(t)
                            except:
                                pass
                    self.list_sentences.append(list)
            except:
                pass

    def choose_units(self, units, lesson):

        list_units_choosen = []
        self.result_units_choosen = {}

        if lesson == 'words':
            for unit in units:
                list_units_choosen.append(self.list_words[unit-1])
        if lesson == 'sentences':
            for unit in units:
                list_units_choosen.append(self.list_sentences[unit-1])

        for i, unit in enumerate(list_units_choosen):
            for pair in unit:
                if pair[0] in self.result_units_choosen:
                    self.result_units_choosen.setdefault(pair[0], []).append(pair[1])
                else:
                    self.result_units_choosen[pair[0]] = [pair[1]]

    def pop_random_next_combination(self):

        random_key = random.choice(list(self.result_units_choosen.keys()))
        return self.result_units_choosen.pop(random_key), random_key
