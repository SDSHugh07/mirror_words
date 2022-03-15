# /bin/env python
# coding: utf-8

"""
collection of functions to support reversing the characters within the words of a sentence
"""

from queue import Queue

queue_split_sentence = Queue()
queue_reversed_words = Queue()

delimiters = [' ', ',', '.']

def reverse_word(word):
    """
    description: reverse the characters in a word
    input:
        'word': the word to be reversed
    output:
        the reversed word
    """

    i = len(word)

    reversed_word = ""

    while i > 0:
        reversed_word += word[i-1]
        i = i-1

    return reversed_word

def mirror_words(sentence, length):
    """
    description: a function to reverse the characters within the words of a sentence, while preserving the
    original word order

    word order is preseved by leveraging the properties of a Python standard library Queue (FIFO)

    input:
        'sentence': a sentence containing words to be reversed
        'length': the length of input 'sentence'

    output:
        the sentence containing words with their characters reversed
    """

    str_current_word = ""
    i = 0

    """
    NOTE: the 'pythonic' way would be to to use '#for character in sentence:',
    but to adhere to the guidelines of the exercise, iterating with the 'length' 
    argument
    """
    while i < length:
        character = sentence[i]
        if character in delimiters:
            #we've encountered a delimeter after a valid word
            if len(str_current_word) > 0:
                queue_split_sentence.put(str_current_word)
                queue_split_sentence.put(character)
                str_current_word = ""
            #we've encountered a lone delimeter
            else:
                queue_split_sentence.put(character)
        else:
            str_current_word += character

        i += 1

    #we've encountered a final word without a terminating delimeter
    if len(str_current_word) > 0:
        queue_split_sentence.put(str_current_word)

    reversed_sentence = ""

    while queue_split_sentence.qsize() > 0:
        item = queue_split_sentence.get()
        if item in delimiters:
            queue_reversed_words.put(item)
        else:
            queue_reversed_words.put(reverse_word(item))

    #recompose the sentence
    while queue_reversed_words.qsize() > 0:
        item = queue_reversed_words.get()
        reversed_sentence += item

    return reversed_sentence

if __name__ == "__main__":
    list_sentences = [
        "",
        " ",
        ",",
        ".",
        "..",
        ",.",
        "I",
        "One",
        "One.",
        ".One.",
        "..One..",
        "One.Two",
        ".One.Two.",
        "..One..Two..",
        "One two, I three.  Four.",
        ]

    for sentence in list_sentences:
        print("original sentence: " + sentence)
        new_sentence = mirror_words(sentence, len(sentence))
        print("mirrored sentence: " + new_sentence + "\n")


