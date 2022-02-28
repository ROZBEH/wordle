'''
A very simple python script to generate a set of suggestions for the game of wordle.
It assumes that you have access to the internet since it needs to call datamuse api.
You can read more about the API here.
# https://www.datamuse.com/api/
'''
__author__      = "Rouzbeh Shirvani"

import requests
import itertools
precursor_words = ['tesla', 'daisy', 'crook', 'state', 'vapor', 'urban', 'raise', 'pluto', 'nancy', 'mazed', 'mazed']
start_word_idx = 0
current_word = precursor_words[start_word_idx]
all_responses = precursor_words
chars_forbidden = {0:[], 1:[], 2:[], 3:[], 4:[]}
chars_none = []
while True:
    print(all_responses[0:8])
    current_word = str(input('Please select one word from the above options.\nYou can also choose your own word of interest\n'))
    user_input = str(input('Enter the correctness of my prediction: \n options are c:correct, i:incorrect, a:almost correct\n'))
    if len(user_input) != 5:
        print('please enter valid options')
    else:
        correct_idxes = [pos for pos, char in enumerate(user_input) if char == 'c']
        almost_correct_idxs = [pos for pos, char in enumerate(user_input) if char == 'a']
        incorrect_idxs = [pos for pos, char in enumerate(user_input) if char == 'i']
        for item in almost_correct_idxs:
            chars_forbidden[item].append(current_word[item])
        for item in incorrect_idxs:
            chars_forbidden[item].append(current_word[item])
        almost_correct_chars = [current_word[i] for i in almost_correct_idxs]
        incorrect_chars = [current_word[i] for i in incorrect_idxs]
        correct_chars = [current_word[i] for i in correct_idxes]
        intersection_chars_1 = list(set(correct_chars).intersection(incorrect_chars))
        intersection_chars_2 = list(set(almost_correct_chars).intersection(incorrect_chars))
        incorrect_chars = set(incorrect_chars) - set(intersection_chars_1) - set(intersection_chars_2)
        chars_none += incorrect_chars
        print("...Generating the next set of suggestions ... please wait ...")
        # If none of the predictions are correct or even almost correct
        if len(incorrect_idxs) == 5:
            start_word_idx += 1
        # If some of the predictions are almost correct and all others are incorrect
        elif len(correct_idxes) == 0 and len(almost_correct_idxs) > 0:
            all_responses = []
            almost_correct_chars_joined = ''.join(almost_correct_chars)
            chars_with_unknowns = almost_correct_chars_joined + '?'*(5-len(almost_correct_chars_joined))
            str_permutation = list(itertools.permutations(chars_with_unknowns,len(chars_with_unknowns)))
            str_permutation = [''.join(item) for item in str_permutation]
            str_permutation = list(set(str_permutation))
            for item in str_permutation:
                response = requests.get("https://api.datamuse.com/words?sp=" + item + "&max=1000")
                response_json = response.json()
                for res in response_json:
                    if res['word'] not in all_responses:
                        incorrect_intersection = list(set(list(res['word'])).intersection(chars_none))
                        almost_correct_intersection = list(set(list(res['word'])).intersection(almost_correct_chars))
                        if len(incorrect_intersection)==0 and len(almost_correct_intersection)==len(almost_correct_chars) and res['word'].find(' ') == -1:
                            add_word = True
                            for i, ch in enumerate(res['word']):
                                if ch in chars_forbidden[i]:
                                    add_word = False
                            if add_word:
                                all_responses.append(res['word'])
        # If some of the predictions are almost correct and all others are incorrect
        else:
            all_responses = []
            query_item = ['?']*5
            for item in correct_idxes:
                query_item[item] = current_word[item]
            query_item = ''.join(query_item)
            response = requests.get("https://api.datamuse.com/words?sp=" + query_item + "&max=1000")
            response_json = response.json()
            for res in response_json:
                if res['word'] not in all_responses:
                    incorrect_intersection = list(set(list(res['word'])).intersection(chars_none))
                    almost_correct_intersection = list(set(list(res['word'])).intersection(almost_correct_chars))
                    if len(incorrect_intersection)==0 and len(almost_correct_intersection)==len(almost_correct_chars) and res['word'].find(' ') == -1:
                        add_word = True
                        for i, ch in enumerate(res['word']):
                            if ch in chars_forbidden[i]:
                                add_word = False
                        if add_word:
                            all_responses.append(res['word'])
