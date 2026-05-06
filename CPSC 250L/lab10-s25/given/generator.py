# With help from ChatGPT
import os
import random

# Data to use for random generation
first_names = ["Leo", "Bella", "Max", "Luna", "Charlie", "Milo", "Simba", "Oscar", "Daisy", "Ruby"]
middle_names = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.", "J.", ""]
last_names = [
    "Kim", "Ali", "Reed", "Nguyen", "Sato",
    "Singh", "Brooks", "Morgan", "Patel", "Harrison",
    "Ramirez", "Carter", "Khan", "Chen", "Diaz",
    "Wells", "Riley", "Bailey", "Cooper", "Parker"
]

additional_last_names = [
    "Hunter", "Garcia", "Blake", "Lopez", "Kennedy",
    "Mason", "Morales", "Hudson", "Matsumoto", "Ibrahim",
    "Griffin", "Spencer", "Jordan", "Hernandez", "Rossi",
    "Choi", "Gupta", "West", "Jiang", "Hayes"
]

species_list = {
    "Mammal": ["Panthera leo", "Panthera tigris", "Elephas maximus", "Macropus giganteus", "Giraffa camelopardalis"],
    "Bird": ["Haliaeetus leucocephalus", "Aptenodytes forsteri", "Falco peregrinus", "Ara macao", "Pelecanus onocrotalus"],
    "Reptile": ["Pythonidae", "Crocodylus porosus", "Chamaeleo calyptratus", "Varanus komodoensis", "Testudines"]
}
diets = ["Carnivore", "Herbivore", "Omnivore"]
regions = ["Rainforest", "Savannah", "Desert", "Mountain", "Wetlands"]
wing_spans = [1.5, 2.0, 2.5, 3.0, 4.0]

# Set the percentage of bogus data
bogus_percentage = 20  # Adjust this value as needed
total_entries = 250

def generate_animal_data(bogus=False):
    animal_type = random.choice(["Mammal", "Bird", "Reptile"])
    first_name = random.choice(first_names)
    middle_name = random.choice(middle_names)
    last_name = f"{random.choice(last_names)}-{random.choice(additional_last_names)}"
    species = random.choice(species_list[animal_type])

    age = random.randint(1, 20)

    if animal_type == "Mammal":
        extra_data = random.choice(diets)
    elif animal_type == "Bird":
        extra_data = random.choice(wing_spans)
    else:
        extra_data = random.choice(regions)

    # Create bogus data if specified
    if bogus:
        if random.choice([True, False]):
            age = "unknown" if random.choice([True, False]) else random.randint(-10, 0)  # Invalid age
        else:
            # Missing or invalid extra data
            if random.choice([True, False]):
                # Missing extra data
                return f"{animal_type}\t{last_name}\t{first_name}\t{middle_name}\t{species}\t{age}"
            else:
                extra_data = random.choice(["N/A", "invalid"])

    return f"{animal_type}\t{last_name}\t{first_name}\t{middle_name}\t{species}\t{age}\t{extra_data}"

# Generate 100 animals with specified percentage of bogus data
bogus_count = int(total_entries * (bogus_percentage / 100))
animals = [generate_animal_data(bogus=(i < bogus_count)) for i in range(total_entries)]
random.shuffle(animals)

# Save to file
file_path = os.path.join("data", f"zoo_{total_entries}_{bogus_percentage}.txt")
with open(file_path, "w", encoding='utf8', newline='') as f:
    f.write("\n".join(animals))

print(f"Generated {total_entries} animals with {bogus_percentage}% bogus data and saved to zoo.txt")
