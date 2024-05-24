# import module
import random
import time

print("Hello😊")
time.sleep(2)
name = input("what is your name: ")
time.sleep(1)
print("Good day🕺", name)
print("Welcome to Letter Quest: Country")
# defining a function named PLAY GAME
def playgame():
    print("Please Enter Yes or No")
    play = input("Can we play a game: ")


    if play == "Yes" or play == "yes":
        print('Good')
        print("""
      Before we start this game.
        This game is all about guessing countries that start with any letters.
        Here, We have from countries that start with letter A - J.
        So, This game is just about getting countries that start from A, if u got it , You proceed to B, but if You didn't.. You will start from A again...
        You don't have to miss any of the letters...
        And again... while writing start with capital letter...
        Good luck!!!
        """)
        global length
        time.sleep(5)
        def game():
            print("Please start with Upper Case")
            countries_to_guess_A = ['Afghanistan', 'Angola', 'Australia','Argentina','Algeria','Andorra','Albania']
            word = random.choice(countries_to_guess_A)
            length = len(word)
            print("Countries with", length,"letters that start with letter A")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_B = ['Belgium', 'Brazil', 'Botswana','Belarus','Bolivia','Benin','Bulgaria']
            word = random.choice(countries_to_guess_B)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter B")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_C = ['Cameroon', 'Canada', 'Chad','China','Croatia','Colombia','Costa Rica']
            word = random.choice(countries_to_guess_C)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter C")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_D = ['Demark', 'Dominica',]
            word = random.choice(countries_to_guess_D)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter D")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_E= ['Egypt', 'Ecuador', 'Ethiopia','Eritrea','Estonia']
            word = random.choice(countries_to_guess_E)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter E")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_F = ['France', 'Finland', 'Fiji','Belarus']
            word = random.choice(countries_to_guess_F)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter F")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_G = ['Gambia', 'Ghana', 'Greece','Guinea-Bissau','Germany','Georgia','Gabon']
            word = random.choice(countries_to_guess_G)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter G")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_H = ['Haiti', 'Hungary', 'Hawaii','Hanover','Hesse',]
            word = random.choice(countries_to_guess_H)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter H")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_I = ['Iceland', 'Iran', 'Iraq','India','Italy','Isreal','Indonesia','Ireland']
            word = random.choice(countries_to_guess_I)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter I")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            countries_to_guess_J = ['Jamaica', 'Japan','Jordan']
            word = random.choice(countries_to_guess_J)
            display_word = word
            length = len(word)
            print("Countries with", length,"letters that start with letter J")
            guess = input('> ')
            if guess == word:
                print("Congratulation")
            elif guess != word:
                print(f"""
                   Sorry!
                   The country was {word}
                   You didn't get it.
                   You have to start again.
                """)
                game()
            def conclude():
                print(f"""
                Congratulation", {name} "on finishing the game
                That was really smart of you.
               
                """)
            conclude()
            again = input("Can we play again: ")
            if play == "Yes" or play == "yes":
                game()
            elif play == "No" or play == "no":
                print("ThanK you for your time, see you next time.")
            else:
                print("Invalid Input")
                playgame()
        game()
    elif play == "No" or play == "no":
        print("Thank you for your time, see you next time.")
    else:
        print("Invalid Input")
        playgame()
playgame()


