from telnetlib import STATUS
from game.wordlist import word_list
from game.jumper import game_play
from game.jumper import select_word

class Director:
    """
    A person who directs the game.
    The repsonsibility of this Class to start the game and control when it ends. 
    It uses a while loop to ask if the player would like to play again after winning or losing a game.  

    Attributes:
        get_word = The word to guess
        playing = whether or not the game is over

    """
    def start_game(self):
        word = select_word.get_word(self)
        game_play.playing(self,word)
        while input('Play again? (y/n) ') =='y':
            word = select_word.get_word(self)
            game_play.playing(self,word)

    
    if __name__ == '__main__':
        start_game()
