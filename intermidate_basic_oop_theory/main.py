class User:
    # This method always be executed when you create the object
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        # Initializing data b y default
        self.followers = 0
        self.following = 0

    # Creating methods
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating an object
user_1 = User("001", "Juan camilo")
user_2 = User("002", "Carlos chacon")
print(user_1.username)
user_1.follow(user_2)
print(user_1.following)




# user_2 = User()
# user_2.id = "0002"
# user_2.username = "Jack"
# print(user_2.username)