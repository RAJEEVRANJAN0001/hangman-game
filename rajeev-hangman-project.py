import random
def hangman():
    lists_of_words=['handman','rajeev','world','macbook']
    word=random.choice(lists_of_words)
    turns=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=""
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word = main_word+"_ "
        if main_word == word:
            print(main_word)
            print("you have won the game")
            break


        print("guess the words",main_word)
        guess=input()

        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("entre th valid character")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("only 9 turns left")
                print("------------")
            if turns==8:
                print("only 8 turns left")
                print("------------")
                print("    O     ")
            if turns==7:
                print("only 7 turns left")
                print("------------")
                print("    O     ")
                print("    |    ")
            if turns==6:
                print("only 6 turns left")
                print("-----------")
                print("    O     ")
                print("    |     ")
                print("   /      ")
            if turns==5:
                print("only 5 turns left")
                print("-----------")
                print("    O     ")
                print("    |     ")
                print("   / \     ")
            if turns==4:
                print("only 4 turns left")
                print("----------")
                print("   \O     ")
                print("    |     ")
                print("   / \    ")
            if turns==3:
                print("only 3 turns left")
                print("-----------")
                print("   \O/     ")
                print("    |      ")
                print("   / \     ")
            if turns==2:
                print("only 2 turns left")
                print("-----------")
                print("   \O/  |  ")
                print("    |      ")
                print("   / \     ")
            if turns==1:
                print("last attempts have a nice a luck for live ")
                print("-----------")
                print("   \O/_|   ")
                print("    |      ")
                print("   / \     ")
            if turns==0:
                print("you lost it")
                print(" now you are died")
                print("-----------")
                print("    O_|   ")
                print("   /|\      ")
                print("   / \     ")
                break
name=input("please enter the name  ")
print("welcome to the game of words",name,"!")
print("---------------")
print("now try guess the word within  10 attempts")
hangman()
