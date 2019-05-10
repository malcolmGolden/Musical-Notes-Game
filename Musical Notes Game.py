# main code for Musical Notes Game

import random
from itertools import cycle
musical_notes = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")

def random_note():
    note = random.choice(musical_notes)
    print(note)
    user_input = input("What note comes after this note? :")

    note_cycle = cycle(musical_notes)
    next_note = next(note_cycle)
    print(next_note)


    if user_input == note:
            print("Correct!")
    else:
        print("Try Again..")

random_note()