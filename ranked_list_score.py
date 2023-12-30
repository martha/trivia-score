import random
import itertools
import pprint
import math

# from answers_2022 import answers, olivia_guess, frijoles_guess, festival_guess, knowers_guess
from ranked_lists_2023 import mountains, martha_lael_mountains, correct_mountains

"""
Given a "guess list", or a list of items, and an answer dictionary mapping
the items to their rank, return the score by looking at each pair
weighted by the difference in rank.

Ranks can be year of historical event, mountain height, cost in dollars, etc.
"""
def weighted_pairwise_score(guess_list, answer_dict):
  weighted_score = 0
  num_bad_pairs = 0

  # Iterate through the guess list one by one
  for i, g1 in enumerate(guess_list):

    # For each item in the guess list, iterate through all following items
    # in the list, so that we can compare all pairs.
    for j, g2 in enumerate(guess_list[i+1:]):
      # Get both items' ranks from the answer dict, and find the difference.
      # Take the max of 0 with that diff, because if the diff is negative
      # then they are in the correct order, and we give 0 points; but if the
      # diff is positive, then they are in the wrong order and we assign points
      # depending on how far off in time the events are.
      # This step is pre-normalization, so points are bad!
      weighted_score += max(0, answer_dict[g1] - answer_dict[g2])
      if answer_dict[g2] < answer_dict[g1]:
        num_bad_pairs += 1

  print(f"Number of bad pairs: {num_bad_pairs}")

  # Return the weighted score with a curve. This makes answers at the top of the
  # possible range farther apart so we see more differentiation in final scores.
  return math.pow(weighted_score * 4 + 1, 1/4) - 1

"""
Given a raw score, an item dictionary mapping the items to their ranks,
and a max score for the round,
normalize the score so that points are good.
"""
def normalize(score, answer_dict, normalized_max_score):
  # find the max possible score
  l = list(answer_dict.keys())
  l.reverse()
  max_score = weighted_pairwise_score(l, answer_dict)

  # normalize the score into a decimal between 0 and 1
  normalized = (max_score - score) / max_score

  # return the normalized score
  return normalized * normalized_max_score


"""
Given a "guess list", or an ordered list of items, an answer dictionary mapping
the items to their ranks, a max score for the round (used for normalizing),
and an optional bonus quantity for a perfect list,
return the normalized score plus bonus if applicable.
"""
def score(guess_list, answer_dict, max_score = 20, bonus = 0):
  print(guess_list)
  raw_score = weighted_pairwise_score(guess_list, answer_dict)
  normalized_score = normalize(raw_score, answer_dict, max_score)
  print(f"Raw score: {raw_score}")
  print(f"Normalized score: {normalized_score}")
  if guess_list == list(answer_dict.keys()):
    normalized_score += bonus
    print(f"Score with bonus: {normalized_score}")
  print("\n")
  return normalized_score


def swap_position(l, i, j):
  tmp = l[i]
  l[i] = l[j]
  l[j] = tmp



# TODO - need to debug

if __name__ == "__main__":
  print("mountains")
  correct_mountains.reverse()
  score(correct_mountains, mountains)

