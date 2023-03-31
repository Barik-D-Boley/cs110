import sys
import random


def readlines(filename):
    """
    Reads the file with the given filename and
    returns a list of lines in the file.
    """
    with open(filename) as f:
        return f.readlines()


def strip_newlines(lines):
    """
    Removes all the newlines (and any other extra whitespace) from a set of lines
    """
    new_lines = []
    for line in lines:
        new_lines.append(line.strip())
    return new_lines


def assign_teams(players):
    """
    players -- a list of player names (strings)

    Returns a dictionary that maps a player name to a team.
    Team assignments are randomly chosen from "Y Hackers", "Clever Cougars",
    and "We Did Nothing"
    """
    # Write code here
    pass


def do_player(assignments):
    """
    assignments -- a dictionary that maps player to team

    Asks for a player name. Then prints out the team that player is assigned to.
    The format is:
    {player} is on {team}
    If the player is not in the dictionary, then the program prints:
    Sorry, no player by that name.
    """
    # Write code here
    pass


def do_team(assignments):
    """
    assignments -- a dictionary that maps player to team

    Asks for a team. Then prints out a bulleted list of all of the players
    on that team. The format is:
    * {player
    """
    # Write code here
    pass


def do_menu(assignments):
    """
    Allows a person to enter "p" for player or "t" for team.
    Then calls a function to handle looking up a person or a team.
    """
    while True:
        response = input("Player or Team? (p/t) ")
        if response == "":
            break
        if response == "p":
            do_player(assignments)
        elif response == "t":
            do_team(assignments)
        else:
            print("Invalid choice, try again.")


def main(infile):
    """
    Reads player names from a file, then sets up a dictionary that assigns
    each player to a team. Finally, runs a menu system to allow
    a person to lookup a player's team or get a list of all the players
    on a given team.
    """
    players = readlines(infile)
    players = strip_newlines(players)
    assignments = assign_teams(players)
    do_menu(assignments)



if __name__ == '__main__':
    main(sys.argv[1])