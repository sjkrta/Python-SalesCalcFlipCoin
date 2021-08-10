# flip_a_coin

User will be prompt to enter either 'head' or 'tail'
then if it matches their choice, it will print congrats or vice versa
after that user will be asked to choose to play again?
if they choose y, game restarts otherwise ends

#how_it_works

there is five function.
ask_user=> asks to choose head or tail
flip()=> flips the coin
ask_user_again=>if user wants to go again
win_loss=> validates winning or losing
game()=>calls all other function

then after functions are declared game() is called.

# flip_a_coin_without_function

This is very easy and faster way to solve this game.
We just have to create a while loop for a condition play.
We initially set it true and ask user input for head or tail.
then make the match with random import and declare winner.
Now we can ask user for input in while loop again.
if user responds positive we just break inner loop 
otherwise we set play to false and then the loop ends and 
game is over()
