
# 1. For a given person, return their name
def get_name(person1):
    return person1["name"]

# 2. For a given person, return their favourite tv show
def get_favourite_tv_show(person2):
    return person2["favourites"]["tv_show"]

# 3. For a given person, check if they like a particular food
def likes_to_eat(person, meal):
    snacks = person["favourites"]["snacks"]
    # snacks = [ ]
    # meal = "bread"
    # snack first time round the loop = "soup"
    # snack 
    for snack in snacks:
        if meal == snack:
            return True
        
    return False 

# 4. For a given person, add a new name to their list of friends

# put person and name_of_friend as parameters 
# from person --> "friends" key which holds friends name
# use append() to add an item to a list
# put name_of_friend in append()
def add_friend(person, name_of_friend):
    person["friends"].append(name_of_friend)

# 5. For a given person, remove a specific name from their list of friends
# seems similar to adding a friend but instead need to take away a friend
# from person --> "friends" key to access list of friends names
# use remove() and take away index 1
# put the parameters person and name_of_friend
def remove_friend(person, name_of_friend):
    person["friends"].remove("Fred")

