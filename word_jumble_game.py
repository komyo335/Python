import random
def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)
def play_jumble_word():
    words = ['computer','banana','nvidia','spacex','google','pineapple']
    word_to_guess = random.choice(words)
    jumbled_word = jumble_word(word_to_guess)

    print("Welcome from Jumble Game")
    print("Guess a word and fill the text")
    print("Jumbled word", jumbled_word)

    guess = input("Guess a words: ").lower()

    while guess != word_to_guess :
       print("Incorrect guess. Try again ! ")
       guess = input("Your Guess :").lower()
      
    print("Congratulations! You've  guessed the words correctly")

play_jumble_word()