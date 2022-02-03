from game.parachute import parachute
from game.wordlist import word_list
from game.format import color

import random

class select_word:
    def get_word(self):
    #This will randomly select the word
        word = random.choice(word_list)
        return word
  
class game_play:
    def playing(word):
        word_display = '-' * len(word)
        letter_correct = False
        letters_guessed = []
        attempts = 0

        print('')
        print(color.BOLD + 'Are you ready to jump?' + color.END)
        print(parachute(attempts))
        print(word_display)
        print('')

        while not letter_correct and attempts < 5:
            letter = input('Guess a Letter [a-z]: ')
            if len(letter) == 1 and letter.isalpha():
                if letter in letters_guessed:
                    print(color.RED, 'You already guessed that letter', letter, color.END)
                    
                elif letter not in word:
                    print(color.RED, letter, 'is not in the word!', color.END)
                    attempts = attempts + 1
                    letters_guessed.append(letter)
                    print(parachute(attempts))
                    print(word_display)
                    print('')
                else:
                    print(color.GREEN, 'You have guessed correctly', letter ,'is in the word!', color.END)
                    letters_guessed.append(letter)
                    word_as_list = list(word_display)
                    print(parachute(attempts))
                    print(word_display)
                    print('')
            else:
                print(color.RED,'Not a valid guess!', color.END)
                

        if letter_correct:
            print(color.BOLD,color.BLUE,'Congrats, you guessed the word! You win!', color.END)
            print('')
        else:
            print(color.BOLD, color.RED,'Sorry, you lost your parachute and crashed', color.END)
            print('')
            print(color.ORANGE,'The correct word was ' + word, color.END )
            print('')


class Director:   
    def start_game(self):
        word = select_word.get_word(self)
        game_play.playing(word)
        while input('Play again? (y/n) ') =='y':
            word = select_word.get_word(self)
            game_play.playing(word)

    
    if __name__ == '__main__':
        start_game()
