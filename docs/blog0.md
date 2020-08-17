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

Below you will find a list of the models we tried using as well as the reasoning behind it. Since we had over 200 features in all, we had to also introduce dimensionality reduction techniques, which are covered in other blog posts, so check them out!

Overall, we took two approaches to modeling:
1. Training a model that will generalize from all the players in our dataset. With over 190,000 samples, a model may be able to do fairly well. [Alceo and Henriques (2017)](https://www.insticc.org/Primoris/Resources/PaperPdf.ashx?idPaper=83622 "link to paper") took this approach and achieved a 85% top 100 precision score. Additionally, splitting up the data for this method was fairly simple.
2. Training and modeling on a player-by-player basis. The logic behind this is that every player is different and has distinct preferences, and maybe we can come up with better models for individual players rather than on the whole dataset. The downside of this approach is that we won't have as many samples to train on. 

# Models we will explore

## 1. Binary Logistic Regression
Logistic regression is one of the most fundamental algorithms for binary classification. Unlike linear regression, which outputs continuous values, binary logistic regression utilizes a sigmoid function that converts the output into a number between 0 and 1. We can then round up or round down from that final prediction (or even specify our own threshold) to categorize our sample as being a hit or not a hit. It utilizes a cost function called Cross-Entropy or log-loss, which makes it easy to calculate the gradient and minimize our cost function. It penalizes confident and wrong predictions more than it rewards confident and right decisions. In our case with MLB hitting, we would like to be as confident as we can on our predictions, especially when we predict the outcome to be a hit. If we predict an incorrect outcome (let's say a hit when the result was not a hit), we want our model to penalize that type of behavior.

## 2. Random Forest
Random Forests are ensemble tree-based learning algorithms. Ensemble means there is a combination of separate algorithms (same or different) to classify an object. The Random Forest Classifier builds a set of decision trees by randomly bootstrapping and choosing a random subset of variables at each step. It then aggregates the votes from different decision trees and chooses the majority vote to decide the final class of the test object. The benefit of random forests are that they are easy to use and easy to interpret. Particularly when training a player-specific model, we can obtain a lot of really interesting information about what features are important and what features are not. This can tell us how a player behaves and how their preferences are different from other players. However, one downside is that it is based on decision trees, which can sometimes be inaccurate in practice.

## 3. Stochastic Gradient Descent
Like its name suggests, stochastic gradient descent utilizes gradient descent to minimize its cost function on training data. Stochastic gradient descent is an optimization algorithm that randomly selects a sample (typically of size 1) from the dataset for each iteration of calculating the gradient to minimize the loss function. With a hyperparameter loss function of log-loss, this classifier is similar to logistic regression, but distinguishes itself in the batch size it uses to train on each iteration (logistic regression classifier utilizes the whole training set in each iteration of calculating the gradient). For very large datasets like this one, SGD can come in handy for our our training. Specifically for our general model where we have over 200 features and 180,000 samples, we want to be able to train our models without too much computation. Lastly, SGD classifiers work really well with sparse floating point data, and with the wildly different ranges of baseball statistics, this could potentially be successful. 

## 4. Multilayer Perceptron
Lastly, we decided to see if a deep learning model could produce the best results, given the complex nature of our dataset. A multi-layer perceptron is a feed-forward neural network that consists of at least three layers of nodes: an input layer, a hidden layer, and an output layer.MLP uses backpropagation for training, which allows us to find more complex, non-linear relationships in the data. Additionally, [Alceo and Henriques (2017)](https://www.insticc.org/Primoris/Resources/PaperPdf.ashx?idPaper=83622 "link to paper") found that their baseball dataset  achieved an 85% top 100 precision score when using a three-layer MLP. We were driven to replicate and possibly do better than their results by using a similar model.

# What about Evaluation Metrics?
Probably the most important question to ask yourself when conducting a data science project is "by what metric will I evaluate the accuracy of my model?". Our main goal for this project was to "Beat the Streak", basically to correctly predict a set of up to two players that will get a base hit on any given day. If this were a gambling situation, there would be a lot at stake with each guess. If we were to guess that a player should get a hit, we want to almost never be wrong. In contrast, we are completely okay with guessing a player not to get a hit with the actual outcome of them receiving a hit (because we didn't lose anything). This means we are aiming to maximize our precision. Precision is calculated by the number of correctly guessed positive outcomes, "true positives", divided by the number of times you guessed the outcome was positive (true positives plus false positives). 

**[<-PREVIOUS PAGE]({{page.previous_}} "previous")** **[NEXT PAGE ->]({{page.next_}} "next")** <br><br>