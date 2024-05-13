"""

A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

Below are a pair of functions converting l/100km into mpg, and vice versa.

1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.


"""

def liters_100km_to_miles_gallon(liters):
    gallon = liters / 3.785411784
    miles = (100 * 1000) / 1609.344
    return miles/gallon
def miles_gallon_to_liters_100km(miles):
    litres = 3.785411784
    kilometers = (miles * 1609.344) / (1000 * 100)
    return litres/kilometers

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

