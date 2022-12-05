# starting-strength
regressing across a series of lifts parameterized by current weight and progress, extrapolates out certain miletones, generates graph

### how to use me
1. update [src/config.py](/src/config.py) with your appropriate
2. run main.py
3. observe output graph and output log

### improvements
- cumulative milestones (e.g. 1k club)
- decay factor to increase realistic regression
- generate interactive UI to overlay these
- dynamically bound size of graph to milestones
- include milestones in label
- compute 1RM and other rep ranges
- convert lbs to kgs

### example output
![test_output](/img/test_v1.png)

```
squat 275 lbs on 2023-01-22  (7 weeks)
squat 315 lbs on 2023-02-26  (12 weeks)
squat 365 lbs on 2023-04-16  (19 weeks)

deadlift 315 lbs on 2023-01-01  (4 weeks)
deadlift 405 lbs on 2023-03-26  (16 weeks)

bench 200 lbs on 2023-01-01  (4 weeks)
bench 225 lbs on 2023-02-19  (11 weeks)
bench 275 lbs on 2023-05-21  (24 weeks)

press 135 lbs on 2023-01-15  (6 weeks)
press 150 lbs on 2023-02-12  (10 weeks)
```