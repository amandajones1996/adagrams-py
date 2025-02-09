import random 
import copy
def draw_letters():
    LETTER_POOL = {
        'A': 9, 
        'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2, 
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2, 
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1, 
        'Y': 2, 
        'Z': 1
    }
#make list to return for "hand"
#draw 10 random letters from pool
#reflect letter distribution thats in dict
    hand = []
    for letter, amount in LETTER_POOL.items():
        for num in range(amount):
            hand.append(letter)
            random.shuffle(hand)
    return hand[:10]

def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    for char in word.upper():
        if char not in letter_bank_copy:
            return False
        elif char in letter_bank_copy:
            letter_bank_copy.remove(char)
    return True 

def score_word(word):
    # passes in a string
    # returns an int representing total score
    # if len of word 7-10 than +8 points
    letter_value = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
    ('D', 'G'): 2,
    ('B', 'C', 'M', 'P'): 3,
    ('F', 'H', 'V', 'W', 'Y'): 4,
    ('K',): 5,
    ('J', 'X'): 8,
    ('Q', 'Z'): 10
    }
    score = []
    # iterate through dictionary
    for letter, point in letter_value.items():
        for char in word:
            # if char in word also in keys of dict, add the associated point
            if char.upper() in letter:
                score.append(point)
    #if the length of the word is between 7-10, add 8 pts
    if len(word) in range(7, 11):
        score.append(8)
            
    return sum(score)

def get_highest_word_score(word_list):
# return a tuple with("word", int(score))
    highest_score = 0
    highest_word = ""
    # calculate score of each word in list with helper function
    for word in word_list:
        words_score = score_word(word)
        # if the last word score is greater than current, then update
        if words_score > highest_score:
            highest_score = words_score
            highest_word = word
        # for tied scores
        elif words_score == highest_score:
            # words with length of 10 are highest
            if len(word) == 10 and len(highest_word) != 10:
                highest_word = word
            # if the length of the new word is less length than highest word and highest word is not equal to 10 then new word wins
            elif len(word) < len(highest_word) and len(highest_word) != 10:
                highest_word = word
            # if the lengthes are the same, then use the word already in highest word
            elif len(word) == 10 and len(highest_word) == 10:
                highest_word = highest_word
    final_word = (highest_word, highest_score)
    return final_word