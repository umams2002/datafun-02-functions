import statistics as stats

data_A = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean_data_A = stats.mean(data_A)
median_data_A = stats.median(data_A)
mode_data_A = stats.mode(data_A)
variance_data_A = stats.variance(data_A)

print(f"Mean of Data in {data_A}= ", mean_data_A)
print(f"Meadian of Data in {data_A}= ", median_data_A)
print(f"Mode of Data in {data_A}= ", mode_data_A)
print(f"Variance of Data in {data_A}= ", variance_data_A)

data_B = [2,86,87,88,111,86,103,87,94,78,77,85,99]

mean_data_B = stats.mean(data_B)
median_data_B = stats.median(data_B)
mode_data_B = stats.mode(data_B)
variance_data_B = stats.variance(data_B)

print(f"Mean of Data in {data_B}= ", mean_data_B)
print(f"Meadian of Data in {data_B}= ", median_data_B)
print(f"Mode of Data in {data_B}= ", mode_data_B)
print(f"Variance of Data in {data_B}= ", variance_data_B)