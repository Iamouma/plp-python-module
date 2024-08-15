def get_user_info():
    # Ask user for their name
    name = input("Please enter your name: ")
    
    # Ask the user for their age
    age = input("Please enter age: ")
    
    # Ask the user for their location
    location = input("Please enter location: ")
    
    # Print a persoanlized meassage using the users name, age and location
    print(f"Hello {name}, you are {age} years old and live in {location}.")