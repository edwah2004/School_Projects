frictionCoefficient = 0
responseTime = 0
gravity = float(9.81)

speed = int(input ("What is the speed of the vehicle? (mph)\n"))
mpsSpeed = float(speed/2.237)
ask = True

while ask == True:
    condition = int(input ("What was the condition of the road?\n1.Dry\n2.Wet\n3.Icy\n"))
    if condition == 1:
        frictionCoefficient = float(0.7)
        ask = False
    elif condition == 2:
        frictionCoefficient = float(0.5)
        ask = False
    elif condition == 3:
        frictionCoefficient = float(0.3)
        ask = False
    else:
        print ("That was an invalid input.")
        ask = True

age = int(input ("What is the age of the driver?\n"))
responseTime = (age/20)

responseDistance = (mpsSpeed*responseTime)
brakeDistance = ((mpsSpeed**2)/(2*frictionCoefficient*gravity))
totalDistance = (responseDistance + brakeDistance)

responseDistance = round(responseDistance,2)
brakeDistance = round(brakeDistance,2)
totalDistance = round(totalDistance,2)

print ("Response Distance:",responseDistance,"Meters")
print("Braking Distance:",brakeDistance,"Meters")
print("TotalDistance:",totalDistance,"Meters")
