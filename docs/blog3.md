---
layout: post
title: The Effects of Weather on MLB Hitting
date: 2020-07-27
author: Andrew Liu
---

One category of variables that we considered using for our model was weather and wind data.
This data was scraped directly from mlb.com and the four variables we scraped were the
weather in degrees, the weather type, the wind speed in miles per hour, and the wind direction.
The web scraping was done in BeautifulSoup4 and Selenium. We traversed through each day
between the 2014-2019 seasons and scraped the box score, venue, and weather and wind data
for each season game.

Data on MLB website:
!(./images/images2.png)

The rationale behind using these variables is that it might be easier or harder to get a hit during
different weather and wind conditions. For example, a player may be more physically drained
and thus have a more difficult time getting a hit if the weather is sunny and over 90 degrees. On
the contrary, a player may have an easier time getting a hit if the wind is strong and blowing
toward the outfield as it favors the batter.

In order to find out whether weather and wind data correlated with a player getting a hit, we
matched the weather data with game logs and ran some statistical tests. For the continuous
variables such as weather (degrees) and wind speed (mph), we first tried running logistic
regression. However, there was almost no linear correlation for either variable or combined to
be found with very small r<sup>2</sup>  values close to 0.

Weather (Degrees): 
Wind Speed (MPH):
Combined:

Similarly, the scatterplots that we created did not provide much insight:

Weather (Degrees) scatterplot:

Wind (MPH) scatterplot:
