# Heads or Tails

import random

random_int = random.random()
heads_or_tails = int(random_int * 2)

if heads_or_tails == 0:
    print("Tails")
else:
    print("Heads")