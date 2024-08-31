from random import randint


choice_pc = randint(1, 101) # PC choice for the entire game.
#print(choice_pc)

def game():
    """ Guessing game with numbers from 1-100.
     The PC has a random selection and the user chooses himself"""
    user_choice = input("Enter a number between 1 and 100: ") # User's choice for one turn
    if user_choice.isdigit(): # checking if the input from the user is really a number
        user_choice = int(user_choice) # conversion of the data type from STR to INT by the user
        if user_choice in range(0, 101): # Checking if a number is in the range from 1-100
            if user_choice < choice_pc:
                print("Too small!")
                return game()
            elif user_choice > choice_pc:
                print("Too big!")
                return game()
            else:
                return ("You win")
        else:
            print("Your number is outside the range 1-100!")
            return game()
    else:
        print("It's not a number!")
        return game()



print(game())




"""
Napište jednoduchou hru na hádání čísel.
Počítač musí vylosovat číslo v rozsahu 1 - 100. Pak by měl:
1.- Zeptejte se: "Hádej číslo: " a načtěte číslo z klávesnice.
2.- Zkontrolujte, zda se skutečně jedná o číslo, a v případě chyby zobrazte zprávu "Není to číslo!" a poté se vraťte k bodu 1.
3.- Pokud je číslo zadané uživatelem menší než nakreslené číslo, zobrazte zprávu "Příliš malé!" a vraťte se do bodu 1.
4.- Pokud je číslo zadané uživatelem větší než vylosované číslo, zobrazte zprávu "Příliš velké!" a vraťte se do bodu 1.
5.- Pokud se číslo zadané uživatelem rovná vylosovanému číslu, zobrazí se zpráva "Vyhrál jsi!" a program se ukončí.
"""