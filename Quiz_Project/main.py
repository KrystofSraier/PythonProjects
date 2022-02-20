class Car:
    def __init__(self, seats, breakes):
        self.seats = seats
        self.breakes = breakes
        self.followers = 0
        self.following = 0

    def change_number_of_followers(self, user):
        user.followers += 1
        self.following += 1


car_1 = Car(5, 6)
car_2 = Car(5,3)


car_1.change_number_of_followers(car_1)

print(car_1.following)
print(car_1.followers)





