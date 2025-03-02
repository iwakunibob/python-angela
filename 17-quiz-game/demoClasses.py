class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name

    def change_name(self, new_name):
        self.name = new_name
    
    def print_user(self):
        print(f"User ID = {self.id} {self.name}")


user_1 = User("001", "Angela")
user_2 = User("002","Janice")
user_3 = User("003", "Bob")
user_1.print_user()
user_2.print_user()
user_3.print_user()


# def function():
#     pass  can be used to avoid a syntax check

# print("hello") 