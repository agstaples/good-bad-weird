from get_jokes import get_dad_joke_string
from random import choice


def make_word_tuples(num_words):
    """from joke string, create word tuples paired with next word(s)"""

    word_groups = {}

    joke_string = get_dad_joke_string()

    joke_words = joke_string.split()

    for i in range(len(joke_words) - num_words):
        word_tuples = tuple(joke_words[i:i + num_words])
        previous_word = joke_words[i - 1]
        next_word = joke_words[i + num_words]

        if word_tuples not in word_groups:
            word_groups[word_tuples] = {
                                        "previous": [],
                                        "next": [],
            }

        word_groups[word_tuples]["previous"].append(previous_word)
        word_groups[word_tuples]["next"].append(next_word)

    return word_groups


def random_forward_markov(num_words):
    """gets upcoming words in joke"""

    word_groups_dict = make_word_tuples(num_words)
    word_tuples_lst = list(word_groups_dict.keys())

    words_group = choice(word_tuples_lst)

    while words_group[0] != "||" or words_group[-1] == "||":
        words_group = choice(word_tuples_lst)

    joke = list(words_group)
    next_word = choice(list(word_groups_dict[words_group]["next"]))

    while next_word != "||" or words_group[-1] != "||":
        if len(words_group) == 3:
            words_group = (words_group[1], words_group[2], next_word)
        elif len(words_group) == 2:
            words_group = (words_group[1], next_word)
        else:
            words_group = next_word

        joke.append(next_word)

        next_word = choice(list(word_groups_dict[words_group]["next"]))

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

    for group in word_tuples_lst:
        if input_word in group and "||" not in group:
            middle_starting_group.append(group)
        else:
            starting_group.append(group)

    if middle_starting_group:
        words_group = choice(middle_starting_group)
    else:
        words_group = choice(starting_group)

    joke = list(words_group)
    next_word = choice(list(word_groups_dict[words_group]["next"]))
    previous_word = choice(list(word_groups_dict[words_group]["previous"]))

    while previous_word != "||" or words_group[0] != "||":
        if len(words_group) == 3:
            words_group = (previous_word, words_group[0], words_group[1])
        elif len(words_group) == 2:
            words_group = (previous_word, words_group[0])
        else:
            words_group = previous_word

        joke.insert(0, previous_word)

        previous_word = choice(list(word_groups_dict[words_group]["previous"])) 

    words_group = (joke[-2], joke[-1])

    while next_word != "||" or words_group[-1] != "||":
        if len(words_group) == 3:
            words_group = (words_group[1], words_group[2], next_word)
        elif len(words_group) == 2:
            words_group = (words_group[1], next_word)
        else:
            words_group = next_word

        joke.append(next_word)

        next_word = choice(list(word_groups_dict[words_group]["next"]))

    new_joke = []

    for word in joke:
        if word != "||":
            new_joke.append(word)

    return " ".join(new_joke)









































