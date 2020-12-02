# Luis Urena
# The purpose of this program is to track an individuals soccer season

import sys
import pickle

game_list = []

# File to store game list with statistics
filename = 'games.pk'


# This function is used to add a new game and its statistics to the game list
def add_game_stats():
    game = []
    print("How many minutes did you play?")
    game.append(int(input()))
    print("how many goals, if any, did you score?")
    game.append(int(input()))
    print("How many assists did you have?")
    game.append(int(input()))
    print("Did you receive any yellow cards? Y/N")

    # record yellow cards
    y_card = str(input())
    if y_card == 'y':
        print('Did you receive one or two yellow cards? Enter 1 or 2')
        if int(input()) == 1:
            game.append(1)
        else:
            game.append(2)
    elif y_card == 'n':
        game.append(0)
    else:
        print("Please enter either Y or N")

    # Records red card
    print("Did you receive a red card? Y/N")
    r_card = str(input())
    if r_card == 'y':
        game.append(1)
    elif r_card == 'n':
        game.append(0)
    else:
        print("Please enter either Y or N")

    game_list.append(game)
    return


# This function allows the user to revise the statistics for a game
def revise_game():
    print('Which game do you want to revise?')
    game_revise = int(input())
    print("You are revising game", game_revise)

    print('Which stat do you want to revise?\n'
          '1. minutes\n'
          '2. goals\n'
          '3. assists\n'
          '4. yellow cards\n'
          '5. red cards\n')
    stat_to_revise = int(input())
    if stat_to_revise == 1:
        print('how many minutes did you play?')
        game_list[game_revise - 1][0] = int(input())
    if stat_to_revise == 2:
        print('How many goals did you score?')
        game_list[game_revise - 1][1] = int(input())
    if stat_to_revise == 3:
        print('How many goals did you assist?')
        game_list[game_revise - 1][2] = int(input())
    if stat_to_revise == 4:
        print('How many yellow cards did you get? ')
        game_list[game_revise - 1][3] = int(input())
    if stat_to_revise == 5:
        print('How many red cards did you get')
        game_list[game_revise - 1][4] = int(input())
    print('The statistics for the revised game are: ', game_list[game_revise - 1])

    with open(filename, 'wb') as fi:
        pickle.dump(game_list, fi)

    return


# This function displays the statistics for the season's current games
def view_season(game_list):
    with open(filename, 'rb') as fi:
        game_list = pickle.load(fi)

    list_of_games = game_list
    games = len(list_of_games)
    minutes = 0
    goals = 0
    assists = 0
    yellow_cards = 0
    red_cards = 0

    for i in range(len(game_list)):
        minutes_add = game_list[i][0]
        minutes += minutes_add
    print('Minutes', minutes)

    for i in range(len(game_list)):
        goals_add = game_list[i][1]
        goals += goals_add
    print('Goals: ', goals)

    for i in range(len(game_list)):
        assists_add = game_list[i][2]
        assists += assists_add
    print('Assists: ', assists)

    for i in range(len(game_list)):
        yellows_add = game_list[i][3]
        yellow_cards += yellows_add
    print('Yellow cards: ', yellow_cards)

    for i in range(len(game_list)):
        reds_add = game_list[i][4]
        red_cards += reds_add
    print('Red cards: ', red_cards)

    goals_per_game = goals / games
    assists_per_game = assists / games
    min_per_game = minutes / games
    yellows_per_game = yellow_cards / games
    reds_per_game = red_cards / games

    print('Minutes per game: ' + '{:.2f}'.format(min_per_game))
    print('goals_per_game: ' + '{:.2f}'.format(goals_per_game))
    print('assists_per_game: ' + '{:.2f}'.format(assists_per_game))
    print('yellows_per_game: ' + '{:.2f}'.format(yellows_per_game))
    print('reds_per_game: ' + '{:.2f}'.format(reds_per_game))
    return

# This function displays the statistics for a individual game
def view_game(game_list):
    with open(filename, 'rb') as fi:
        game_list = pickle.load(fi)

    print('Which game do you want to view?')
    game_to_view = game_list[int(input()) - 1]
    print('Minutes:', game_to_view[0])
    print('Goals:', game_to_view[1])
    print('Assist:', game_to_view[2])
    print('Yellow cards:', game_to_view[3])
    print('Red cards:', game_to_view[4])
    return


choice = 0

while choice != 5:
    print("What would you like to do?")
    print("1. Add stats for a new game\n"
          "2. Revise stats for a game\n"
          "3. view season stats\n"
          "4. view stats for a specific game\n"
          "5. Exit")
    choice = int(input())
    if choice == 1:
        add_game_stats()
        # Saves game stats
        with open(filename, 'wb') as fi:
            pickle.dump(game_list, fi)

    if choice == 2:
        revise_game()
        with open(filename, 'wb') as fi:
            pickle.dump(game_list, fi)

    if choice == 3:
        #Loads game stats
        with open(filename, 'rb') as fi:
            game_list = pickle.load(fi)
        view_season(game_list)

    if choice == 4:
        with open(filename, 'rb') as fi:
            game_list = pickle.load(fi)
        view_game(game_list)

    if choice == 5:
        sys.exit()
