class ScoreCounter:
    def __init__(self, for_arriving=100, for_unused_time=2,
                 for_all_frogs=1000, for_preserved_lives=100):
        self.score = 0
        self.for_arriving = for_arriving
        self.for_unused_time = for_unused_time
        self.for_all_frogs = for_all_frogs
        self.for_preserved_lives = for_preserved_lives

    def add_points_for_arriving(self):
        self.score += self.for_arriving

    def add_points_for_unused_time(self, seconds):
        self.score += int(seconds * self.for_unused_time)

    def add_points_for_saving_all_frogs(self):
        self.score += self.for_all_frogs

    def add_points_for_preserved_lives(self, lives):
        self.score += lives * self.for_preserved_lives
