
from lift import Lift
from utils import random_color
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
import os
import datetime

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'out'))

## CONFIG BELOW HERE
TOTAL_WEEKS = 26
WEEK_INTERVALS = 28

lifts = [
    Lift(name="squat", weight=225, lbs_per_lift=5, lifts_per_week=1.5, milestones=[275, 315, 365]),
    Lift(name="deadlift", weight=290, lbs_per_lift=5, lifts_per_week=1.5, milestones=[315, 405]),
    Lift(name="bench", weight=185, lbs_per_lift=2.5, lifts_per_week=1.5, milestones=[200, 225, 275]),
    Lift(name="press", weight=115, lbs_per_lift=2.5, lifts_per_week=1.5, milestones=[135, 150]),
]
## CONFIG ABOVE HERE

total_weeks = TOTAL_WEEKS
now = dt.datetime.now()
then = now + dt.timedelta(weeks=total_weeks)
days = mdates.drange(now,then,dt.timedelta(days=1))

output_buffer = ""

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=WEEK_INTERVALS))
plt.gcf().autofmt_xdate()
plt.title("Weight Progression Over Time")
plt.xlabel("Date")
plt.ylabel("Weight (lbs)")

for lift in lifts:
    # generate a sequence of values
    stop_weight = lift.weight + len(days) * lift.lbs_per_day
    values = np.arange(start=lift.weight, stop=stop_weight, step=lift.lbs_per_day)
    color = random_color()
    plt.plot(days, values, c=color, label=lift.label)
    for milestone in lift.milestones:
        days_until_milestone = lift.days_until_milestone(milestone)
        output_buffer += lift.format_milestone(milestone)
        plt.plot(days[days_until_milestone], milestone, marker="o",  c=color)
    output_buffer += "\n"

## WRITE TO FILE
filename = f"{datetime.datetime.now().strftime('%Y%m%d%H%M.log')}"
f = open(os.path.join(OUTPUT_DIR, filename), "w")
f.write(output_buffer)
f.close()

plt.legend()
plt.show()