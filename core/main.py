from pandas import read_csv

from core.extract_data import extract_data

from classes.player import Player
from classes.players_list import PlayersList


def main():
    file_name = "../data/FIFA Player Card stats (Responses) - Form Responses 1.csv"
    player_stats = extract_data(file_name)
    # print(player_stats)

    file_name = "../data/player_data.csv"
    players_data = read_csv(file_name)
    # print(player_data)

    players_list = list()
    for index_player in range(players_data.shape[0]):
        player_data = players_data.loc[index_player]

        player_name = player_data["name"]
        player_number = player_data["number"]
        player_position = player_data["position"]

        player_stats_form = player_stats[index_player]

        player = Player(player_name, player_number, player_position, player_stats_form)

        players_list.append(player)

    players_list = PlayersList(players_list)

    players_list.compute_stats_average()

    players_list.plot_averages()


if __name__ == '__main__':
    main()
