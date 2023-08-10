# Sort then Process

# Time complexity is O(n * m)
# where n is number of pets and m is number of requests for adoption
# the function loops through all pets for each adoption request 

# Space Complexity is O(n)
# The total amount of data stored is dependent on the number of pets that are passed in initially

# This took me 26 min
shelter = []

initial_pets = [
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1)
]

for name, species, days in initial_pets:
    shelter.append({"name": name, "species": species, "days": days})

def process_adoption(shelter, species):
    adoptable_pets = [pet for pet in shelter if pet["species"] == species]
    if adoptable_pets:
        oldest_pet = min(adoptable_pets, key=lambda pet: pet["days"])
        shelter.remove(oldest_pet)
        return oldest_pet
    else:
        other_species = "dog" if species == "cat" else "cat"
        other_pets = [pet for pet in shelter if pet["species"] == other_species]
        oldest_pet = min(other_pets, key=lambda pet: pet["days"])
        shelter.remove(oldest_pet)
        return oldest_pet

def main():
    while True:
        input_data = input().split(', ')
        
        if input_data[1] == 'person':
            name, _, species = input_data
            adopted_pet = process_adoption(shelter, species)
            if adopted_pet:
                print(f"{adopted_pet['name']}, {adopted_pet['species']}")
        else:
            name, species, days = input_data
            days_in_shelter = int(days.split()[0])
            new_pet = {"name": name, "species": species, "days": days_in_shelter}
            shelter.append(new_pet)

if __name__ == "__main__":
    main()
