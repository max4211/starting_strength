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
