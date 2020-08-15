---
layout: post
title: Framing Our Project into Machine Learning Terms 
date: 2020-07-30
author: Elon Glouberman
previous_: ./weatherandwind.html
next_: ./blog1.html 
---
![baseball](./images/home_image3.png "baseball")
**[<-PREVIOUS PAGE]({{page.previous_}} "previous")** **[NEXT PAGE ->]({{page.next_}} "next")** <br><br>
# The Problem

Can we build a machine learning classifier to predict which MLB players will achieve a base-hit on any given day? The problem at its core is a supervised learning task. The predictor variables as mentioned in the previous section are a batter's stats, the starting pitcher's pitching stats, stadium statistics, and that day's weather. The response variable, or the metric we are trying to predict, is a 1 or a 0: a player achieving a hit by the end of that game or going hitless. Since we can frame our project to either have an outcome of 1 or 0, it is a binary classification problem! 

Below you will find a list of the models we tried using as well as the reasoning behind it. Since we had over 200 data points in all, we had to also introduce dimensionality reduction techniques, which are covered in other blog posts, so check them out!

Overall, we took two approaches to modeling:
1. Training a model that will generalize from all the players in our dataset. With over 190,000 samples, a model may be able to do fairly well. [Alceo and Henriques (2017)](https://www.insticc.org/Primoris/Resources/PaperPdf.ashx?idPaper=83622 "link to paper") took this approach and achieved a 85% top 100 precision score. Additionally, splitting up the data for this method was fairly simple.
2. Training and modeling on a player-by-player basis. The logic behind this is that every player is different and has distinct preferences, and maybe we can come up with better models for individual players rather than on the whole dataset. The downside of this approach is that we won't have as many samples to train on. 

# Models we will explore

## 1. Logistic Regression

## 2. Random Forest

## 3. Stochastic Gradient Descent

## 4. Multilayer Perceptron

# What about Evaluation Metrics?


**[<-PREVIOUS PAGE]({{page.previous_}} "previous")** **[NEXT PAGE ->]({{page.next_}} "next")** <br><br>