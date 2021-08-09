class Team:

    def __init__(self, name, list_of_players, coach):
        self.name = name
        self.list_of_players = list_of_players
        self.coach = coach
# add a points property into your class that starts at 0.
        self._points = 0

# Create a method add_player that takes in a string of 
# a new players'sname and adds that new player to the players list.
    def add_player(self, new_player):
        self.list_of_players.append(new_player)


# Add a method has_player that takes in a string of a player's name
#  and checks to see if they are in the players list. 
# It should return True if the player's name is in the list
#  and False otherwise.
    def has_player(self, player):
        return self.list_of_players.count(player) > 0


# Create a method, play_game that takes in wheter 
# the team has won(True) or lost(False) and 
# adds 3 to the points property for a win.
    
