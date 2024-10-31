# %%
from functools import reduce

def count_simba(listofstrings,word): # Function takes a list of strings and counts how many times a certain word appears in the list\n",
    counts_list = list(map(lambda single_string: single_string.count(word), listofstrings)) # Outputs a list of numbers that represent the count of the word in each string\n",
    count = reduce(lambda x,y: x+y, counts_list) # Adds up the numbers in the list produced above\n",
    return count
    #user_word = input(\"Enter word: \") #This line will run in a .py file, but need to change "Simba" in next line to user_word

# %%

def get_day_month_year(dates):
    day_month_year = list(map(lambda dmy: {'day': dmy.day, 'month': dmy.month, 'year': dmy.year}, dates)) # Use map to extract the day, month, and year from each date in the list
    day_month_year_list = reduce(lambda acc, x: acc + [x], day_month_year, []) # Reduce the mapped results to a list of dictionaries
    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(day_month_year)
    dates = date_list
    return df

# %%
import geopy
from geopy.distance import geodesic

# To calculate the distance of two points we can use "geodesic" or "great_circle". We are going to use the first one:
def compute_distance(pairs):
    # We use lambda to calculate the distance between each pair of coord (in this case, coords[0] and coords[1]). 
    # "map" applies this lambda to each element of "pairs". 
    # The result is an iterable with the distances, which we then convert to a list.
    return list(map(lambda coords: geodesic(coords[0], coords[1]).kilometers, pairs))

pairs = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
dist_km = compute_distance(pairs)
dist_km

# %% [markdown]
# ### Exercise 4:
# Consider a list that each element can be an integer or a list that contains integers or more lists with integers example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. Create a recursive function called "sum_general_int_list" that takes as input this type of list and returns the sum of all the integers within the lists for instance for list_1=[[2], 3, [[1,2],5]] the result should be 13.

# %%
def sum_general_int_list(list_ex):
    # We use lambda and isistance to check if an element "x" is a list or an integer:
     # a) If "x" is a list, the function makes a recursive call to sum_general_int_list(x) to decompose that list and sum its elements.
     # b) If "x" is an integer, lambda returns the value of "x" and adds it.
    # "map" applies this lambda to each element of "list". 
    # The result is the sum of all the elements.
    return sum(map(lambda x: sum_general_int_list(x) if isinstance(x, list) else x, list_ex))

list_ex = [[2], 3, [[1, 2], 5]]
result = sum_general_int_list(list_ex)
result
