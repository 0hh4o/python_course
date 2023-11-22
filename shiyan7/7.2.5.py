class User:
    def __init__(self,rank = -8,progress = 0):
        self.rank = rank
        self.progress = progress
    def progress(self):
        return self.progress
    def rank(self):
        return self.rank
    def inc_progress(self,activity_rank):
        if activity_rank < -8 or activity_rank == 0 or activity_rank > 8:
            raise ValueError("Invalid activity rank")

        rank_diff = activity_rank - self.rank
        if (self.rank*activity_rank < 0) and (rank_diff == -2):
            rank_diff += 1
        elif self.rank*activity_rank < 0:
            rank_diff -= 1

        if rank_diff == 0:
            progress = 3
        elif rank_diff == -1:
            progress = 1
        elif rank_diff > 0:
            progress = 10 * rank_diff * rank_diff
        else:
            progress = 0

        if rank_diff < 0:
            progress = max(-50, progress)

        self.progress += progress

        while self.progress >= 100:
            self.progress -= 100
            if self.rank == -1:
                self.rank += 2
            else:
                self.rank += 1
                if self.rank == 0:
                    self.rank = 1

        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
user = User(rank = -2)
user.inc_progress(-1)
print(user.progress)
user.inc_progress(-1)
print(user.progress)
print(user.rank)