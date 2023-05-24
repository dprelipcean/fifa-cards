class Player:
    def __init__(self, name, number, position, stats_form):

        self.name = name
        self.number = number
        self.position = position

        self.stats_form = stats_form

        self.stats_average = dict()

    def compute_stats_average(self):
        for stat in self.stats_form.columns:
            data_raw = self.stats_form[stat]

            self.stats_average[stat] = sum(data_raw) / len(data_raw)

    def get_pace(self):
        return self.stats_average["PAC"]
