import numpy as np

house_prices = np.array([350000, 420000, 310000, 275000, 500000, 450000, 380000, 290000, 330000, 370000, 510000, 790000])


#Filter the array to get the prices of houses that are above 400,000 with filter and while loop
filtered = [ ]
for x in house_prices:
    if x > 400000:
        filtered.append(True)
    else:
        filtered.append(False)

new_filtered = np.array(house_prices[filtered])

x = np.where(house_prices>400000)
where_filtered = house_prices[x]

# print("Simple filtered: ", new_filtered)
# print("Where filtered: ", where_filtered)


#sorting in asc and desc

asc = np.sort(house_prices) 
desc = asc[::-1]
# print("Ascending orded: ", asc)
# print("Descending order: ", desc)

#Calculate the median
median = np.median(house_prices)
# print(median)

#Standard deviation
standard_dev = np.std(house_prices)
# print(standard_dev)

#Variance
variance = np.var(house_prices)
# print(variance)


#calculate the median 
n = len(house_prices)
if n % 2 == 1:
    med = asc[n // 2]
elif n % 2 == 0:
    med = (asc[(n // 2) - 1] + asc[(n // 2 )]) / 2

# print(med)

mean = np.mean(house_prices)
# print(mean)

#standard deviation calculation
sum_deviations = sum((house_prices - mean)**2)
std_deviation = np.sqrt(sum_deviations/n)
# print(std_deviation)

#calculate the variance
variance = sum_deviations/n
# print(variance)

#Percentile 25%, 50%, 75% 
percentile_25 = np.percentile(house_prices, 25)
percentile_50 = np.percentile(house_prices, 50)
percentile_75 = np.percentile(house_prices, 75)
# print(percentile_25)
# print(percentile_50)
# print(percentile_75)

#quantile 0.3, 0.6, 0.8
quantile_03 = np.quantile(house_prices, 0.3)
quantile_06 = np.quantile(house_prices, 0.6)
quantile_08 = np.quantile(house_prices, 0.8)
# print(quantile_03)
# print(quantile_06)
# print(quantile_08)


histogram = np.histogram(house_prices)
# print(histogram)

minimum_value = np.min(house_prices)
# print(minimum_value)

maximum_value = np.max(house_prices)
# print("Maximum value: ", maximum_value)

below_350 = house_prices[house_prices<350000]
# print(below_350)
# print("Average price of houses with price below 350000: ", np.average(below_350))

sum_prices = np.sum(house_prices)
# print(sum_prices)

prices_last_year =  np.array([370000, 440000, 220000, 510000, 670000, 110000, 720000, 410000, 650000, 340000, 610000, 320000])


#Year over year growth individually
# for i in range(len(house_prices)):
#     yoy = ((prices_last_year[i]) - (house_prices[i]))/ np.absolute(house_prices[i]) * 100
#     print(yoy)

# houses that increased in price
increased = prices_last_year>house_prices
# print(increased)

# Houses that have not increased in price
not_increased = house_prices[house_prices>prices_last_year]
# print(not_increased)


