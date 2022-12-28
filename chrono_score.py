import random
import itertools
import pprint

from answers import answers, olivia_guess

# TODO - we have to convert from the list of hist events to numbers
# TODO - double points for exact correct list?

"""
Given a "guess list", or a list of events, and an answer dictionary mapping
the events to their historical year, return the score by looking at each pair
weighted by the difference in year.
"""
def weighted_pairwise_score(guess_list, answer_dict):
  weighted_score = 0
  for i, g1 in enumerate(guess_list):
    for j, g2 in enumerate(guess_list[i+1:]):
      # Compare the pair in the guess list
      # Get the year of each event from the answer dict, and find the difference
      # Take the max of 0 with that difference because if the difference is neg
      # then they are in the correct order and we don't give points. But if
      # the diff is pos, then they are in the wrong order, and we give points
      # according to how far apart they are.
      weighted_score += max(0, answer_dict[g1] - answer_dict[g2])
  return weighted_score

"""
Given a score and an answer dictionary mapping the events to their historical
year, normalize the score so that more points = more good.
"""
def normalize(score, answer_dict):
  # find the max
  l = list(answer_dict.keys())
  l.reverse()
  max_score = weighted_pairwise_score(l, answer_dict)
  print(max_score)

  normalized = (max_score - score) / max_score
  return round(normalized * 50)


def swap_position(l, i, j):
  tmp = l[i]
  l[i] = l[j]
  l[j] = tmp


def score(guess_list, answer_dict):
  print(guess_list)
  raw_score = weighted_pairwise_score(guess_list, answer_dict)
  normalized_score = normalize(raw_score, answer_dict)
  print(f"Raw score: {raw_score}")
  print(f"Nor score: {normalized_score}")
  return normalized_score


if __name__ == "__main__":
  score(olivia_guess, answers)


  # l = list(answers.keys())
  # print(l)
  # score(l, answers)

  # # l.reverse()
  # # score(l, answers)

  # # l.reverse()  # reverse it back

  # for i in range(30):
  #   r = random.randint(0, 28)
  #   swap_position(l, r, r+1)
  #   score(l, answers)
