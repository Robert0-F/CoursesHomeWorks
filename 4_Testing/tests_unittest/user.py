class User:
    def __init__(self, name='Bot', age=10, hobbies=None):
        self.name = name
        self.age = age


    def set_hobbies(self, hobbies:str):
        self.hobbies = hobbies.split(',')