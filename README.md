# Wordle Recommender
A naive way to generate suggestions for the game of wordle

## Instructions

In order to start the script simply run `python main.py` and follow the screen prompts.
The script makes calls to [datamuse api](https://www.datamuse.com/api/). For example, if you
pass `https://api.datamuse.com/words?sp=t??k` to the api, the api will return "*words that start 
with t, end in k, and have two letters in between*". 