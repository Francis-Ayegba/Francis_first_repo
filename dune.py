"""Object-oriented programming demonstration.

The example shows the main OOP characteristics:
abstraction, encapsulation, inheritance, and polymorphism.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
	"""Abstraction: define a common interface for all vehicles."""

	def __init__(self, brand: str) -> None:
		self.brand = brand
		self.__speed = 0  # Encapsulation: private implementation detail.

	@property
	def speed(self) -> int:
		return self.__speed

	def accelerate(self, amount: int) -> None:
		if amount < 0:
			raise ValueError("amount must not be negative")
		self.__speed += amount

	@abstractmethod
	def move(self) -> str:
		"""Each subclass provides its own implementation."""


class Car(Vehicle):
	"""Inheritance: Car reuses and extends Vehicle."""

	def move(self) -> str:
		return f"{self.brand} car drives at {self.speed} km/h"


class Boat(Vehicle):
	"""Inheritance with a different behavior."""

	def move(self) -> str:
		return f"{self.brand} boat sails at {self.speed} knots"


def show_vehicle(vehicle: Vehicle) -> None:
	"""Polymorphism: the same call works for different vehicle types."""
	vehicle.accelerate(50)
	print(vehicle.move())


if __name__ == "__main__":
	# Objects are instances of classes; composition can be added through
	# objects containing other objects when a larger model is needed.
	vehicles = [Car("Toyota"), Boat("Yamaha")]
	for vehicle in vehicles:
		show_vehicle(vehicle)
