"""Script to extract the data from the form csv format into other formats."""

from pandas import read_csv, DataFrame


def extract_data(file_name):
    data = read_csv(file_name)

    number_of_columns = data.shape[1]

    number_of_players = int((number_of_columns - 2) / 6)
    print(f"A total of {number_of_players} players have been identified.")

    data_raw = read_csv("../data/input/player_data.csv")
    list_of_player_names = data_raw["name"].to_list()
    list_of_player_emails = data_raw["email"].to_list()

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

        player_name = list_of_player_names[player_index_response]
        player_email = list_of_player_emails[player_index_response]
        print(player_name, player_email)

        # Filter out the player own assesment
        list_of_email_addresses = data["Email Address"].to_list()
        if player_email in list_of_email_addresses:
            index_vote = list_of_email_addresses.index(player_email)
            data_score_person.drop(index_vote, inplace=True)

        print(data_score_person)

        players[player_name] = data_score_person

        data_score_person.to_csv(f"../data/output/stats_per_player/{player_name}.csv")

    column_names = ["PAC", "SHO", "PAS", "DRI", "DEF", "PHY"]
    for row in data.iterrows():
        row = row[1]
        email_voter = row["Email Address"]
        voter_dict = dict()
        for player_index in range(number_of_players):
            index_low = 2 + 6 * player_index
            index_high = 2 + 6 * (player_index + 1)

            player_name = data_raw["name"].to_list()[player_index]

            data_votes = row.iloc[index_low:index_high].to_list()
            # print(data_votes)

            voter_dict[player_name] = data_votes

        voter_dataframe = DataFrame.from_dict(voter_dict, orient="index", columns=column_names)
        voter_dataframe.to_csv(f"../data/output/votes_per_voter/{email_voter}.csv")

    return players


# if __name__ == '__main__':
#     extract_data()
