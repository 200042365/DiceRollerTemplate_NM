from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice
import random

# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "6"


def select_face_option(event):
    global dice_type
    dice_type = document.getElementById("dice-selector").value
    print(f"Selected dice type: {dice_type}")


def roll_all_dice(event):
    global dice_type
    faces = int(dice_type)
    num_dice = int(document.getElementById("num-dice").value)
    rolls = dice.diceroll(faces, num_dice)
    roll_history = document.getElementById("roll-history")
    roll_history.innerHTML += f"<p> The {faces} faced-dice was rolled {num_dice}x: {', '.join(map(str, rolls))}</p>"

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = "would you like to roll again?"

