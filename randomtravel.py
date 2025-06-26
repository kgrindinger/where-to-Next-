import random
import os

# --- Load all countries from file ---
all_countries_file = "all_countries.txt"
if not os.path.exists(all_countries_file):
    print(f"Error: '{all_countries_file}' not found.")
    exit()

with open(all_countries_file, "r") as file:
    all_countries = [line.strip() for line in file if line.strip()]

# --- Load visited countries from file ---
visited_file = "visited.txt"
if os.path.exists(visited_file):
    with open(visited_file, "r") as file:
        visited = [line.strip() for line in file if line.strip()]
else:
    visited = []

# --- Show current visited countries ---
if visited:
    print("You've already marked these as visited:")
    print(", ".join(visited))
else:
    print("No countries have been marked as visited yet.")

# --- Add new visited countries ---
new_input = input("Enter any additional countries you've visited (comma-separated), or press Enter to skip: ")
if new_input:
    new_visited = [c.strip() for c in new_input.split(",")]
    for country in new_visited:
        if country and country not in visited:
            visited.append(country)

# --- Save updated visited list ---
with open(visited_file, "w") as file:
    for country in visited:
        file.write(country + "\n")

# --- Normalize for comparison ---
def normalize(lst):
    return [x.lower() for x in lst]

# --- Filter out visited countries from all countries ---
remaining = [country for country in all_countries if country.lower() not in normalize(visited)]

# --- Recommend a destination ---
if remaining:
    next_trip = random.choice(remaining)
    print(f"\nYour next travel destination is: {next_trip}!")
else:
    print("\nYou've visited all the countries in the list. Time to explore beyond!")
