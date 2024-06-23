from module43 import Vehicle 
from module44 import Driver # type: ignore
from module46 import Customer # type: ignore
from module47 import Ride # type: ignore

# Driver Application
driver = Driver()
driver.add_driver_details()

# Customer Application
customer = Customer()
customer.add_customer_details()

# Server
ride = Ride()
ride.add_ride_details()
ride.link_customer(customer)
ride.link_driver(driver)

print("Ride booked...")
ride.show()