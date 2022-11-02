print("Welcome to Hangman")

step1 = ("player 1 will choose a word to print")
step2 = ("player 2 will try to guess the word")
step3 =("You have unlimited guesses...but try to finish it as early as possible")
step4 = ("Good Luck")
print(step1+"\n"+step2+"\n"+step3+"\n"+step4+"\n")

user1_word = input("enter a word: ")
print('''





















''')

man0 = (r'''
------------------
|        |
|        |
|        |
|        
|       
|       
|
|
|
|_____________''')

man1 =(r'''
------------------
|        |
|        |
|        |
|        O
|       
|       
|
|
|
|_____________''')

man2 = (r'''
------------------
|        |
|        |
|        |
|        O
|        |
|        |
|        |
|
|
|_____________''')

man3 = (r'''
------------------
|        |
|        |
|        |
|        O
|       /|
|      / |
|        |
|
|
|_____________''')

man4 = (r'''
------------------
|        |
|        |
|        |
|        O
|       /|\
|      / | \
|        |
|
|
|_____________''')

man5 = (r'''
------------------
|        |
|        |
|        |
|        O
|       /|\
|      / | \
|        |
|       /
|      /
|_____________''')

man6 = (r'''
------------------
|        |
|        |
|        |
|        O
|       /|\
|      / | \
|        |
|       / \
|      /   \
|_____________''')
man = 0
blanks = list("*"*len(user1_word))
print(man0)

list = []
guess = str
while guess != user1_word:
    print("".join(blanks))
    guess_word = input("Guess a letter or a word: ")
    if len(guess_word) != 1:
        if guess_word == user1_word:
            break
        else:
            print("You guessed the wrong word")
            man +=1
            list.append(guess_word)
            print("wrong guess: "+", ".join(list))
    if len(guess_word) == 1:
        miss = True
        print("list of wrong guess: "+", ".join(list))
        for i,c in enumerate(user1_word):
            if c == guess_word:
                blanks[i] = guess_word
                miss = False
        if miss == True:
            guess_word != user1_word
            print("You guessed the wrong letter")
            man +=1
            list.append(guess_word)
            print("wrong guess: "+", ".join(list))
    if "".join(blanks) == user1_word:
        print(user1_word)
        break
    if man == 0:
        print(man0)
    elif man == 1:
        print(man1)
    elif man == 2:
        print(man2)
    elif man == 3:
        print(man3)
    elif man == 4:
        print(man4)
    elif man == 5:
        print(man5)
    elif man >= 6:
        print(man6)
    
print("YOU WON!!!")
        
    
            
        
        
    
            
        