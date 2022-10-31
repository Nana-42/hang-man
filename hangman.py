print("Welcome to hangman")
word = input("Enter a word to guess: ")

counter = False
for n in range(len(word)):
    new = '_'
    print(new, end=' ')

guess = input('\nEnter a character: ')

while(counter == False):
    for n in word:
        if(guess == n):
            print("You have guessed", n)
            gues
            word = word.replace(n, '')
            for i in range(len(word)):
                print(new, end=' ')
        else:
            print("False! Enter aother letter")
            counter = True
    print("Hello world")