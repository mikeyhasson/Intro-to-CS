#################################################################
# FILE : hangman.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex4 2020
# DESCRIPTION: Hangman is a classic word game in which you guess secret words
#################################################################
import hangman_helper
UNKNOWN_LETTER="_"
DEF_PENALTY=1
LETTER=hangman_helper.LETTER
WORD=hangman_helper.WORD
HINT=hangman_helper.HINT
HINT_LENGTH = hangman_helper.HINT_LENGTH
POINTS_INITIAL = hangman_helper.POINTS_INITIAL
"""messages"""
INPUT_NOT_VALID_MSG="User input is not valid. Please try again"
LETTER_ALREADY_CHOSEN_MSG="You've already chosen this letter. Please choose a different one"
CORRECT_LETTER_MSG="That was a great choice of letter!"
WRONG_LETTER_MSG = "That letter was not in the word, try again!"
CORRECT_WORD_MSG = "great job, you've guessed the correct word"
WRONG_WORD_MSG = "Word guess is incorrect"
HINTS_LIST_MSG="I've produced a list of hints "
WIN_MSG="Congrats! You've won!"
LOSE_MSG="You lose. Better luck next time.The word was "
GAME_START_MSG="welcome to the game"

def update_word_pattern(word,pattern,letter):
    """this function updates the game pattern, according to a recieved letter changing the underlines into a
    discovered letter.
    :param:word:the word the played is supposed to discover, on which the pattern is based
    :param:pattern:the word with undiscovered letter being signified as _(underline)
    :param:letter:the letter the user discovered.
    :return:the updated pattern
    """
    pattern_list=list(pattern)
    index=-1
    for current_letter in word:
        index+=1
        if current_letter==letter:
            pattern_list[index]=current_letter
    return "".join(pattern_list)
def user_new_score_calculate(n):
    """this function calculates the addition of points to the user according to a defined formula
    :param:n: number of times the letter appears in the word
    :return:how many points need to be added
    """
    return n*(n+1)//2

def user_choice_letter (user_choice,score,wrong_guess_lst,pattern,chosen_word):
    """this function is used when the user chooses a letter.
    :param:user_choice:the letter the user guessed
    :param:score:the user's current score
    :param:wrong_guess_lst:list of letters that were already guessed but aren't in the word
    :param:current pattern, with letters not guessed marked as an underline
    :param:chosen_word:the word the user is supposed to find
    :return: updated score,wrong guesses list,pattern and a message for the user to see
    """
    if len(user_choice) > 1 or user_choice.isupper() or not user_choice.isalpha(): #invalid inputs
        message = INPUT_NOT_VALID_MSG
    elif user_choice in wrong_guess_lst or user_choice  in pattern:
        message = LETTER_ALREADY_CHOSEN_MSG
    else:
        score -= DEF_PENALTY
        if user_choice in chosen_word:
            pattern = update_word_pattern(chosen_word, pattern, user_choice)
            number_of_appearences = pattern.count(user_choice)  # number of times the user choice is in the pattern
            score += user_new_score_calculate(number_of_appearences)
            message = CORRECT_LETTER_MSG
        else:
            wrong_guess_lst.append(user_choice)
            message = WRONG_LETTER_MSG
    return score,wrong_guess_lst,pattern,message

def user_choice_word (user_choice,score,pattern,chosen_word):
    """this function is used when the user chooses a letter.
    :param:user_choice:the letter the user guessed
    :param:score:the user's current score
    :param:current pattern, with letters not guessed marked as an underline
    :param:chosen_word:the word the user is supposed to find
    :return: updated score,pattern and a message for the user to see
    """
    score -= DEF_PENALTY
    if user_choice == chosen_word:
        number_of_appearences = pattern.count(UNKNOWN_LETTER)
        score += user_new_score_calculate(number_of_appearences)
        pattern = chosen_word
        message= CORRECT_WORD_MSG
    else:
        message = WRONG_WORD_MSG
    return score,pattern,message

