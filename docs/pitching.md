---
layout: post
title: Pitching Data and Methodology
date: 2020-08-03
author: Elon Glouberman
---
![pitcher](./images/pitching_image.jpg "pitcher")

## Why Pitching? **[NEXT PAGE ->](./stadium.html "next")**

When there is a hitter, there is a pitcher. You can't have one without the other. To only collect pitching stats or only batting stats is gathering one part of the story. When trying to predict whether a player will get a hit a hit in a given MLB game, we are also figuring out whether a pitcher will give up a hit as well. 

Before every MLB game, we can obtain information like who the starting pitcher will be as well as their history of performances. Pitching stats that we thought were relevant were hits allowed per innings pitched (on the season and in the last x games), strikeout rate (more strikeouts probably mean that batters have a tougher time facing the pitcher), ground ball rate, average pitches per appearance, and detailed stats from the previous game they pitched. 

Other metrics we collected include variables that could have a potential predictive significance such as earned run average (ERA), innings pitched on the season, Walks/hits per innings pitched (WHIP), and number of batters faced on the season.

Variables were aggregated on a game-by-game basis for each season the pitcher played. We also calculated rolling 10, 20, and 30 day window averages to account for potential "streaky" behavior, which is very common for pitchers in the MLB.


## Methodology and Sources

We obtained probable pitcher information from the same API we used for hitting. For the conventional stats such as ERA, hits allowed, strikeouts, and game-by-game data, we utilized Beautiful Soup as a web scraper and scraped [Baseball Reference](https://www.baseball-reference.com/), a popular baseball statistics website. Starting with a list of names of probable pitchers obtained from the hitting data, for a given player and season, the web scraper returned game logs for that specified player (code can be found [here](https://github.com/eglouberman/MLB-hit-predictor/blob/master/pitch_scraper.py)). The game logs included about 50 data points such as aggregated ERA on the season, opponents, number of pitches, innings pitched, walks, HR allowed, etc. Then, using NumPy in Python, I manually aggregated single game statistics such as hits allowed to obtain hits allowed per innings pitched. Using similar methodology, I calculated about 15 more data points which included strikeout rate, ground ball percentages, and rolling averages for the main metrics (to possibly account for "streaky" behavior).