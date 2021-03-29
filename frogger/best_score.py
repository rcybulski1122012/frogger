class BestScore:
    def __init__(self, path):
        self.path = path

    def get(self):
        try:
            with open(self.path) as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def set(self, score):
        with open(self.path, "w") as f:
            f.write(str(score))
