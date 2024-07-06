# Random Word kütüphanesinden rastgele kelime alıyoruz.
from random_word import RandomWords
r = RandomWords()
rand_word = r.get_random_word()
# Aldığımız kelimenin tek kelime olmasını sağlıyoruz.
while " " in rand_word:  # Check if there are spaces in the word
    rand_word = r.get_random_word()
# Rasgele kelimemizi array yapıyoruz
array_rand_word = list(rand_word)
# Kelimemizdeki harf kadar tire oluşturuyoruz.
guessed_word = ["_"] * len(array_rand_word)
print(guessed_word)

# Yapılan deneme sayısı.
current_attempts = 0
# Yapılacak maksimum deneme sayısı.
max_attempts = 10

# Yaptığımız deneme maksimum denemeden küçük olduğu sürece
while current_attempts < max_attempts:
    # Girdi al
    x = input("Enter a character: ")
    # Found bool'u false başlıyor.
    found = False
    for i in range(len(array_rand_word)):
        # Tahmin ettiğimiz harf varsa found bool'u true oluyor.
        if x == array_rand_word[i]:
            guessed_word[i] = x
            found = True
    # found bool'u true ise "correct" yazdır.
    if found:
        print("Correct!")
    # found bool'u false ise "karakter bulunamadı" yazdır ve deneme sayısını bir arttır.
    else:
        print("Character not found in the word.")
        current_attempts += 1

    print("Guessed word so far:", " ".join(guessed_word))

    # guessed_word array'inde tire kalmadı ise doğru buldunuz.
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", "".join(guessed_word))
        break

if "_" in guessed_word:
    print("Out of attempts. The word was:", "".join(array_rand_word))
