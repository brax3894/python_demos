class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def full_name (self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}, {self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}."

user1 = User("Joe", "Frez", 56)
user2 = User("Henry", "Huerta", 23)
print(user1.first, user1.last)
print(user2.first, user2.last)
print(user2.full_name())
print (user1.likes("Pizza"))