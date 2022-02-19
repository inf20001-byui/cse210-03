class display:
  '''
  Displays the parachute based on how many incorrect guesses a user makes.
  
  Args:
    attempts (int): Uses the number of incorrect attempts to display the proper parachute.
    level (list(string)): list of different levels of the parachute from full to crashed.

  Returns:
    string: returns the single entry from the list that corresponds to the number of incorrect attempts.
  '''
  
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

    
