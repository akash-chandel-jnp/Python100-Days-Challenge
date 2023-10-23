'''You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

Example Input
Brazil
5
["Sao Paulo", "Rio de Janeiro"]
Example Output
I've been to Brazil 5 times.
My favourite city was Sao Paulo.
Hint
Look at the function call above to see what the name of the function should be.

The inputs for the function are positional arguments. The order is very important.

Feel free to choose your own parameter names.'''

# TODO 1 - create a function that takes 3 inputs , country name comma separated (convert into list) and favourite city
country = input("Add country name\n") # Add country name
visits = int(input("Number of visits\n")) # Number of visits
list_of_cities = eval(input("create list from formatted string\n")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country_name , no_of_visits, list_of_cities):
    # travel_log.append({"country": country_name, "visits" : no_of_visits ,"cities" : list_of_cities})
    #                                   OR
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = no_of_visits
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)



# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")