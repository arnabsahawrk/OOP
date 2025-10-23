from abc import ABC, abstractmethod
from time import sleep

from ride import RideMatching, RideRequest


class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid, current_location, wallet) -> None:
        super().__init__(name, email, nid)
        self.current_ride = None
        self.current_location = current_location
        self.wallet = wallet

    def display_profile(self):
        print(f"Rider Name: {self.name}, Email: {self.email}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
            print(f"{amount} tk added to the wallet. Total: {self.wallet} tk")
        else:
            print("Invalid amount.")

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(rider=self, end_location=destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(
            ride_request=ride_request, vehicle_type=vehicle_type
        )

        if ride:
            ride.set_rider(self)
            self.current_ride = ride

    def show_current_ride(self):
        if self.current_ride and self.current_ride.driver:
            print("Ride Details!!")
            print(f"Rider: {self.name}")
            print(f"Driver: {self.current_ride.driver.name}")
            print(f"Selected Vehicle:{self.current_ride.vehicle.vehicle_type}")
            print(f"Start Location: {self.current_ride.start_location}")
            print(f"End Location: {self.current_ride.end_location}")
            print(f"Started Time: {self.current_ride.start_time}")
            print(f"End Time: {self.current_ride.end_time}")
            print(f"Total Cost: {self.current_ride.estimated_fare}")
        else:
            print("No current ride found. Please request a ride first.")


class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f"Driver Name: {self.name}, Email: {self.email}")

    def accept_ride(self, ride):
        ride.set_driver(self)

    def reach_destination(self, ride):
        sleep(2)
        ride.end_ride()
