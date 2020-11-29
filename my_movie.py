import random

amount = ["Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine"]

adjective = ["blue",
             "wild",
             "dark",
             "shiny",
             "strange"]

verb = ["sing",
          "dance",
          "slep",
          "look",
          "drive"]

people = ["Jim-Bob",
          "that person you forgot to text back",
          "Glenn Hubbard",
          "Samuel L. Jackson",
          "Bill Tell"]

object = ["Churches",
          "Candels",
          "Mustards",
          "Planes",
          "Rocks"]

random_amount = random.choice(amount)
random_adjective = random.choice(adjective)
random_people = random.choice(people)
random_object = random.choice(object)
random_verb = random.choice(verb)

print(f"My favorite movie is called:  {random_amount} {random_adjective} {random_object} {random_verb} with {random_people}")
