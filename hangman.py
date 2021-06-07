import random
from datetime import date

def language_choice():
    print(f"{nickname}, please select from the following \nSpanish\nPolish\nEnglish")
    ind = 1
    while ind > 0:
        x = input("Choose a language: ").lower()
        if x == "spanish":
            from words import spanish_list as wordlist
            ind -= 1
        elif x == "english":
            from words import english_list as wordlist
            ind -= 1
        elif x == "polish":
            from words import polish_list as wordlist
            ind -= 1
        else:
            print(f'{nickname}!!! Type in the language you have chosen correctly. Do I REALLY need to tell you '
                  f'everything?')
    return wordlist


def secret_word():
    wordlist = language_choice()
    secret = random.choice(wordlist)
    return secret.upper()


def difficulty():
    print(f"Do you like a challenge, {nickname}?"
          " Or are you a wee babe fresh from the womb?"
          " \nChoose game difficulty (EASY/HARD/NIGHTMARE): ")
    ind = 1
    while ind > 0:
        diff_lvl = input().upper()
        if diff_lvl == "EASY":
            tries = 9
            ind = 0
        elif diff_lvl == "HARD":
            tries = 6
            ind = 0
        elif diff_lvl == "NIGHTMARE":
            tries = 3
            ind = 0
        else:
            print(f"Did I stutter? Easy or Hard, {nickname}?")
    return tries


def gameplay(secret):
    word_completion = "_" * len(secret)
    guessed = 0
    guessed_letters = []
    guessed_words = []
    tries = difficulty()
    print(f"Let's play Hangman {nickname}!")
    if tries == 6:
        print(f"We're going down in the blaze of GLORY {nickname}!!!")
    elif tries == 9:
        print("Easy mode? Crybaby.")
    else:
        print(f"Welcome to Hell, {nickname}. MWAHAHAHAHAHA!!!")
    print(hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please take a wild guess, a single letter or the entire word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have guessed this letter already!", guess)
            elif guess not in secret:
                print(guess, "is not in the word, sorry luv!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!", guess, "is a part of the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(secret) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed += 1
        elif len(guess) == len(secret) and guess.isalpha():
            if guess in guessed_words:
                print("You have guessed this word already!", guess)
            elif guess != secret:
                print(guess, "is not the word you are looking for, sorry luv!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = secret
        else:
            print(f"Are you trying to cheat me, little {nickname}? The Lord of the Hanged?")
        print(hangman(tries))
        print(word_completion)
        print("\n")
    if guessed > 0:
        global wins
        wins += 1
        print("Congrashuleyshins, GOD how do you even spell this word... Congratz! You got the word :)")
    else:
        global losses
        losses += 1
        print("You absolute buffoon, it was " + secret + ". Now you will DIE!!!")



def hangman(tries):
    stages = ["""
               -----
              |     |
              |     o
              |    /|\\
              |     |
              |    / \\
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
               -----
              |     |
              |     o
              |    /|\\
              |     |
              |    /
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
               -----
              |     |
              |     o
              |    /|\\
              |     |
              |    
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
               -----
              |     |
              |     o
              |    /|
              |     |
              |    
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
               -----
              |     |
              |     o
              |     |
              |     |
              |    
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
               -----
              |     |
              |     o
              |    
              |    
              |    
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
               -----
              |     |
              |   
              |    
              |   
              | 
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """ 
               -----
              |     
              |   
              |    
              |   
              | 
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
        \n
              |    
              |   
              |    
              |   
              | 
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """,
              """
        \n     
        \n        
        \n         
        \n          
        \n         
        \n       
        |==|==|
        | =|= |__________
        | = = = = = = = =|
        |________________|
              """
              ]
    return stages[tries]


def main():
    print(
        "\n██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗"
        "\n██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║"
        "\n███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║"
        "\n██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║"
        "\n██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║"
        "\n╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")
    input(
            "\n         ╋╋╋╋╋╋┏━┳━┓╋╋╋╋╋┏┓╋╋╋╋╋┏┓╋╋╋┏━┳┓╋╋╋╋╋┏┓"
            "\n         ┏━┳┳┳━┫━┫━┫┏━┳━┳┫┗┳━┳┳┓┃┗┳━┓┃━┫┗┳━┓┏┳┫┗┓"
            "\n         ┃╋┃┏┫┻╋━┣━┃┃┻┫┃┃┃┏┫┻┫┏┛┃┏┫╋┃┣━┃┏┫╋┗┫┏┫┏┫"
            "\n         ┃┏┻┛┗━┻━┻━┛┗━┻┻━┻━┻━┻┛╋┗━┻━┛┗━┻━┻━━┻┛┗━┛"
            "\n         ┗┛")
    print('Welcome to Hangman \nWhat is it they call you?')
    today = date.today()
    global wins
    wins = 0
    global losses
    losses = 0
    global attempts
    attempts = 0
    global nickname
    nickname = input()
    j = 1
    while j > 0:
        print("This is only the beginning you nasty little critter."
              "\nWhat do you wanna do here?"
              "\nPlay the game? Type: PLAY"
              "\nCheck the ranking? Type: RANKING"
              "\nTo exit type: EXIT")
        choice = input().upper()
        if choice == 'RANKING':
            print(f"{nickname}, this is the ranking board for Hangman.")
            try:
                leaderboard = open("leaderboard.txt", 'a')
                leaderboard.write("\n" + nickname + "---" + str(today) + "\nNumber of attempts:"
                                  + str(attempts) + "\nNumber of wins:"
                                  + str(wins) + "\nNumber of losses:" + str(losses) + "\n")
                leaderboard.close()
                show = open("leaderboard.txt", 'r')
                xx = show.readline()
                while (xx != ''):
                    print(xx, end="")
                    xx = show.readline()
                show.close()
            except I0Error:
                print("Something went wrong, sorry luv!")
            print("Press ENTER to go back to main menu ")
            while input().upper == "":
                j = 1
            continue
            j -= 1
        elif choice == 'PLAY':
            secret = secret_word()
            gameplay(secret)
            attempts += 1
            j -= 1
            while input("Would you like to exit? (YES/NO) ").upper() == "NO":
                h = 1
                while h > 0:
                    print("To play again type: PLAY"
                          "\nTo check the ranking type: RANKING"
                          "\nTo exit type: EXIT")
                    decision = input().upper()
                    if decision == "PLAY":
                        secret = secret_word()
                        gameplay(secret)
                        attempts += 1
                        h -= 1
                    elif decision == "RANKING":
                        print(f"{nickname}, this is the ranking board for Hangman.")
                        try:
                            leaderboard = open("leaderboard.txt", 'a')
                            leaderboard.write("\n" + nickname + "---" + str(today) + "\nNumber of attempts:"
                                              + str(attempts) + "\nNumber of wins:"
                                              + str(wins) + "\nNumber of losses:" + str(losses) + "\n")
                            leaderboard.close()
                            show = open("leaderboard.txt", 'r')
                            xx = show.readline()
                            while (xx != ''):
                                print(xx, end="")
                                xx = show.readline()
                            show.close()
                        except I0Error:
                            print("Something went wrong, sorry luv!")
                        print("Press ENTER to go back to main menu ")
                        while input().upper == "":
                            h = 1
                        continue
                        h -= 1
                    elif decision == "EXIT":
                        exit()
                    else:
                        print("Not funny dude.")
        elif choice == 'EXIT':
            exit()
        else:
            print(f'Hey, {nickname}, did your Mother drop you much as a babe? ')


if __name__ == "__main__":
    main()
