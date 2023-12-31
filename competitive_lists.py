import csv

def score(team_lists):
	"""
	For each category, the trivia teams get one point for every item they
	write down, and one additional point per item that no other team writes.
	"""
	team_scores = {}
	item_counts = {}

	# Iterate through all the items submitted by all teams and put them
	# in a hashmap where the key is the item name and the value is the
	# number of times it appears in all teams' lists
	for team in team_lists.keys():
		for item in team_lists[team]:
			if item in item_counts.keys():
				item_counts[item] += 1
			else:
				item_counts[item] = 1

	# Iterate again through all the teams
	for team in team_lists.keys():
		# For every team, they get one point per item in the list
		team_scores[team] = len(team_lists[team])
		# Then iterate through the items again to check if they are unique
		for item in team_lists[team]:
			if item_counts[item] == 1:  # If the count in the hashmap created above is 1, then it's unique
				team_scores[team] += 1  # and the team gets an extra point

	return team_scores

def parse_csv(csv_name):
	"""
	accepts a pointer to a CSV file, where each comma-separated line
	represents one team's list of items. the first token in every line
	should be a team name and the rest of the tokens are the team's items
	"""
	team_lists = {}
	with open(csv_name) as csvfile:
	    reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
	    for row in reader:
	        team_name = row.pop(0)
	        team_lists[team_name] = row

	return team_lists

def pretty_print_scores(team_scores):
	for team in team_scores.keys():
		print(f"{team} gets {team_scores[team]} points")

if __name__ == "__main__":
	team_lists = parse_csv('fruit_list_example.csv')
	team_scores = score(team_lists)
	pretty_print_scores(team_scores)
