# update me to generate appropriate outputs

from lift import Lift

lifts = [
    Lift(name="squat", weight=225, lbs_per_lift=5, lifts_per_week=1.5, milestones=[275, 315, 365]),
    Lift(name="deadlift", weight=290, lbs_per_lift=5, lifts_per_week=1.5, milestones=[315, 405]),
    Lift(name="bench", weight=185, lbs_per_lift=2.5, lifts_per_week=1.5, milestones=[200, 225, 275]),
    Lift(name="press", weight=115, lbs_per_lift=2.5, lifts_per_week=1.5, milestones=[135, 150]),
]