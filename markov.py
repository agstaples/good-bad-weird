from get_jokes import get_dad_joke_string
from random import choice
import string


def memoize(function):
    """memoizes results of making word tuples"""

    memo = {}

    # checks if results already memoized, adds if not
    def helper_func(*args):
        if args not in memo:            
            memo[args] = function(*args)
        return memo[args]
    return helper_func

@memoize
def make_word_tuples(num_words=2):
    """from joke string, create word tuples paired with next word(s)"""


    word_groups = {}

    joke_string = get_dad_joke_string()

    joke_words = joke_string.split()

    # creating word grouping
    for i in range(len(joke_words) - num_words):
        word_tuples = tuple(joke_words[i:i + num_words])
        previous_word = joke_words[i - 1]
        next_word = joke_words[i + num_words]

        if word_tuples not in word_groups:
            word_groups[word_tuples] = {
                                        "previous": [],
                                        "next": [],
            }

        # adding previous and next words to grouping values
        word_groups[word_tuples]["previous"].append(previous_word)
        word_groups[word_tuples]["next"].append(next_word)

    return word_groups
    

def random_forward_markov(num_words=2):
    """generated random joke"""

    word_groups_dict = make_word_tuples(num_words)
    word_tuples_lst = list(word_groups_dict.keys())

    words_group = choice(word_tuples_lst)

    # ensuring we're starting at beginning of joke
    while words_group[0] != "||":
        words_group = choice(word_tuples_lst)
    
    joke = list(words_group)
    next_word = choice(list(word_groups_dict[words_group]["next"]))

    # checking for end of joke
    # for single word chains check if current or next word is end marker ("||") 
    # for multiple word chains, check if next or last of current is "||"
    if num_words == 1:
        while next_word != "||" or words_group[0] == "||":
            words_group = (next_word,)

            joke.append(next_word)

            next_word = choice(list(word_groups_dict[words_group]["next"]))
    else:
        while next_word != "||" or words_group[-1] != "||":
            if len(words_group) == 3:
                words_group = (words_group[1], words_group[2], next_word)
            elif len(words_group) == 2:
                words_group = (words_group[1], next_word)

            joke.append(next_word)

            next_word = choice(list(word_groups_dict[words_group]["next"]))

    # removing start and end markers from joke
    new_joke = []

    for word in joke:
        if word != "||":
            new_joke.append(word)

    return " ".join(new_joke)


def multi_directional_markov(input_word, num_words=2):
    """takes in a single word and builds a chain going first backward and then forward"""

    word_groups_dict = make_word_tuples(num_words)

    word_tuples_lst = list(word_groups_dict.keys())

    middle_starting_group = []
    starting_group = []

    new_joke = []
    index_joke = []

    # setting preference for starting in the middle of a joke instead of the start or end
    for group in word_tuples_lst:
        if input_word in group and "||" not in group:
            middle_starting_group.append(group)
        else:
            starting_group.append(group)

    if middle_starting_group:
        words_group = choice(middle_starting_group)
    else:
        words_group = choice(starting_group)

    # starting joke from middle and capturing previous and next
    joke = list(words_group)
    next_word = choice(list(word_groups_dict[words_group]["next"]))
    previous_word = choice(list(word_groups_dict[words_group]["previous"]))

    # adding previous words to joke until marker ("||") hit
    while previous_word != "||" or words_group[0] != "||":
        if num_words == 3:
            words_group = (previous_word, words_group[0], words_group[1])
        elif num_words == 2:
            words_group = (previous_word, words_group[0])
        else:
            words_group = (previous_word,)

        joke.insert(0, previous_word)

        previous_word = choice(list(word_groups_dict[words_group]["previous"])) 

    # establishing word group from end of current joke to move forward from
    if num_words == 3:
        words_group = (joke[-3], joke[-2], joke[-1])
    elif num_words == 2:
        words_group = (joke[-2], joke[-1])
    else:
        words_group = (joke[-1])

    # getting word index for red text formatting in html 
    # (+ 1 to account for front end word index starting at 1 instead of 0)
    for word in joke:
        if word != "||":
            index_joke.append(word)
    index_marker = max(i for i, word in enumerate(index_joke) if word == input_word) + 1

    # adding next words to joke until marker ("||") hit
    while next_word != "||" or words_group[-1] != "||":
        if num_words == 3:
            words_group = (words_group[1], words_group[2], next_word)
        elif num_words == 2:
            words_group = (words_group[1], next_word)
        else:
            words_group = (next_word,)

        joke.append(next_word)

        next_word = choice(list(word_groups_dict[words_group]["next"]))

    # removing start and end markers from joke
    for word in joke:
        if word != "||":
            new_joke.append(word)

    return (" ".join(new_joke), index_marker)








































