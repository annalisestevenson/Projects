# analyze the price of oil over 30 years dating from January 1986 to January 2016
# Quandl API
import requests

import json
from json import load
apiUrl = "https://www.quandl.com/api/v3/datasets/BUNDESBANK/BBK01_WT5511.json?api_key=8gLiMf99KJ6ZKjEdkSii"

data = requests.get(apiUrl).text
data_json = json.loads(data)
# import requests
# data = requests.get(apiURL)

# json_obj = load(response)
# response.json()
# print data
# for i in data:
# 	if i[]

new_data = data_json["dataset"]["data"]
# print new_data[0:201]
print min(new_data) 
print max(new_data)

import numpy as np
import pylab
import matplotlib.pyplot
import cmath
import scipy
from scipy import stats
from scipy.stats import norm

#importing pyplot
from matplotlib import pyplot as plt
gold = {4.18: 1237.7, 4.15: 1229.75, 4.14: 1240.3, 4.13: 1245.75, 4.12: 1259.2, 4.11: 1247.25, 4.08: 1235, 4.07: 1237.5, 4.06: 1225.75, 4.04: 1215, 4.01: 1232.1, 3.31: 1233.6, 3.30: 1238.2, 3.29: 1216.45, 3.24: 1216.45, 3.23: 1232.2, 3.22: 1251.8, 3.21: 1244.25, 3.18: 1254.5, 3.17: 1269.6, 3.16: 1233.1, 3.15: 1233.6, 3.14: 1256.55, 3.11: 1262.25, 3.10: 1247.25, 3.09: 1258.25, 3.08: 1274.1, 3.07: 1267.6, 3.04: 1271.5, 3.03: 1241.95, 3.02: 1229.35, 3.01: 1240, 2.29: 1234.15, 2.26: 1231, 2.25: 1235.4, 2.24: 1232.25, 2.23: 1218.75, 2.22: 1203.65, 2.19: 1221.5, 2.18: 1204.4, 2.17: 1202.4, 2.16: 1212, 2.15: 1208.45, 2.12: 1239.5, 2.11: 1223.25, 2.10: 1183.4, 2.09: 1188.9, 2.08: 1173.4, 2.05: 1158.5, 2.04: 1146.25, 2.03: 1130, 2.02: 1123.6, 2.01: 1122}
print gold.keys()
kdict = gold.keys()
print gold.values()
vdict = gold.values()
print "The mean price is" , float(sum(vdict))/len(gold)
# print cmath.polar(gold)
# print numpy.mean(gold)
# x = [4.18, 4.15,4.14, 4.113, ]
x = [gold.keys()]
y = [gold.values()]
print "The Standard deviation for the price of gold over time is" , np.std(y)
print "THe variance for the price of gold over time is" , np.var(y)
print "THe median of the price of gold is" , np.median(y)
print "Some info:" , scipy.stats.describe(y, axis=0)
print "Mean:" , np.mean(y)
print scipy.stats.mstats.find_repeats(y)
print "The z-score is" , scipy.stats.zscore(y, axis = 1, ddof =1)
#plotting to our canvas

plt.scatter(x,y, linewidth=5)
# plt.scatter(x2, y2, linewidth=5)
plt.title("Price of Gold")
plt.ylabel("Price")
plt.xlabel("Date")

plt.legend()
plt.grid(True, color ="k")


#showing what we plotted
plt.show()


# print float(sum(new_data))/len((new_data))


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
