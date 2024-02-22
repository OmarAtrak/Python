class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def toString(self):
        return f"id: {self.id}, username: {self.username}, followers: {self.followers}, following: {self.following}"


user_1 = User("001", "Ahmed")
user_2 = User("002", "Ali")

user_1.follow(user_2)

print(user_1.toString())
print(user_2.toString())
