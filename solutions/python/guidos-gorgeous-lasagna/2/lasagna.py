"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
#PREPARATION_TIME = 0
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME-elapsed_bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    Parameters:
        number_of_layers (int): The number of layers added.

    Returns:
        int: The preparation time (in minutes) derived from 'number_of_layers*2'.

    Function that takes the number of layers the lasagna has, as
    an argument and returns how many minutes it would take to prepare
    based on the average time per layer (2).
    
    """
    return number_of_layers*2

#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    Parameters:
        number_of_layers (int): The number of layers the lasagna has.
        elapsed_bake_time: The time the lasagna has already spent in the oven

    Returns:
        int: The elapsed time (in minutes) derived from PREPARATION_TIME plus elapsed_bake_time.

    Function that takes the preparation time for the lasagna and the elapsed bake time as arguments and returns how many minutes the lasagna has spent baking.
    
    """
    PREPARATION_TIME = preparation_time_in_minutes(number_of_layers)

    return PREPARATION_TIME+elapsed_bake_time

    

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
