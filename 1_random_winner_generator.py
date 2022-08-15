print("Hello, this is a random winner generator.")
participants = int(input("Please enter the number of participants: "))
winners = int(input("lease indicate the number of winners: "))
print("We know that we have", participants, "participants, and there will be", winners, "winners.")

import random

for i in range(winners):
  i += 1
  winners = random.randint(1, participants)
  print(i, "winner under the number -", winners)
