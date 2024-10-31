# %%
def count_simba(listofstrings,word): # Function takes a list of strings and counts how many times a certain word appears in the list\n",
    counts_list = list(map(lambda single_string: single_string.count(word), listofstrings)) # Outputs a list of numbers that represent the count of the word in each string\n",
    count = reduce(lambda x,y: x+y, counts_list) # Adds up the numbers in the list produced above\n",
    print(f"The word '{word}' appears {count} times.")
    #user_word = input(\"Enter word: \") #This line will run in a .py file, but need to change "Simba" in next line to user_word

# %%

def get_day_month_year(dates):
    day_month_year = list(map(lambda dmy: {'day': dmy.day, 'month': dmy.month, 'year': dmy.year}, dates)) # Use map to extract the day, month, and year from each date in the list
    day_month_year_list = reduce(lambda acc, x: acc + [x], day_month_year, []) # Reduce the mapped results to a list of dictionaries
    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(day_month_year)
    dates = date_list
    return df


