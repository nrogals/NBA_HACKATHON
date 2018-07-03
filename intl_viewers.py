#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:46:11 2018

@author: vsomdec
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import datetime
import os 


cwd=os.getcwd()
data_path=cwd +"\\Business Analytics\\Business Analytics\\Business Analytics\\"

training_data = pd.read_csv(data_path+ "training_set.csv")
training_data.head()

#training_data = training_data.join(pd.get_dummies(training_data["Country"]))
training_data = training_data.drop(columns=["Season"])
training_data = training_data.groupby(['Game_ID','Game_Date', 'Away_Team', 'Home_Team'])['Rounded Viewers'].sum().reset_index()


training_data = training_data.join(pd.get_dummies(training_data["Home_Team"]))
training_data = training_data.join(pd.get_dummies(training_data["Away_Team"]), rsuffix="_away")
training_data["Month"]=""
training_data["Week Day"]=""

for index, row in training_data.iterrows():
   training_data.at[index, "Month"] = datetime.datetime.strptime(row["Game_Date"], "%m/%d/%Y").month
   training_data.at[index, "Week Day"] = datetime.datetime.strptime(row["Game_Date"], "%m/%d/%Y").weekday()

training_data = training_data.join(pd.get_dummies(training_data["Month"]), rsuffix="_month")
training_data = training_data.join(pd.get_dummies(training_data["Week Day"]), rsuffix="_week")


game_data = pd.read_csv(data_path+"game_data.csv")
player_data = pd.read_csv(data_path + "player_data.csv")
split_idx = int(len(training_data)*.8)
train = training_data[:split_idx]
test = training_data[split_idx:]

train_y = train["Rounded Viewers"]
train_x = train.drop(columns=["Rounded Viewers"])

test_y = test["Rounded Viewers"]
test_x = test.drop(columns=["Rounded Viewers"])

regr = linear_model.LinearRegression()



# Train the model using the training sets
regr.fit(train_x, train_y)

# Make predictions using the testing set
pred_y = regr.predict(test_x)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(test_y, pred_y))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(test_y, pred_y))

# Plot outputs
plt.scatter(test_x, test_y,  color='black')
plt.plot(test_x, pred_y, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()