from telnetlib import STATUS
from game.wordlist import word_list
from game.jumper import game_play
from game.jumper import select_word

class Director:
    """
    A person who directs the game.
    The repsonsibility of this Class to start the game and control when it ends.   

    Attributes:
        word = The word to guess


    """
    def start_game(self):
        word = select_word.get_word(self)
        game_play.playing(self,word)
        while input('Play again? (y/n) ') =='y':
            word = select_word.get_word(self)
            game_play.playing(self,word)

    
    if __name__ == '__main__':
        start_game()
