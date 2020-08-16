---
layout: default
---
# MLB HIT PREDICTOR
<em>Building a machine learning classifier to predict which MLB players will achieve a base-hit on any given day.</em> 

![home](./docs/images/home_image1.png "splash")

## About

Our project explores one of the most iconic outcomes in sports- the major league base hit. We were inspired to approach this problem by a betting game called "Beat the Streak". In the form of an app, you can pick up to two players each day who you think will get a hit, and if you get 57 in a row correct, you can win 5.6 million dollars! While getting rich from this project would surely be a nice (and unlikely) benefit, we decided to give this problem a go using the most powerful tool our disposal, statistical reasoning and data science. Previous attempts at this problem have been quite successful, but not perfect. [Alceo and Henriques (2017)](https://www.insticc.org/Primoris/Resources/PaperPdf.ashx?idPaper=83622 "link to paper") utilized batter performance, team performance, weather, and ballpark characterstics to achieve an 85 percent correct-pick-ratio using machine learning classifiers. Our project aims to mimic the concept behind their success and develop our own model(s) to achieve even greater accuracy.

Our goal was to build an end-to-end data science project, from building a centralized MySQL database using AWS RDS, to data cleaning and engineering in Python (and a bit of R), to data modeling (Python). We spent about five weeks conducting initial research, five weeks scraping and data exploration, and another ten weeks modeling and building this website.

## Data Collection and Preparation

We collected baseball statistics from the years 2014-2019, and over 190,000 samples. The data was collected from many different sources using many different methods: API's, web scraping, etc. Click below on each type of data to learn the importance of it and how it was attained. The database was organized using Amazon Web Services RDS on a mySQL server. We utilized RDS due to its easiness to set up, free storage space, and convenient accessibility among group members. 

* [#1 : Batting Data](./docs/batting.html)
* [#2 : Pitching Data](./docs/pitching.html)
* [#3 : Stadium Data](./docs/stadium.html)
* [#4 : Weather and Wind Data](./docs/weatherandwind.html)

## Exploratory Analysis & Modeling

* [Framing Our Project into Machine Learning Terms](./docs/blog0.html)
* [Variable Selection (Part 1)](./docs/blog1.html)
* [Variable Selection (Part 2)](./docs/blog2.html)
* [Does Weather and Wind Matter?](./docs/blog3.html)
* [Optimizing Logisitic Regression Model](./docs/blog4.html)
* [Player-specific Models](./docs/blog5.html)
* [Multilayer Perceptron](./docs/blog6.html)

## Results & Conclusion
We made a great model and achieved 100 percent accuracy. The model that was best was this and the model that was worst was this. 
* [Multi-player Models Results](./docs/blog7.html)
* [Player-specific Models Results](./docs/blog8.html)
* [Putting it all Together](./docs/blog9.html)


## Who We Are
We are a group of curious and passionate college students from UCLA. We organized this project through the Data Science Union at UCLA. Learn more about us below!

|![Elon's photo](./docs/images/elon.jpg "home_photo")|![Andrew's photo](./docs/images/andrew.png "home_photo")|![nate's photo](./docs/images/nate.png "home_photo")|
|[Elon Glouberman](./docs/bio.html#elon-glouberman)|[Andrew Liu](./docs/bio.html#andrew-liu)|[Nathaniel Barrett](./docs/bio.html#nathaniel-barrett)
|Project Lead|Project Associate|Project Associate
