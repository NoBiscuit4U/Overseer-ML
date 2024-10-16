# About
This repo is my personal library for machine learning.
Here are a few things about this repo.

- I will research new and interesting topics and learn/implement them into code.

- I will also minimize the usage of other libraries mainly only using numpy and matplotlib.

>[!IMPORTANT]
>Since I will be working with csvs for training and test datasets, any csvs used will
>have an associated link in a text file pertaining to the location to which I found it.
> 
>To find this file look in the csvs folder and look for CsvLocations.md

# Currently Working Models
## Linear Regression
Linear Regression is a simple machine learning model used to find the line of best fit.

This can then be used to visualize the correlation between an independent variable (y-axis), and a dependent variable (x-axis)[^1].
[^1]: A correlation between any two variables does not mean they are the sole cause of each other's increase or decrease.

**Example**

![Example](<Screenshot 2024-05-27 212437.png>)[^2]

[^2]: The x and y values are 0-1 because they have been normalized. Normalization is when you use the min and max of a set of numbers to get
a set of numbers between 0-1 that have the same variation as the previous values. 
Normalization Formula: xnorm = x - xmin / xmax - xmin


This example shows the correlation between temperature and ice cream sales.

The blue line is the line of best fit, and the orange line shows data point variation off the line of best fit.

## K-Means
K-means is a simple machine learning model that groups points on a graph based on their distance to a centroid.

K-means is used for basic data grouping and analyzing basic data structure.

**Example**

![Example](<Figure_1.png>)

This example shows three distinct groups of points centralized around the convergence position of each centroid.
