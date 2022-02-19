# displays the parachute based on how many incorrect guesses a user makes.
class display:

  def parachute(attempts):

    levels = [
        #Initial Full Parachute
        '''
        _____ 
       /     \ 
        -----
       \     /
        \   /
          O
         /|\ 
         / \ 
        ''',
    #First wronng guess
        '''
        /     \ 
         -----
        \     /
         \   /
           O
          /|\ 
          / \ 
        ''',
    #Second wrong guess      
        ''' 
         -----
        \     /
         \   /
           O
          /|\ 
          / \ 
        ''',
    #Third wrong guess      
        ''' 
    
        \     /
         \   /
           O
          /|\ 
          / \ 
        ''',      

    #Forth wrong guess
        '''
    
        \   /
          O
         /|\ 
         / \ 
        ''',     
    #Fifth wrong guess
        '''
    
    
         X
        /X\ 
        / \ 
        ''',    
           
    ]
    return levels[attempts]

    
