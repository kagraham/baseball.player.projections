# baseball.player.projections

This repository makes a prediction of baseball outcomes. This was a project I worked on for an MLB organization.

The matchupdata.csv file contains the offensive outcome (higher number is a better outcome) for a batter (batterID) against a pitcher (pitcherID). 

Matchup_projections.py builds a model to project average offensive outcomes for each batterID for the following season, using the information from matchupdata.csv. In this example, each batter had exactly 300 at-bats against a randomly selected pitcher from the dataset.

In this work, I used a Bayesian ridge regression. To get the best prediction, we would want to consider how the batter performed overall, how a particular pitcher performed overall, and how a batter performed against a particular pitcher, if that matchup was randomly selected. The previous season outcomes were normally distributed (see previous_season_histogram.png), an important consideration when using linear models. Bayesian ridge uses probabilistic outcomes, as opposed to point estimates, for a linear regression prediction. 

next_season_projections.csv contains my predictions for the batters.

results_comparison.png is a linear regression comparing the previous and projected season outcomes. It demonstrates how the projected average player outcomes did not deviate far from their previous season performance. For all 100 batters, there was a mean average difference (absolute value) of 0.237.

verification.py was used to build the results comparison image.
