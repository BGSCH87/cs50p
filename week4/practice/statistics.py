import statistics


#median is the middle value in a list. If there are an even number of values, it will return the average of the two middle values.
median = statistics.median([1, 2, 3, 4, 5, 65]) # 3.5
print(median)

#mode is the most common value in a list. If there are multiple values that are the most common, it will return the first one it finds.
mode = statistics.mode([1, 2, 3, 4, 5, 65, 1]) # 1
print(mode)

#standard deviation is a measure of the amount of variation or dispersion of a set of values.
stdev = statistics.stdev([1, 2, 3, 4, 5, 65]) # 24.49489742783178
print(stdev)

#variance is a measure of how much a set of values varies from the mean.
variance = statistics.variance([1, 2, 3, 4, 5, 65]) # 600.0
print(variance)

#quantiles is a function that takes a list of numbers and returns the quantiles of that list. 
#The quantiles are the values that divide the list into four equal parts.
quantiles = statistics.quantiles([1, 2, 3, 4, 5, 6]) # [2.25, 3.5, 4.75]
print(quantiles)

