class Vehicle:
    def __init__(self, vehicle_id: str):
        self._vehicle_id = vehicle_id
        self._is_rented = False

    def rent(self) -> None:
        if not self._is_rented:
            self._is_rented = True

    def return_vehicle(self) -> None:
        self._is_rented = False

    def get_id(self) -> str:
        return self._vehicle_id

    def is_rented(self):
        return self._is_rented

    def __str__(self) -> str:
        return self._vehicle_id


class Car(Vehicle):
    def __init__(
        self,
        vehicle_id,
        model,
        fuel_type,
    ):
        self._model = model
        self._fuel_type = fuel_type
        super().__init__(vehicle_id)

    def __str__(self) -> str:
        return f"{self._model}, {self._vehicle_id}"


# TODO: реалиовать этот класс
class Bike:
    def __init__(self, type: str):
        self._type = type

    # TODO: реалиовать этот метод
    def __str__(self):
        pass


class RentalService:
    def __init__(self):
        self._inventory: list[Vehicle] = []

    def add_vehicles(self, vehicle: Vehicle) -> None:
        self._inventory.append(vehicle)

    def show_available_vehicles(self) -> None:
        for vehicle in self._inventory:
            if not vehicle.is_rented():
                print(vehicle)

    # TODO: реалиовать этот метод
    def rent_vehicle(vehicle: Vehicle):
        pass

    # TODO: реалиовать этот метод
    def return_vehicle(vehicle: Vehicle):
        pass


rental_service = RentalService()

audi = Car(vehicle_id="1", model="Audi", fuel_type="Бензин")

rental_service.add_vehicles(audi)
rental_service.show_available_vehicles()

rental_service.rent_vehicle(audi)

rental_service.return_vehicle(audi)

rental_service.show_available_vehicles()
