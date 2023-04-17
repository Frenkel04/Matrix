class Vehicle:
     way_passed = 0
     def abc (self, fuel_capacity, num_of_wheels, top_speed, fuel_per_km):
         self.fuel_capacity = fuel_capacity
         self.num_of_wheels = num_of_wheels
         self.top_speed = top_speed
         self.fuel_per_km = fuel_per_km
         self.hours = hours
     def xxx(self):
         return f'this vehicle has {self.top_speed} of top speed and {self.fuel_capacity} of fuel'
     def ff(self, hours):
         way_passed = hours * self.top_speed
         if way_passed * self.fuel_per_km > self.fuel_capacity:
           raise ValueError("You don't have enough fuel") 
         self.fuel_capacity -= way_passed * self.fuel_per_km
def main():
    fuel_capacity = float(input())
    num_of_wheels = int(input())
    top_speed = float(input())
    fuel_per_km = float(input())
    hours = int(input())
    way_passed = float
    try:
       Vehicle(fuel_capacity, num_of_wheels, top_speed, fuel_per_km)
    except ValueError as e:
        print(e)
    except:
      print("Wrong data was given")
    try:
      ans = Vehicle.way_passed(hours)
      print(ans)
    except ValueError:
      print("You don't have enough fuel")
    except:
      print("Wrong data was given")
if __name__ == '__main__':
    main()
