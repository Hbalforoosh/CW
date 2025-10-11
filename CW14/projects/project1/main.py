
from users import User
from users import Admin
from trips import Trip


# trip1 = Trip(1, "Tehran", "Mashhad", "VIP", 700, 40, "08:00", "17:00", 10)
# trip2 = Trip(2, "Tabriz", "Shiraz", "Normal", 500, 35, "09:00", "18:00", 15)

# print(trip1)
# print(trip2)
# print("----" * 10)


# user1 = User("hossein", "1234", "hossein@gmail.com",
#              "0920827018", balance=2000)
# user1.dashboard()


# user1.buy_ticket(trip1)
# user1.dashboard()


# admin1 = Admin("admin", "admin123")
# admin1.dashboard()


####################################
trip1 = Trip(1, "Tehran", "Mashhad", "VIP", 7000,
             25, "08:00", "17:00", 5, "active")

print(trip1)
print("-" * 50)
trip1.seat_reservation(3)
print(f"Update Capacity after reservation: {trip1.available_seats}")
print("-" * 50)
trip1.cancel(1)
print(f"Update Capacity after canceling the trip: {trip1.available_seats}")