def user_choice_hint (score,wrong_guess_lst,pattern,words_list):
    """this function is used when the user chooses a hint. it produces a list of potential words that match the pattern
    letters in the wrong guesses list will not be in this list. the list's maximum length is HINT_LENGTH (=3),
    :param:score:the user's current score
    :param:wrong_guess_lst:list of letters that were already guessed but aren't in the word
    :param:current pattern, with letters not guessed marked as an underline
    :param:chosen_word:the word the user is supposed to find
    :return: updated score and a message for the user to see
    """
    score -= DEF_PENALTY
    full_hints_list = filter_words_list(words_list, pattern, wrong_guess_lst) #producing a list of potential words
    if len(full_hints_list) > HINT_LENGTH: #if produced list is too large we will shorten it
        short_hints_list = list() #creating a short list,original indexes (0, 1*n//HINT_LENGTH,2*n//HINT_LENGTH....
                                                                                 # (HINT_LENGTH - 1)n//HINT_LENGTH
        i=0
        while len(short_hints_list) < HINT_LENGTH and i<HINT_LENGTH :
            org_index = len(full_hints_list) * i // HINT_LENGTH
            short_hints_list.append(full_hints_list[org_index])
            i+=1
        hangman_helper.show_suggestions(short_hints_list)
    else:
        hangman_helper.show_suggestions(full_hints_list)#if produced list size is good.
    message = HINTS_LIST_MSG
    return score,message




def run_single_game(words_list,score):
    """this function runs the game for one time.
    :param words_list: list of pontential words for the game
    :param score: the initial amount of points the user has
    :return: the score after the game.
    """
    chosen_word = hangman_helper.get_random_word(words_list)
    wrong_guess_lst=list()
    pattern=UNKNOWN_LETTER*len(chosen_word)
    message= GAME_START_MSG
    while pattern!=chosen_word and score!=0:
        hangman_helper.display_state(pattern, wrong_guess_lst, score,message)
        user_choice_type,user_choice=hangman_helper.get_input()
        if user_choice_type==LETTER:
            score, wrong_guess_lst, pattern, message = user_choice_letter(user_choice, score, wrong_guess_lst, pattern,
                                                                          chosen_word)
        if user_choice_type == WORD:
            score, pattern, message=user_choice_word (user_choice,score,pattern,chosen_word)
        if user_choice_type == HINT:
            score,message=user_choice_hint(score, wrong_guess_lst, pattern, words_list)

    if score==0:
        message= LOSE_MSG + chosen_word
    else:
        message=WIN_MSG
    hangman_helper.display_state(pattern, wrong_guess_lst, score, message)
    return score

def main():
    """the main function of the game. uses the function "run_single_game" to allow mulitple games."""
    words_list = hangman_helper.load_words()
    rounds_played = 0
    points=POINTS_INITIAL
    play_again=True
    while play_again:
        points=run_single_game(words_list,points)
        rounds_played+=1
        if points>0:
            play_again=hangman_helper.play_again("you have played " + str(rounds_played) + " rounds already. You have "
                                         + str(points) + " points. would you like to play another round?")
        else:
            play_again =hangman_helper.play_again("You lost. You have played " + str(rounds_played) + " rounds. "
                                    "would you like to play a new game?")
            points=POINTS_INITIAL
            rounds_played=0

def filter_words_list(words, pattern, wrong_guess_lst):
    """
    This function takes an existing list of words and returns the ones who match the pattern. words that contain letters
    in "wrong_guess_lst" will not be included.
    :param words:list of potential words
    :param pattern:the pattern to match
    :param wrong_guess_lst:list of letters not to be included in the words
    :return:new sorted list
    """
    new_lst=list()
    for word in words:
        if len(word)!=len(pattern):
            continue
        index=-1
        for a in pattern:
            index+=1
            if word[index] in wrong_guess_lst:
                break
            if a == UNKNOWN_LETTER:
                if word[index] in pattern:
                    break
            elif a != word[index]:
                break
        else:
            new_lst.append(word)
    return new_lst


if __name__ == '__main__':
    main()

