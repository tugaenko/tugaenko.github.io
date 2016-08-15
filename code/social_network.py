# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# # Example string input. Use it to test your code.

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# {'Freda': {
# 		'connections': ['Olive', ' John', ' Debra'], 
# 		'games': ['Starfleet Commander', ' Ninja Hamsters', ' Seahorse Adventures']}, 
# 'Ollie': {
# 		'connections': ['Mercedes', ' Freda', ' Bryant'], 
# 		'games': ['Call of Arms', ' Dwarves and Swords', ' The Movie: The Game']}, 
# 'Debra': {
# 	'connections': ['Walter', ' Levi', ' Jennie', ' Robin'], 
# 	'games': ['Seven Schemers', ' Pirates in Java Island', ' Dwarves and Swords']}, 
# 'Olive': {
# 	'connections': ['John', ' Ollie'], 
# 	'games': ['The Legend of Corgi', ' Starfleet Commander']}, 
# 'Levi': {
# 	'connections': ['Ollie', ' John', ' Walter'], 
# 	'games': ['The Legend of Corgi', ' Seven Schemers', ' City Comptroller: The Fiscal Dilemma']}, 
# 'Jennie': {
# 	'connections': ['Levi', ' John', ' Freda', ' Robin'], 
# 	'games': ['Super Mushroom Man', ' Dinosaur Diner', ' Call of Arms']}, 
# 'Mercedes': {
# 	'connections': ['Walter', ' Robin', ' Bryant'], 
# 	'games': ['The Legend of Corgi', ' Pirates in Java Island', ' Seahorse Adventures']}, 
# 'John':{
# 	'connections': ['Bryant', ' Debra', ' Walter'], 
# 	'games': ['The Movie: The Game', ' The Legend of Corgi', ' Dinosaur Diner']}, 
# 'Robin': {
# 	'connections': ['Ollie'], 
# 	'games': ['Call of Arms', ' Dwarves and Swords']}, 
# 'Bryant': {
# 	'connections':['Olive', ' Ollie', ' Freda', ' Mercedes'], 
# 	'games': ['City Comptroller: The Fiscal Dilemma', ' Super Mushroom Man']}, 
# 'Walter': {
# 	'connections': ['John', ' Levi', ' Bryant'], 
# 	'games': ['Seahorse Adventures', ' Ninja Hamsters', ' Super Mushroom Man']}}

# {'Freda': ['Starfleet Commander', ' Ninja Hamsters', ' Seahorse Adventures'], 
# 'Ollie': ['Call of Arms', ' Dwarves and Swords', ' The Movie: The Game'], 
# 'Debra': ['Seven Schemers', ' Pirates in Java Island', ' Dwarves and Swords'], 
#  'Olive': ['The Legend of Corgi', ' Starfleet Commander'], 
# 'Levi': ['The Legend of Corgi', ' Seven Schemers', ' City Comptroller: The Fiscal Dilemma'], 
#  'Jennie': ['SuperMushroom Man', ' Dinosaur Diner', ' Call of Arms'], 
# 'Mercedes': ['The Legend ofCorgi', ' Pirates in Java Island', ' Seahorse Adventures'], 
# 'John': ['The Movie: The Game', ' The Legend of Corgi', ' Dinosaur Diner'], 
#  'Robin': ['Call of Arms', ' Dwarves and Swords'], 
# 'Bryant': ['City Comptroller: The Fiscal Dilemma', ' Super Mushroom Man'], 
# 'Walter': ['Seahorse Adventures', ' Ninja Hamsters', ' Super Mushroom Man']}

# print example_input
# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
import re
def create_data_structure(string_input):
	network = {}
	if string_input == "":
		return network	

	gamers = re.findall(r'(\w+)\slikes\sto\splay\s([\w\s,:]+)\.', string_input )

	for user_games_tuple in gamers:
		user = user_games_tuple[0]
		if user not in network:
			network[user] = {"connections":[], "games":[]}
		network[user]["games"] = user_games_tuple[1].split(", ")

	connections = re.findall(r'(\w+)\sis\sconnected\sto\s([\w\s,]+)\.', string_input )
	for connection_tuple in connections:
		user = connection_tuple[0]
		if user not in network:
			network[user] = {"connections":[], "games":[]}
		network[user]["connections"] = connection_tuple[1].split(", ")
	return network


# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
	if user in network:
		return network[user]["connections"]
	return None
# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
	if user in network:
		return network[user]["games"]
	return None
# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
	if user_A not in network or user_B not in network:
		return False
	if user_B not in network[user_A]["connections"]:
		network[user_A]["connections"].append(user_B)
	return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
	if user not in network:
		network[user] = {"connections":[], "games":[]}
		network[user]["games"] = games
	return network
	 
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
	if user not in network:
		return None
	sec_friends = []	
	for friend in network[user]["connections"]:
		sec_friends = sec_friends + network[friend]["connections"]
	return list(set(sec_friends))

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
	if user_A not in network or user_B not in network:
		return False
	return len( set(network[user_A]["connections"]).intersection(set(network[user_B]["connections"]) ))


# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def get_path(parents, current_user, used):
	# print "get path / current user : ", current_user
	# print "get path / parents : ", parents
	path = [current_user]
	while current_user != used[0]:
		path.append(parents[current_user])
		current_user = parents[current_user]
	return path[::-1]

def find_path_to_friend(network, user_A, user_B, stack = None, parents = None, used = None):
	# print "parents: ",parents
	if user_A not in network or user_B not in network:
		return None
	if stack == None:
		stack = []
	if parents == None:
		parents = {}
	if used == None:
		used = []
	current_user = user_A
	current_users_hub = network[current_user]["connections"]

	if user_B in current_users_hub:
		parents[user_B] = current_user
		current_user = user_B
		if not used:
			used = [user_A]
		stack = []
		return get_path(parents, current_user, used)
	else:
		for user in current_users_hub:
			if ( user != current_user ) and ( user not in used ) and ( user not in stack ):
				stack.append(user)
				parents[user] = current_user
		used.append(current_user)
	if not stack:
		return None
	current_user = stack.pop()

	if current_user:
		return find_path_to_friend(network, current_user, user_B, stack, parents, used)

	return None

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.
def add_game(network, user, game):
	if user not in network :
		return False
	if game not in network[user]["games"]:
		network[user]["games"].append(game)
	return network
# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

net = create_data_structure(example_input)
# print net

# print get_connections(net, "Debra")
# print get_connections(net, "Mercedes")
# print get_games_liked(net, "John")
# print add_connection(net, "John", "Freda")
##print add_connection(net, "Mercedes", "Freda")
# print add_new_user(net, "Debra", []) 
# print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
# print get_secondary_connections(net, "Mercedes")
# print count_common_connections(net, "Mercedes", "John")
print find_path_to_friend(net, "John", "Ollie")
print find_path_to_friend(net, "John", "Bryant")
# print find_path_to_friend(net, "John", "Ollie")
# print find_path_to_friend(net, "John", "Ollie")
# print find_path_to_friend(net, "John", "Ollie")
# print find_path_to_friend(net, "John", "Ollie")
# print find_path_to_friend(net, "John", "Ollie")
# print find_path_to_friend(net, "John", "Ollie")
# print find_path_to_friend(net, "John", "Ollie")
# print find_path_to_friend(net, "John", "Olive")
# print find_path_to_friend(net, "John", "Mercedes")
# print find_path_to_friend(net, "Olive", "Ollie")
# print find_path_to_friend(net, "Debra", "Ollie")
# print add_game(net, "Freda", "Tetris OOOOOO")
