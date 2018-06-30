cars = 100.0
#no. of cars present

space_in_a_car = 4.0
#Space that can be occupied by max. no of passengers in a single car

drivers = 30.0
#no. of drivers present

Passengers = 90.0
#no. of passengers present

cars_driven = 30.0
#as trhe no. of passengers are 30 therefore only 30 cars can be driven.....

cars_not_driven = cars - drivers
#cars that cannot be driven

car_pool_capacity = cars_driven * space_in_a_car
#total passengers that all the cars can take.

average_passengers_per_car = Passengers / cars_drivers
#No. of passenger in a single car


print "There are only",cars,"cars available."
print "There are only",drivers,"are available."
print "there wil be",cars_not_driven,"cars empty today."
print "we can transport",car_pool_capacity,"people today."
print "we have",Passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"passengers in each car."
