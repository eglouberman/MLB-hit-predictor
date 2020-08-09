---
layout: post
title: Weather and Wind Data and Methodology
date: 2020-08-09
author: Andrew Liu
---
![cloudy](./images/cloudy.jpg "cloudy")

## Why Weather and Wind?



## Methodology and Sources

The weather and wind data were scraped off of mlb.com/scores using Python and the BeautifulSoup4 and Selenium libraries. The scraper parsed through each date within the 2014-2019 seasons and clicked on the box score of each regular season game (discludes training or exhibition games). Within the box score, multiple data fields were collected such as the date, the overall score of the game, the venue, and the weather and wind data. In total, the following 10 variables were collected for each game: Date, Team 1, Team 2, Team 1 Score, Team 2 Score, Venue, Weather (Degrees), Weather Type, Wind (MPH), and Wind Direction.
