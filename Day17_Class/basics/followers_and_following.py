class Twitter_user:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1  # now I am following someone
        user.followers += 1


user1 = Twitter_user("Akash", 32)
user2 = Twitter_user("Anurag", 34)

user1.follow(user2)  # user1 now follows user2

print(f"{user1.name} has {user1.followers} followers")
print(f"{user1.name} is following {user1.following} people.")

print(f"{user2.name} has {user2.followers} followers")
print(f"{user2.name} is following {user2.following} people.")
