class Dog:
    species = "Canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 20)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")
dog1.display_info()
dog2.display_info()