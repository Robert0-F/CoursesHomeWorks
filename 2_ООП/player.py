
from variants import Variants


class Player:


    def __init__(self, Variants=Variants.ROCK, name='Bot'):
        self.Variants = Variants
        self.name = name


    def whoWins(self, user_1, user_2):
        user1 =  user_1.Variants.value
        user2 = user_2.Variants.value

        if user1 == 2 and user2 == 1 or user1 == 3 and user2 == 2 or user1 == 1 and user2 == 3:
            return f'Победил {user_1.name}'
        elif user1 ==user2:
            return 'Ничья'
        else:
            return f'Победил {user_2.name}'