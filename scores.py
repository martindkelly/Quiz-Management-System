#class for keeping track of users scores
class Scores:

    def __init__(self):
        self.correct = 0
        self.total = 0
    
    #for correct score increment correct and total
    def inc_score(self):
        self.correct += 1
        self.total += 1

    #for wrong score only increment total
    def inc_wrong(self):
        self.total += 1

    def get_correct(self):
        return self.correct
    
    def get_total(self):
        return self.total
    
    #returns percentage of correct answers rounded to 1 decimal place
    def get_percentage(self):
        if self.total == 0:
            return 0.0
        else:
            return round((self.correct / self.total) * 100, 1)
    