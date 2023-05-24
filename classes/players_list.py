import matplotlib.pyplot as plt
from numpy import floor

class PlayersList:

    def __init__(self, players_list):
        self.players = players_list

    def compute_stats_average(self):
        for player in self.players:
            player.compute_stats_average()

    def plot_averages(self, to_save=True):
        for stat in ["PAC", "SHO", "PAS", "DRI", "DEF", "PHY"]:
            fig = plt.figure(figsize=(10, 5), dpi=150)
            ax = fig.subplots(nrows=1, ncols=1)

            plt.title(f"STAT: {stat}")

            xticks = list()
            data = list()
            val_min = 100
            for player in self.players:
                xticks.append(player.name)

                data_raw = player.stats_form[stat]
                for val in data_raw:
                    if val == 0 or val > 95:
                        print(player.name, stat, val)
                data.append(data_raw)

                val_min = min(val_min, min(data_raw))

            plt.boxplot(data, showmeans=True)

            print(xticks)

            ax.set_xticklabels(xticks)
            plt.xticks(rotation=45)
            # ax.get_xaxis().tick_bottom()
            # ax.get_yaxis().tick_left()
            val_min = 10 * floor(val_min/10)
            plt.ylim(ymax=100, ymin=val_min)

            plt.grid()

            if to_save:
                plt.savefig(f"../data/output/plots/{stat}.png")
            else:
                plt.show()
