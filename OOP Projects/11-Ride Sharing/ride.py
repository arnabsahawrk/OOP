from datetime import datetime
from random import randint
from time import sleep

from vehicle import CNG, Bike, Car


class RideSharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f"""Company Name: {self.company_name}
Total Riders: {len(self.riders)}
Total Drivers: {len(self.drivers)}
"""


class Ride:
    def __init__(self, start_location, end_location, vehicle) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.estimated_fare = self.calculate_fare(vehicle=vehicle.vehicle_type)
        self.vehicle = vehicle

    def set_driver(self, driver):
        self.driver = driver

    def set_rider(self, rider):
        self.rider = rider

    def end_ride(self):
        if self.rider and self.driver and self.estimated_fare:
            self.rider.wallet -= self.estimated_fare
            self.driver.wallet += self.estimated_fare
            print(f"Ride ended. Fare {self.estimated_fare} tk transferred.")

    def calculate_fare(self, vehicle):
        fare_per_km = {"car": 50, "bike": 30, "cng": 20}
        return randint(1, 20) * fare_per_km.get(vehicle.lower(), 0)

    def __repr__(self) -> str:
        return f"started {self.start_location} to {self.end_location}"


class RideRequest:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class RideMatching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, ride_request, vehicle_type):
        if len(self.available_drivers) > 0:
            print("Looking for drivers....")

            sleep(1)
            x = randint(0, len(self.available_drivers) - 1)
            driver = self.available_drivers[x]

            if vehicle_type.lower() == "car":
                vehicle = Car("Car", "AB343", 550)
            elif vehicle_type.lower() == "bike":
                vehicle = Bike("Bike", "CC3434", 250)
            elif vehicle_type.lower() == "cng":
                vehicle = CNG("CNG", "GG343", 190)
            else:
                return

            ride = Ride(
                start_location=ride_request.rider.current_location,
                end_location=ride_request.end_location,
                vehicle=vehicle,
            )
            driver.accept_ride(ride)
            return ride
