import random
import itertools
import pprint
import math

from answers import answers, olivia_guess

"""
Given a "guess list", or a list of events, and an answer dictionary mapping
the events to their historical year, return the score by looking at each pair
weighted by the difference in year.
"""
def weighted_pairwise_score(guess_list, answer_dict):
  weighted_score = 0

  # Iterate through the guess list one by one
  for i, g1 in enumerate(guess_list):

    # For each item in the guess list, iterate through all following items
    # in the list, so that we can compare all pairs.
    for j, g2 in enumerate(guess_list[i+1:]):
      # Get both events' years from the answer dict, and find the difference.
      # Take the max of 0 with that diff, because if the diff is negative
      # then they are in the correct order, and we give 0 points; but if the
      # diff is positive, then they are in the wrong order and we assign points
      # depending on how far off in time the events are.
      # This step is pre-normalization, so points are bad!
      weighted_score += max(0, answer_dict[g1] - answer_dict[g2])

  # Return the weighted score with a curve. This makes answers at the top of the
  # possible range farther apart so we see more differentiation in final scores.
  return math.pow(weighted_score * 3 + 1, 1/3) - 1

"""
Given a raw score and an answer dictionary mapping the events to their years,
normalize the score so that points are good.
"""
def normalize(score, answer_dict):
  # find the max possible score
  l = list(answer_dict.keys())
  l.reverse()
  max_score = weighted_pairwise_score(l, answer_dict)

  # normalize the score into a decimal between 0 and 1
  normalized = (max_score - score) / max_score

  # return the normalized score out of 50
  return normalized * 50


"""
Given a "guess list", or a list of events, and an answer dictionary mapping
the events to their historical year, return the normalized score plus bonus
if applicable.
"""
def score(guess_list, answer_dict):
  print(guess_list)
  raw_score = weighted_pairwise_score(guess_list, answer_dict)
  normalized_score = normalize(raw_score, answer_dict)
  print(f"Raw score: {raw_score}")
  print(f"Normalized score: {normalized_score}")
  if guess_list == list(answer_dict.keys()):
    normalized_score += 25
    print(f"Score with bonus: {normalized_score}")
  print("\n")
  return normalized_score


if __name__ == "__main__":
  score(olivia_guess, answers)
