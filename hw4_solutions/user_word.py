from functools import reduce
listofstrings = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two"]

def count_simba(listofstrings,word): # Function takes a list of strings and counts how many times a certain word appears in the list
    counts_list = list(map(lambda single_string: single_string.count(word), listofstrings)) # Outputs a list of numbers that represent the count of the word in each string
    count = reduce(lambda x,y: x+y, counts_list) # Adds up the numbers in the list produced above
    print(f"The word '{word}' appears {count} times.")

user_word = input("Enter word: ")
count_simba(listofstrings,user_word)