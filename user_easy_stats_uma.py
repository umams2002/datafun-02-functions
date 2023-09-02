from util_logger import setup_logger
logger, logname = setup_logger(__file__)

import statistics
import sys

uni_data =[261.96,
731.94,
14.62,
957.5775,
22.368,
48.86,
7.28,
907.152,
18.504,
114.9,
1706.184,
911.424,
15.552,
407.976,
68.81,
2.544,
665.88,
55.5,
8.56,
213.48,
22.72,
19.46,
60.34,
71.372,
1044.63,
11.648,
90.57,
3083.43,
9.618,
124.2,
3.264,
86.304,
6.858,
15.76,
29.472,
1097.544,
190.92,
113.328,
532.3992,
212.058,
371.168,
147.168,
77.88,
]

logger.info("uni_data = " + str(uni_data))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)

# TODO: change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var    = " + str(round((var),2) ))
logger.info(f"stdev  = " + str(round((stdev),2) )) 
logger.info(f"lowest = " + str(round((lowest),2) ))
logger.info(f"highest= " + str(round((highest),2) )) 


# Descriptive: Univariant Time Series Data.........................

# describe relationships
# univariant time series data (one variable over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xSales= [261.96,
731.94,
14.62,
957.5775,
22.368,
48.86,
7.28,
907.152,
18.504,
114.9,
1706.184,
911.424,
15.552,
407.976,
68.81,
2.544,
665.88,
55.5,
8.56,
213.48,
22.72,
19.46,
60.34,
71.372,
1044.63,
11.648,
90.57,
3083.43,
9.618,
124.2,
3.264,
86.304,
6.858,
15.76,
29.472,
1097.544,
190.92,
113.328,
532.3992,
212.058,
371.168,
147.168,
77.88,
]

yQuantity = [2,
3,
2,
5,
2,
7,
4,
6,
3,
5,
9,
4,
3,
3,
5,
3,
6,
2,
2,
3,
4,
7,
7,
2,
3,
2,
3,
7,
2,
3,
2,
6,
6,
2,
3,
7,
5,
9,
3,
3,
4,
4,
2,
]


# if the lists are not the same size,
# log an error and quit the program
if len(xSales) != len(yQuantity):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xSales)}!={len(yQuantity)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the new correlation function from the statistics module
xx_corr = statistics.correlation(xSales, xSales)
xy_corr = statistics.correlation(xSales, yQuantity)

# log the information
logger.info("Here's some time series data:")
logger.info(f"xSales:{xSales}")
logger.info(f"yQuantity:{yQuantity}")
logger.info(f"correlation between xSales and xSales = {xx_corr:.2f}")
logger.info(f"correlation between xSales and yQuantity = {xy_corr:.2f}")