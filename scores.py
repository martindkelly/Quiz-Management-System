
class Scores:

    def __init__(self):
        self.correct = 0
        self.total = 0
    
    def inc_score(self):
        self.correct += 1
        self.total += 1

    def inc_wrong(self):
        self.total += 1

    def get_correct(self):
        return self.correct
    
    def get_total(self):
        return self.total
    
    def get_percentage(self):
        if self.total == 0:
            return 0.0
        else:
            return round((self.correct / self.total) * 100, 1)
    