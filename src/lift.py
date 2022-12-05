import math

class Lift:
    def __init__(self, name, weight, lbs_per_lift, lifts_per_week, milestones):
        self.name = name
        self.weight = weight
        self.milestones = milestones
        self.lbs_per_lift = lbs_per_lift
        self.lifts_per_week = lifts_per_week
        self.lbs_per_week = lbs_per_lift * lifts_per_week
        self.lbs_per_day = self.lbs_per_week / 7 # strictly used for modeling estimation
        self.label = f"{name} | {self.lbs_per_week} lbs/wk"

    def weeks_until_milestone(self, milestone, round=True):
        exact_weeks = (milestone - self.weight) / self.lbs_per_week
        return self.round_result(exact_weeks, round)

    def days_until_milestone(self, milestone, round=True):
        exact_days = (milestone - self.weight) / (self.lbs_per_day)
        return self.round_result(exact_days, round)

    def round_result(self, result, round):
        return math.ceil(result) if round else result