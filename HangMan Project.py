import random

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
already_guessed = set()


print (hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

 

    #Check guessed letter
    for position in range(word_length): 
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter
    
    if guess in already_guessed:
            print ("You already guessed that letter! dummy!")

    else:
        already_guessed.add(guess)
        
    #Check if user is wrong.
    if guess not in chosen_word:
        
        lives -= 1
        print (f"You got one wrong, lost a life, lives left = {lives}" )
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters if so end game
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(hangman_art .stages[lives])