import random
import os

# Predefined list of all possible travel destinations
all_countries = ["Italy", "Denmark", "Sweden", "Norway", "Germany", "Switzerland"]

# Normalize a country list to lowercase for comparison, but keep original casing for output
def normalize(countries):
    return [c.strip().lower() for c in countries]

# Load visited countries from a file, or start with an empty list
visited_file = "visited.txt"
if os.path.exists(visited_file):
    with open(visited_file, "r") as file:
        visited = [line.strip() for line in file.readlines()]
else:
    visited = []

# Show already visited countries
if visited:
    print("You've already marked these as visited:")
    print(", ".join(visited))
else:
    print("No countries have been marked as visited yet.")

# Let user add more visited countries
new_input = input("Enter any additional countries you've visited (comma-separated), or press Enter to skip: ")
if new_input:
    new_visited = [c.strip() for c in new_input.split(",")]
    # Add only new entries
    for country in new_visited:
        if country and country not in visited:
            visited.append(country)

# Save updated visited list
with open(visited_file, "w") as file:
    for country in visited:
        file.write(country + "\n")

# Remove visited countries from the full destination list (case-insensitive match)
normalized_visited = normalize(visited)
remaining = [country for country in all_countries if country.lower() not in normalized_visited]

# Recommend a new destination
if remaining:
    next_trip = random.choice(remaining)
    print(f"\nYour next travel destination is: {next_trip}!")
else:
    print("\nYou've visited all countries in the list. Time to add more destinations!")

