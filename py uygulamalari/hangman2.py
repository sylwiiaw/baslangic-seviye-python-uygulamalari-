import random

words = ["kazandibi", "muhallebi", "baklava", "kadayif", "browni"]
word = random.choice(words)
guesses = ""
tries = 5

print("Hangman oyununa hoş geldiniz!")

while tries > 0:
    false = 0
    for character in word:
        if character in guesses:
            print(character, end=" ")
        else:
            print("_", end=" ")
            false += 1
    
    print("\n")

    if false == 0:
        print("Tebrikler! kelimeyi buldunuz:", word)
        break

    guess = input("Bir harf tahmin edin: ").lower()

    if guess in guesses:
        print("Bu harfi zaten tahmin ettiniz.")
    elif guess  in word:
        guesses += guess 
    else:
        guesses += guess 
        tries -= 1
        print("Yanliş tahmin! Kalan hakkiniz:", tries)

    if tries == 0:
        print("Maalesef, hakkiniz bitti. kelime:", word)
