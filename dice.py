
import random   #   mod for generating random numbers

def diceroll(faces, dices=1):   #parameter faces is the number of sides to the dice
    """Simulate rolling multiple dice with the given number of faces."""
    rolls = [random.randint(1, faces) for _ in range(dices)]
    #  generates a random number between 1 & faces
    return rolls   #  returns list of results
