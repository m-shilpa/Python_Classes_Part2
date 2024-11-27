from datetime import datetime

class Person:
    def __init__(self, first_name,last_name, birth_year):
        self._birth_year = birth_year
        self._first_name = first_name
        self._last_name = last_name
        self._base_salary = 50000
        self._bonus = 10

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self._birth_year

    def set_birth_year(self, birth_year):
        self._birth_year = birth_year

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    @full_name.setter
    def full_name(self, full_name) :
        self._first_name, self._last_name = full_name.split()

    @property
    def salary(self):
        return self._base_salary + (self._base_salary * (self._bonus)/100 )
    
    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, base_salary):
        self._base_salary =base_salary

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, bonus):
        self._bonus = bonus



class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius >0:
            self._radius = radius
            self._area = None
        else:
            raise ValueError

    @property
    def diameter(self):
        return 2* self._radius
    
    @property
    def area(self):
        if self._area is None:
            self._area = 3.14 * self._radius * self._radius
        return self._area
    

class Vehicle:
    vehicle_count= 0

    def __init__(self, name, model, year):
        self._vehicle_name = name
        self._model = model
        self._year = year
        self.__class__.vehicle_count +=1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count
        
    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is a {vehicle_type}"

class ElectricVehicle(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)

    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is an electric {vehicle_type}"

class ValidatedAttribute:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value > 0:
            self._value = value
        else:
            raise ValueError
        

class DynamicClass:
    static_value = 0

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dynamic_attr(self, name, value):
        setattr(self, name, value)
