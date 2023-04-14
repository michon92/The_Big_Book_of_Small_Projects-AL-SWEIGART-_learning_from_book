"""
Logiczna gra, w której na podstawie wskazówek,
musisz odgadnąć trzycyfrową liczbę.
Żadna cyfra w liczbie się nie powtarza
"""
import random

NUM_DIGITS = 3  # liczba trzycyfrowa do odgadnięcia
MAX_GUESES = 10  # liczba prób, jakie masz do odgadnięcia


def main():
    print("Bajgle, logiczna gra na dedukcję.\n\
        Typuję trzycyfrową liczbę, żadna cyfra nie może się powtórzyć.\n\
          \tGdy mówię:      Oznacza to:\n\
          \tPIKO        Jedna cyfra jest poprawna, ale jest w złym miejscu;\n\
          \tFERMI       Jedna cyfra jest poprawna i jest w odpowiednim miejscu\
          \n\tBAJGLE      Żadna cyfra nie jest poprawna\n".format(NUM_DIGITS))

    while True:  # Pętla głowna
        secretNum = getSecretNum()  # Ta zmienna przechowuj liczbę,\
        print(secretNum)
        # którą gracz musi odgadnąć
        print("Mam na myśli liczbę.")
        print("Masz {} prób, by odgadnąć jaka to liczba".format(MAX_GUESES))

        numGuesses = 1  # pierwsza próba gracza
        while numGuesses <= MAX_GUESES:
            guess = ''
            #  Wykonywanie pętli do czasu aż gracz nie poda poprawnego formatu
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Próba #{}: ".format(numGuesses))
                guess = input('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

        if guess == secretNum:
            break  # Podana liczba jest poprawna, kończymy pętlę
        if numGuesses > MAX_GUESES:
            print("Wykorzystałeś wszystkei próby")
            print("\tPrawidłowa odpowiedź to: {}.".format(secretNum))

        # Zapytanie, czy gramy ponownie?
        decision = input("Grasz ponownie?, t - tak, n - nie: ").upper()
        if decision != 'T':
            break
    print("Dziękuję pięknie za grę")


def getSecretNum():
    """Zwraca liczbę loswą złożoną z cyfr 0-9 - wartość NUM_DIGITS"""
    numbers = list('0123456789')
    random.shuffle(numbers)  # shuffle - ustaw je w losowej kolejności xD

    # Dodaj kolejne cyfry do tajemnej cyfry
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Zwraca podpowiedź lub info o wygranej"""
    if guess == secretNum:
        return 'Udało się! Brawo! Bellisimo xD!'
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # poprawna cyfra w opdowienim miejscu
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Poprawca cyfra w złym mijscu
            clues.append('Piko')
    if len(clues) == 0:
        return 'BAJGLE'  # Brak poprawnych cyfr
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()