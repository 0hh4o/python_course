class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if self.draft - (1.5*self.crew) > 20 :
            return True
        else:
            return False
titanic = Ship(27.51,5)
print(titanic.is_worth_it())