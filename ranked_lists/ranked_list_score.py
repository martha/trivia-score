import random
import itertools
import pprint
import math

from vitamin_c_example import vitamin_c_mg_per_100g, example_guess

"""
Given a "guess list", or a list of items, and an answer dictionary mapping
the items to their rank, return the score by looking at each pair
weighted by the difference in rank.

Ranks can be e.g. year, height, cost, etc.
"""
def weighted_pairwise_score(guess_list, answer_dict, p = 1/2, noisy = False):
  weighted_score = 0
  num_bad_pairs = 0  # This is not used except for logging

  # Iterate through the guess list one by one
  for i, g1 in enumerate(guess_list):

    # For each item in the guess list, iterate through all following items
    # in the list, so that we can compare all pairs.
    for j, g2 in enumerate(guess_list[i+1:]):

      # Get both items' ranks from the answer dict, and find the difference.
      # Take the max of 0 with that diff, because if the diff is negative
      # then they are in the correct order, and we give 0 points; but if the
      # diff is positive, then they are in the wrong order and we assign points
      # depending on how far apart the ranks are.
      # This step is pre-normalization, so points are bad!
      diff = max(0, answer_dict[g1] - answer_dict[g2])

      # Take the square root to attenuate the penalty for really big mistakes
      sqrt_diff = math.pow(diff, p)

      weighted_score += sqrt_diff
      if answer_dict[g2] < answer_dict[g1]:
        num_bad_pairs += 1

  if noisy:
    print(f"Number of bad pairs: {num_bad_pairs}")

  return weighted_score

"""
Given a raw score, an item dictionary mapping the items to their ranks,
and a max score for the round, normalize the score -- points are now good.
"""
def normalize(score, answer_dict, p = 1/2, q = 1/2, normalized_max_score = 20):
  # first find the worst possible score by taking the correct order and reversing it
  order = list(dict(sorted(answer_dict.items(), key=lambda item: item[1])).keys())
  order.reverse()
  worst_score = weighted_pairwise_score(order, answer_dict, p)
  print(f"Worst possible score: {worst_score}")

  # Divide this score by the worst possible score to get a number between 0 and 1
  zo = score / worst_score

  # Taking the sqrt here applies a curve, which makes answers at the top
  # of the possible range farther apart so we see more differentiation in final scores.
  # The power is an argument passed so it can be customized to different lists.
  sqrt_zo = math.pow(zo, q)

  # Finally, return the score normalized against the desired max score for this round.
  normalized = normalized_max_score * (1 - sqrt_zo)
  return round(normalized)


"""
Given a "guess list", or an ordered list of items, an answer dictionary mapping
the items to their ranks, p and q which are params you can fiddle with for
score normalization, and an optional bonus quantity for a perfect list,
return the normalized score plus bonus if applicable.
"""
def score(guess_list, answer_dict, p = 1/2, q = 1/2, max_score = 20, bonus = 0):
  print(f"Guess list:")
  pprint.pprint(guess_list)

  raw_score = weighted_pairwise_score(guess_list, answer_dict, p, noisy = True)
  print(f"Raw score: {raw_score}")

  normalized_score = normalize(raw_score, answer_dict, p, q, max_score)
  print(f"Normalized score: {normalized_score}")

  if guess_list == list(dict(sorted(answer_dict.items(), key=lambda item: item[1])).keys()) \
      and bonus > 0:
    normalized_score += bonus
    print(f"Score with bonus: {normalized_score}")

  print("\n")
  print("\n")
  return normalized_score


def swap_position(l, i, j):
  tmp = l[i]
  l[i] = l[j]
  l[j] = tmp



if __name__ == "__main__":
  p = 1/2
  q = 1/2
  print("Example team")
  score(example_guess, vitamin_c_mg_per_100g, p, q)


