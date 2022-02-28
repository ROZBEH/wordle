# Wordle Recommender
A naive way to generate suggestions for the game of wordle

## Instructions

In order to start the script simply run `python main.py` and follow the screen prompts.
The script makes calls to [datamuse api](https://www.datamuse.com/api/). For example, if you
pass `https://api.datamuse.com/words?sp=t??k` to the api, the api will return "*all the words that start 
with t, end in k, and have two letters in between*". 

## Couple of Notes
- The algorithm starts with a bunch of precusrsor suggestions. I just picked whatever word that came to my mind. One doesn't have to follow them. You can simply put whatever word you see as better fit. 
- Once you make a suggestion, you then have to give a feedback to the script on how well the suggestions are by specifying something like `iicai`. 
`c:correct letter, correct spot`
`a:correct letter, wrong spot`
`i:wrong letter`
- After the feedback, the algorithm check which of the chars were correct and which ones are at the wrong place.
Let's say the suggestion was `tesla` but the actual word is `their` so the feedback should be `caiia` which you 
can infer based on the colors in the game. Once done, the algorithm then calls the api with the following query.
`t????` which means that find all the 5 letter words that start with `t`. Among those, it then searches for the words
that are allowed by checking which of the chars are among the forbidden chars. Please check the code for more details.
- It is designed for the hard mode of wordle but it should work with easy mode too.
- Although I tried it with a lot of wordle archive cases and it worked but it might fail
at some of the edge cases.
- The algorithm that I used might not be the most efficient ones in terms of big O. It has elements 
of brute force in it.