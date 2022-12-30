import random
import itertools
import pprint
import math

from answers import answers, olivia_guess

# TODO - double points for exact correct list?

"""
Given a "guess list", or a list of events, and an answer dictionary mapping
the events to their historical year, return the score by looking at each pair
weighted by the difference in year.
"""
def pairwise_score(guess_list, answer_dict):
  mismatched_pairs = 0
  for i, g1 in enumerate(guess_list):
    for j, g2 in enumerate(guess_list[i+1:]):
      g1_date = answer_dict[g1]
      g2_date = answer_dict[g2]
      if g1_date > g2_date:
        mismatched_pairs += 1
  print(f"Mismatched pairs: {mismatched_pairs}")
  return math.sqrt(mismatched_pairs)

"""
Given a score and an answer dictionary mapping the events to their historical
year, normalize the score so that more points = more good.
"""
def normalize(score, answer_dict):
  # find the max
  l = list(answer_dict.keys())
  l.reverse()
  max_score = pairwise_score(l, answer_dict)
  normalized = (max_score - score) / max_score
  return round(normalized * 50)


def swap_position(l, i, j):
  tmp = l[i]
  l[i] = l[j]
  l[j] = tmp


def score(guess_list, answer_dict):
  # print(guess_list)
  raw_score = pairwise_score(guess_list, answer_dict)
  normalized_score = normalize(raw_score, answer_dict)
  print(f"Raw score: {raw_score}")
  print(f"Nor score: {normalized_score}")
  if guess_list == list(answer_dict.keys()):
    print(f"Bon score: {25}")
    normalized_score += 25
    print(f"Tot score: {normalized_score}")
  print("\n")
  return normalized_score


if __name__ == "__main__":
  score(olivia_guess, answers)

  l = list(answers.keys())
  score(l, answers)

  for i in range(100):
    r = random.randint(0, 28)
    swap_position(l, r, r+1)
    score(l, answers)
