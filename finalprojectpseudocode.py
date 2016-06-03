# analyze the price of oil over 30 years dating from January 1986 to January 2016
# Quandl API
from json import load
import json
apiUrl = "https://www.quandl.com/api/v3/datasets/OPEC/ORB.json"
# import quandl
# mydata = quandl.get("FRED/GDP")
https://www.quandl.com/api/v3/datasets/FRED/NGDPPOT.json?api_key=8gLiMf99KJ6ZKjEdkSii

# take data from Quandl on the Real Potential GDP
# import data to sublime
# take data from Quandl on the Price of Oil
# import data to sublime
# store data in list
# for loop: for time < 2017 and > 1986, return mean, median, standard deviation, and variance
# find the mean of the Real Potential GDP
# set = meanGDP
# print "The mean of the Real Potential GDP is" , meanGDP 
# find the mean of the Price of Oil
# set = meanPOil
# find the median of the Real Potential GDP

# find the median of the Price of Oil
# find the population standard deviation of the Real Potential GDP
# find the population standard deviation of the Price of Oil
# find the population variance of the Real Potential GDP
# find the population variance of the Price of Oil
# for 
#set all to variables
# if mean GDP(variable) from 1986-2016 is increasing, AND mean oil price from 1986-2016 is increasing
# say "there is a positive correlation between the Real Potential GDP and the Price of Oil"
# elif mean GDP(variable) from 1986-2016 is increasing, AND mean oil price from 1986-2016 is decreasing
# say "there is a negative correlation between the Real Potential GDP and the Price of Oil"
# elif mean GDP(variable) from 1986-2016 is not increasing or decreasing, or mean Price of Oil(variable) is not increasing or decreasing
# say "there is no correlation between the two"
# compute a confidence interval 
# find the z value
# mean +/- z*sigma and  sigma = s / sqrt(n)
# 68% confidence interval: stats.norm.interval(0.68, loc=mu, scale=sigma/sqrt(N))
