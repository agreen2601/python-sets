# Showroom
# 1
showroom = set()

# 2
showroom.update(["car", "van", 'bus', 'plane'])

# 3
print(len(showroom))

# 4
showroom.add('bus')

# 5
print(showroom)

# 6
showroom.update(("boat", "tank"))
print(showroom)

# 7
showroom.discard("car")
print(showroom)


# Acquiring more cars
# 1
junkyard = {"boat", "plane", "spaceship", "UFO", "jet", "car"}

# 2
print(junkyard.intersection(showroom))

# 3
combined = junkyard.union(showroom)
print(f"combined {combined}")

# 4
combined.discard('van')
print(f"got rid of the van {combined}")