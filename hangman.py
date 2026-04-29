"""
Hangman Game
A simple text-based word guessing game.
"""

import random


def display_hangman(tries):
    """Display the hangman figure based on remaining tries."""
    stages = [
        # Final state: head, torso, both arms, both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # 5 tries left
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # 4 tries left
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # 3 tries left
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,
        # 2 tries left
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        # 1 try left
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
           -
        """,
        # 0 tries left (initial empty state)
        """
           --------
           |      
           |      
           |      
           |      
           |      
           -
        """
    ]
    return stages[tries]


def play_game():
    """Main game function."""
    # List of 5 predefined words
    words = ["python", "hangman", "programming", "developer", "computer"]
    
    # Select a random word
    word = random.choice(words)
    
    # Game variables
    guessed_letters = []
    tries = 6
    word_letters = set(word)
    
    print("=" * 50)
    print("       WELCOME TO HANGMAN!")
    print("=" * 50)
    print("\nGuess the word, one letter at a time.")
    print(f"You have {tries} incorrect guesses allowed.\n")
    
    while len(word_letters) > 0 and tries > 0:
        # Display current game state
        print(display_hangman(tries))
        
        # Show the word with guessed letters revealed
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord: " + display_word)
        
        # Show guessed letters
        print(f"\nGuessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining tries: {tries}")
        
        # Get user input
        guess = input("\nEnter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in word_letters:
            word_letters.remove(guess)
            print(f"\nCorrect! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"\nSorry, '{guess}' is not in the word.")
        
        print("-" * 50)
    
    # Game over - display final result
    print(display_hangman(tries))
    
    if tries > 0:
        print("\n" + "=" * 50)
        print(f"       CONGRATULATIONS! YOU WON!")
        print(f"       The word was: {word.upper()}")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("       GAME OVER!")
        print(f"       The word was: {word.upper()}")
        print("=" * 50)


def main():
    """Main entry point."""
    while True:
        play_game()
        
        # Ask to play again
        print("\nDo you want to play again? (yes/no)")
        response = input("Enter: ").lower()
        
        if response not in ["yes", "y"]:
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()