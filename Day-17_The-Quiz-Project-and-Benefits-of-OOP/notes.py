class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        print(f"{self.username} started following {user.username}")


user_1 = User("001", "adknisely")
user_2 = User("002", "kbknisely")

print(f"User name: {user_1.username} | ID# {user_1.id} | Followers: {user_1.followers} | Following: {user_1.following}")
print(f"User name: {user_2.username} | ID# {user_2.id} | Followers: {user_2.followers} | Following: {user_2.following}")

user_1.follow(user_2)

print(f"User name: {user_1.username} | ID# {user_1.id} | Followers: {user_1.followers} | Following: {user_1.following}")
print(f"User name: {user_2.username} | ID# {user_2.id} | Followers: {user_2.followers} | Following: {user_2.following}")
