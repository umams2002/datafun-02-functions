'''
44608 Data fundamentals

Project 2

Uma Subramanian
'''

import math as maths
import statistics as stats

from util_logger import setup_logger
logger, logname = setup_logger(__file__)
'''
Calcualte the area of parking lot
'''

def calc_area(length, width):
    area = length * width
    return area

def parking_lot_cost(length,width , cost_per_sq):
    total_area = calc_area(length, width)
    lot_cost = total_area * cost_per_sq
    return lot_cost

print(f"Total area of parking lot where lot A (120,450) is {calc_area(120,450)}")
print(f"Cost of parking lot where lot A (120,450) is  area is  {parking_lot_cost(120,450,1.50)}")


logger.info(f"total area of A (120,450) is {calc_area(120,450)}")


def calculate_circle_area_given_radius(radius):
    """
    Return area of a circle given the radius.

    @param radius: the radius of the circle
    @return: the area of the circle
    @raise Exception: if radius is not a number

    """

    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_circle_area({radius})")

    try: 
        area = 2 * maths.pi * radius
        logger.info(f"The circle area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
'''
Math functions
'''
print(f"Explore some functions in the math module ")
print(f"math.comb(5,1) = {maths.comb(5,1)}")
print(f"math.perm(5,1) = {maths.perm(5,1)}")
print(f"math.acos(0.55) = {maths.acos(0.55)}")
print(f"math.ceil(-5.3) = {maths.ceil(-5.3)}")
print(f"math.exp(-6.89) = {maths.exp(-6.89)}")
logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {maths.comb(5,1)}")
logger.info(f"math.perm(5,1) = {maths.perm(5,1)}")
logger.info(f"math.acos(0.55) = {maths.acos(0.55)}")
logger.info(f"math.ceil(-5.3) = {maths.ceil(-5.3)}")
logger.info(f"math.exp(-6.89) = {maths.exp(-6.89)}")

'''
order_amount = get_order_amount(price_with_tax, quantity)

'''
def get_order_amount(price_with_tax, quantity):
    logger.info(f"function calling get_order_amount(price_with_tax, quantity) is {price_with_tax,quantity} ")
    result = price_with_tax * quantity
    logger.info(f"Return result of get_order_amount(price_with_tax, quantity) is {result}")
    return result
   

print(f"Calculate order amount for OrderNo.1 is (656.45,5) is {get_order_amount(656.45,5)} ")
logger.info(f"Calculate order amount for OrderNo.1 is (656.45,5) is {get_order_amount(656.45,5)} ")


