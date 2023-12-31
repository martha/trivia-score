import random
import itertools
import pprint
import math

from ranked_lists_2023 import mountains, \
  martha_lael_mountains, correct_mountains, test_mountains, kronenberg_mountains, \
  costs, kronenberg_costs, edwards_costs, test_costs, \
  battles, edwards_battles, kronenberg_battles, test_battles \

"""
Given a "guess list", or a list of items, and an answer dictionary mapping
the items to their rank, return the score by looking at each pair
weighted by the difference in rank.

Ranks can be year of historical event, mountain height, cost in dollars, etc.
"""
def weighted_pairwise_score(guess_list, answer_dict, p = 1/2, noisy = False):
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
      # depending on how far apart the ranks are.
      # This step is pre-normalization, so points are bad!

      # Raising it to a power here applies a curve, which makes answers at the top
      # of the possible range farther apart so we see more differentiation in final scores.
      # The power is an argument passed so it can be customized to different lists.
      diff = max(0, answer_dict[g1] - answer_dict[g2])
      sdiff = math.pow(diff, p)
      weighted_score += sdiff
      if answer_dict[g2] < answer_dict[g1]:
        num_bad_pairs += 1

  if noisy:
    print(f"Number of bad pairs: {num_bad_pairs}")

  return weighted_score

"""
Given a raw score, an item dictionary mapping the items to their ranks,
and a max score for the round,
normalize the score so that points are good.
"""
def normalize(score, answer_dict, normalized_max_score):
  # find the worst possible score
  order = list(dict(sorted(answer_dict.items(), key=lambda item: item[1])).keys())
  order.reverse()
  worst_score = weighted_pairwise_score(order, answer_dict)
  print(f"Worst possible score: {worst_score}")

  # Divide this score by the worst possible score to get a number between 0 and 1
  zo = score / worst_score
  szo = math.pow(zo, 1/2)

  # Finally, return the score normalized against the desired max score for this round.
  normalized = normalized_max_score * (1 - szo)
  return normalized


"""
Given a "guess list", or an ordered list of items, an answer dictionary mapping
the items to their ranks, a max score for the round (used for normalizing),
and an optional bonus quantity for a perfect list,
return the normalized score plus bonus if applicable.
"""
def score(guess_list, answer_dict, p = 1/2, max_score = 20, bonus = 0):
  print(f"Guess list:")
  pprint.pprint(guess_list)

  raw_score = weighted_pairwise_score(guess_list, answer_dict, p, True)
  print(f"Raw score: {raw_score}")

  normalized_score = normalize(raw_score, answer_dict, max_score)
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



# TODO - need to make and document parameters p and q

if __name__ == "__main__":
  # MOUNTAINS: we liked square root (power of 1/2) which is the default param
  score(test_mountains, mountains)
  score(kronenberg_mountains, mountains)
  score(martha_lael_mountains, mountains)

  # COSTS: we like p = 2/3
  # p = 0.3
  # score(test_costs, costs, p)
  # score(kronenberg_costs, costs, p)
  # score(edwards_costs, costs, p)


  # BATTLES
  # p = 1/2
  # score(test_battles, battles, p = p)
  # score(edwards_battles, battles, p = p)
  # score(kronenberg_battles, battles, p = p)

  # finish testing with the final group



