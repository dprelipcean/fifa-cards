meta_data_keys = "Timestamp,Email Address,"

player_stats = "PAC,SHO,PAS,DRI,DEF,PHY,"

number_of_players = 13
header_new = meta_data_keys
for index_ in range(number_of_players):
    header_new += player_stats

print(header_new)
