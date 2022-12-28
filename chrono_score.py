import random
import itertools
import pprint

# TODO - fine tune so that the scores make sense.
# TODO - higher is worse - we need to normalize this
# TODO - we have to convert from the list of hist events to numbers


# """
# Given a "guess list", or a list of n integers from 1 to n with no repeats,
# return the score based on the distance of each element from its correct
# position in the list.
# """
# def dist_score(guess_list):
#   total_dist = 0
#   for i, guess in enumerate(guess_list):
#     distance = abs(guess - 1 - i)  # because guess isn't 0-indexed
#     total_dist += distance
#   return total_dist

"""
Given a "guess list", or a list of n integers from 1 to n with no repeats,
return the score based on looking at each pair and determining if they are
in the correct order or not.
"""
def pairwise_score(guess_list):
  mismatched_pairs = 0
  for i, g1 in enumerate(guess_list):
    for j, g2 in enumerate(guess_list[i+1:]):
      if g1 > g2:
        mismatched_pairs += 1
  return mismatched_pairs

# """
# Given a "guess list", or a list of n integers from 1 to n with no repeats,
# return the score based on whether neighbors are close to one another.
# For each item in the list, take its 2 neighbors on either side in the correct
# list (for 2, this would be 1 and 3), and if the guess list doesn't place
# those neighbors within 2 steps of the item, the score goes up.
# """
# def close_neighbors_score(guess_list):
#   non_close_neighbors = 0
#   for i, guess in guess_list:
#     real_neighbors = [guess - 1, guess + 1]

#     guess_neighbors_min_index = max(i - 2, 0)
#     guess_neighbors_max_index = min(i + 3, len(guess_list)  # 3 because of 0-indexing?
#     guess_neighbors = guess_list[guess_neighbors_min_index:guess_neighbors_max_index]

#     for n in real_neighbors:
#       if n <= 0 or n > len(guess_list):
#         continue
#       if n not in guess_neighbors:
#         non_close_neighbors += 1

#   return non_close_neighbors
#   # TODO - test this code
#   # TODO - fix for errors


# """
# Given a "guess list", or a list of n integers from 1 to n with no repeats,
# combines the two techniques above (dist and pairwise) to return an
# overall score for the list.
# """
def score(guess_list):
  print(guess_list)
  score = pairwise_score(guess_list)# + dist_score(guess_list)
  print(score)
  return score

# def normalize(score, len):
#   worst_list = list(range(1, len + 1)).reverse()
#   max_score = score(worst_list)
#   normalized_score = 

"""
Given a list l and two indices i and j, swaps the element at index i with the
element at index j.
"""
def swap_position(l, i, j):
  tmp = l[i]
  l[i] = l[j]
  l[j] = tmp

def test_30_lists():
  # Test the list in order. Score should be 0
  l = list(range(1,31))
  score(l)

  # Test the list backwards. Should be the maximum score(?)
  l.reverse()
  score(l)

  # Test random lists
  for i in range(10):
    random.shuffle(l)
    score(l)

  l = list(range(1,31))
  swap_position(l, 4, 5)
  score(l)
  swap_position(l, 25, 26)
  score(l)

def test_5_lists():
  list_by_score = {}
  for l in list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])):
    s = pairwise_score(l)
    if not list_by_score.get(s):
      list_by_score[s] = []
    list_by_score[s].append(l)
  pp = pprint.PrettyPrinter(width=41, compact=True)
  pp.pprint(list_by_score)

if __name__ == "__main__":
  test_30_lists()
