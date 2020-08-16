---
layout: post
title: Stadium Data and Methodology
date: 2020-08-06
author: Nate Barrett
---
![a](./images/Stadium0.jpg "a")

## Why Stadium? **[NEXT PAGE ->](./weatherandwind.html "next")**

To importance of data of each baseball stadium stems from internal player factors of their envoirnments. Players will tend to have a notion to feel more comfortable at there home stadium and less comfertable at away stadiums (or sometimes the other way around). This directly affects a players performance and causes the stadium to play an incremental role in the dataset.

With data gathered from each stadium of all 30 teams in the MLB, variables such as rate of Runs in a given baseball game, rate of hits in a given game, rate of home runs per game, etc. we provide statisical and theoretical inferences of the data of stadiums for each hitter that plays at each specific stadium. This analysis gives additonal insight into how a player performs rather they play in a cold winter night in Colorado, or a blazing hot evening in Arizona.

The overall data anlysis of stadiums will leave us with a further layer of analysis of hitting, pitching, and weather. Which altogether will contribute heavily to our goal of finding out whether or not a specific player will get a hit during gameitme. 

##  Sources

This data was retrieved from the [ESPN MLB Statcast Data Archive](http://www.espn.com/mlb/stats/parkfactor) which is composed of much data surrounding MLB Stadiums such as general httting metrics , pitching metrics, and weather metrics of each given baseball stadium. The selected Park Factor data doesn't use average value metrics to measure the hitting and pitching stats of each stadium, Park Factor compares the rate of stats at home vs. the rate of stats on the road. A rate higher than 1.000 favors the hitter. Below 1.000 favors the pitcher. Teams with home games in multiple stadiums list aggregate Park Factors. The methodology of analysis for these park factors was mostly done using Python, more specifically the numpy, scipy, Sci-kit learn, and pandas packages respectively. 
