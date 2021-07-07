time = int(input("Time: "))
accel = int(input("Accel: "))
dist = int(input("Dist. Driven: "))
duration = 0

print()

#some graph

speed = accel * time

while duration <= time:
    print("duration", duration,"distance: ", "*" * int(0.5 * 0.1 * accel * duration * duration))
    duration = duration + 1

print()

#DESTINATION CHECK

distancereached = 0.5 * accel * time * time

if dist <= distancereached:
    print("DESTINATION REACHED (REACHED: ", distancereached, "m)")
if dist > distancereached:
    print("UM... I HOPE YOU FIND YOUR WAY (REACHED: ", distancereached, "m)")

#SPEED TEST

if speed <= 60:
    print("Normal Speed (YOUR SPEED IS: ",speed, "m/s)")

if speed > 60:
    print("OVERSPEED! SLOW DOWN! (YOUR SPEED IS: ",speed, "m/s --- MAX SPEED IS 60m/s)")


