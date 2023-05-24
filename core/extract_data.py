from pandas import read_csv

def extract_data(file_name):

    data = read_csv(file_name)

    number_of_columns = data.shape[1]

    number_of_players = int((number_of_columns - 2) / 6)
    print(f"A total of {number_of_players} players have been identified.")

    players = dict()

    for player_index in range(number_of_players):
        index_low = 2 + 6 * player_index
        index_high = 2 + 6 * (player_index + 1)

        data_score_person = data.iloc[:, index_low:index_high]
        # print(data_score_person)

        column_names = data_score_person.columns
        # print(column_names)
        player_index_response = column_names[0][4:]
        if player_index_response == "":
            player_index_response = 0
        else:
            player_index_response = int(player_index_response)

        # print(player_index, player_index_response)

        # Relabel columns
        columns_relabeling = dict()
        for index_col, column_name in enumerate(column_names):
            columns_relabeling[column_name] = column_name[:3]

        data_score_person.rename(columns=columns_relabeling, inplace=True)

        # Filter out the player own's asesment
        data_raw = read_csv("../data/player_data.csv")
        player_email = data_raw["email"].to_list()[player_index_response]
        print(player_email)




        players[player_index_response] = data_score_person
    return players


if __name__ == '__main__':
    extract_data()
