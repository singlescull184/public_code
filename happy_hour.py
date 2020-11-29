import random

bars = ["The Hamilton",
        "1020 Bar",
        "The Heights9",
        "The Dead Poet"]

people = ["Mattan",
          "that person you forgot to text back",
          "Glenn Hubbard",
          "Samuel L. Jackson",
          "Bill Tell"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_person2 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person} and also {random_person2}?")
