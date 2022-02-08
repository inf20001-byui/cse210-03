from telnetlib import STATUS
from game.parachute import parachute
from game.wordlist import word_list
from game.format import color

import random

class select_word:
    # This will randomly select a word using the word_list function in wordlist.py file.
    def get_word(self):
        word = random.choice(word_list)
        return word
  
class game_play:
    #Class the controls the play of the game.
    def playing(self,word):
        # Setup for the basic function of the game.
        self._word_display = '-' * len(word) # Display one dash for each letter until the letter is guessed.
        self._letter_correct = False # Sets that the word is solved to false.
        letters_guessed = [] # Keeps track of the letters already guessed by the player.
        attempts = 0 # Counts incorrect attempts at letters.

        #Displays the beginning of the game.
        print('')
        print(color.BOLD + 'Are you ready to jump?' + color.END)
        print(parachute(attempts))
        print(self._word_display)
        print('')

        while not self._letter_correct and attempts < 5:
            #Loop to begin tracking the number of incorret guesses and will end the game after 5.
            letter = input('Guess a Letter [a-z]: ')
            if len(letter) == 1 and letter.isalpha():
                if letter in letters_guessed:
                    print(color.RED, 'You already guessed that letter', letter, color.END)
                    
                elif letter not in word:
                    #Statement to show that the letter guessed was incorrect then increment the attempt counter.
                    print(color.RED, letter, 'is not in the word!', color.END)
                    attempts = attempts + 1
                    letters_guessed.append(letter)
                    print(parachute(attempts))
                    print(self._word_display)
                    print('')
                else:
                    #Statement to show that the letter guessed was correct
                    print(color.GREEN, 'You have guessed correctly', letter ,'is in the word!', color.END)
                    letters_guessed.append(letter)
                    word_list = list(word)
                    print(parachute(attempts))
                    self._word_display = ''
                    for letter in word_list:
                        if letter in letters_guessed:
                            self._word_display += letter
                        else:
                            self._word_display += '-'
                    print(self._word_display)
                    print('')
                    if '-' not in self._word_display: #If all the letters have been guessed, there should be no '-' left so the world has been solved.
                        self._letter_correct = True
            else:
                #Basic error checking of a non-valid character is entered.
                print(color.RED,'Not a valid guess!', color.END)
                

        if self._letter_correct:
            #Output to show the player won.
            print(color.BOLD,color.BLUE,'Congrats, you guessed the word! You win!', color.END)
            print('')
        else:
            #Output to show the player lost.
            print(color.BOLD, color.RED,'Sorry, you lost your parachute and crashed', color.END)
            print('')
            print(color.ORANGE,'The correct word was ' + word, color.END )
            print('')


class Director:
    #Class to start the game and control when it ends.   
    def start_game(self):
        word = select_word.get_word(self)
        game_play.playing(self,word)
        while input('Play again? (y/n) ') =='y':
            word = select_word.get_word(self)
            game_play.playing(self,word)

    
    if __name__ == '__main__':
        start_game()
