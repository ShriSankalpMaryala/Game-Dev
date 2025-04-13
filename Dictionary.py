import pygame

world_capitals = {
    "Indonesia" : "Jakarta",
    "Sweden" : "Stockholm",
    "Australia" : "Canberra",
    "Mexico" : "Mexico City",
    "India" : "New Delhi",
    
}
world_capitals["Latvia"]="Riga"
print(world_capitals)

if "India" in world_capitals:
    print(world_capitals["India"])

if "Rwanda" in world_capitals:
    print(world_capitals["Rwanda"])

for key in world_capitals.keys():
    print(world_capitals[key])

for value in world_capitals.values():
    print(value)

print(len(world_capitals))

del world_capitals["Latvia"]
print(world_capitals)