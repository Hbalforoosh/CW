from projects.project1.requerments import validate


class Trip:
    def __init__(
        self,
        trip_id,
        origin,
        destination,
        bus_type,
        price,
        capacity,
        start_time,
        end_time,
        available_seats,
        trip_status="active",
    ) -> None:
        """Attributes Defining"""
        self.trip_id = trip_id
        self.origin = origin
        self.destination = destination
        self.bus_type = bus_type
        self.price = price
        self.capacity = capacity
        self.start_time = start_time
        self.end_time = end_time
        self.available_seats = available_seats
        self.status = trip_status

        """Validation"""
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number.")
        if available_seats is None:
            available_seats = capacity
        validate.validate_trip_id(trip_id)
        validate.validate_city(origin)
        validate.validate_city(destination)
        validate.validate_origin_destination(origin, destination)
        validate.validate_trip_times(start_time, end_time)
        validate.validate_price(price)

    def seat_reservation(self, count=1):
        if self.available_seats < count:
            raise ValueError("All seats are complete.")
        self.available_seats -= count

    def cancel(self, count=1):
        if self.available_seats + count > self.capacity:
            raise ValueError("The number of seats exceeds capacity.")
        self.available_seats += count

    def __str__(self):
        return (
            f"{self.origin} to {self.destination} | {self.start_time}-{self.end_time} | "
            f"{self.price} $ | {self.bus_type} | Capacity: {self.available_seats}/{self.capacity}"
        )
