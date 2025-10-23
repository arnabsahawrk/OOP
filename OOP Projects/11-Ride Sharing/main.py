from ride import RideSharing
from users import Driver, Rider

faster = RideSharing("Faster")

arnab = Rider("Arnab", "arnab.com", 925343, "Feni", 3000)
jobayer = Rider("Jobayer", "jobayer.com", 342442, "Khilkhet", 1500)
gias_udding = Rider("Gias Uddin", "gias.com", 92442, "Khulana", 2500)

faster.add_rider(arnab)
faster.add_rider(jobayer)
faster.add_rider(gias_udding)

shuvo = Driver("Shuvo", "shuvo.com", 45345, "Bramonbaria")
alamin = Driver("Alamin", "a.com", 4342432, "Feni")
skindar = Driver("Skindar", "sikandar.com", 343432, "Kustia")

faster.add_driver(shuvo)
faster.add_driver(alamin)
faster.add_driver(skindar)

arnab.request_ride(faster, "Dhaka", "car")

arnab.show_current_ride()

shuvo.reach_destination(arnab.current_ride)
# print(faster)
