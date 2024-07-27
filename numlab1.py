# Hi! I am new to python numpy. Can you generate some realworld situations where I can use a numpy array with some source code.
import numpy as np

temperatures = np.array([22, 21, 23, 24, 22, 25, 26, 25, 24, 23, 22, 21, 20, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])

mean_temp = np.mean(temperatures)
print(f"Mean Temperature: {mean_temp}")

std_temp = np.std(temperatures)
print(f"Standard Deviation: {std_temp}")

max_temp = np.max(temperatures)
print(f"Maximum Temperature: {max_temp}")

min_temp = np.min(temperatures)
print(f"Minimum Temperature: {min_temp}")

# Hi! let's create a real life example involving weather data. Use numpy to analyze temperature data for a week, perform slicing, indexing, shaping and reshaping operations and calculate various statistics.

# Create sample data
temperature_data = np.array([   [22.1, 23.4, 21.9, 22.8],[23.0, 24.1, 22.5, 23.2],[24.3, 25.0, 23.8, 24.0],[22.8, 23.2, 21.7, 22.5],[21.9, 22.5, 20.8, 21.5],[20.5, 21.0, 19.8, 20.0],[19.8, 20.3, 18.9, 19.5]])

# Slicing and Indexing
day_3_temps = temperature_data[2]
second_time_temps = temperature_data[:, 1]
first_three_days = temperature_data[:3]

# Shaping and Reshaping
reshaped_data = temperature_data.reshape(2, -1)
original_shape = reshaped_data.reshape(7, 4)

# Statistics
daily_avg = np.mean(temperature_data, axis=1)
time_of_day_avg = np.mean(temperature_data, axis=0)
overall_avg = np.mean(temperature_data)
temperature_range = np.ptp(temperature_data, axis=1)
highest_temp = np.max(temperature_data)
lowest_temp = np.min(temperature_data)

# Print results
print("Day 3 temperatures:", day_3_temps)
print("Temperatures at the second time of the day:", second_time_temps)
print("Temperature data for the first three days:\n", first_three_days)
print("Reshaped data:\n", reshaped_data)
print("Reshaped back to original shape:\n", original_shape)
print("Average temperature for each day:", daily_avg)
print("Average temperature for each time of the day:", time_of_day_avg)
print("Overall average temperature:", overall_avg)
print("Temperature range for each day:", temperature_range)
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)
