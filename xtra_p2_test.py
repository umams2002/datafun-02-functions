import doctest

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


def testcase_calc_parking_lot_cost(length,width , cost_per_sq):
    total_area = calc_area(length, width)
    lot_cost = total_area * cost_per_sq
    return lot_cost

def calc_area(length, width):
    area = length * width
    return area

if __name__ == "__main__":
    testcase_calc_parking_lot_cost(length=145,width=345,cost_per_sq=45.90)
    testcase_calc_parking_lot_cost(length=33.66,width=45.89,cost_per_sq=50)

    logger.info("===========================================================")
    logger.info("Running doctest.testmod() function to unit test our code")
    logger.info("===========================================================")

    # Run doctest and log the results

    doctest_result = doctest.testmod()
    if doctest_result.failed == 0:
        logger.info("All tests passed!")
    else:
        logger.error(f"{doctest_result.failed} tests failed!")

    logger.info("Script complete. More info in the log file.")