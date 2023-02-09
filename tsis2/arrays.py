cars = ["Ford", "Volvo", "BMW"]

print(cars)
cars[0] = "Toyota"
for x in cars:
  print(x)
cars.append("Honda")
cars.pop(1)
cars.remove("Volvo")