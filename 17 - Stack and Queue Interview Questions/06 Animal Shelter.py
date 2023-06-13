class Animal_Shelter:
    def __init__(self):
        self.cat = []
        self.dog = []

    def __str__(self):
        cat_value = [str(value) for value in self.cat]
        dog_value = [str(value) for value in self.dog]
        return f"{cat_value}\n{dog_value}"

    def enqueue(self, animal, type):
        if type.lower() == "cat":
            self.cat.append(animal)
        else:
            self.dog.append(animal)

    def dequeue_cat(self):
        if len(self.dog) == 0:
            return None
        return self.cat.pop(0)

    def dequeue_dog(self):
        if len(self.dog) == 0:
            return None
        return self.dog.pop(0)

    def dequeue_any(self):
        if len(self.cat) == 0:
            return self.dog.pop(0)
        else:
            return self.cat.pop(0)

animal_shelter = Animal_Shelter()

if __name__ == "__main__":
    animal_shelter.enqueue("cat1", "cat")
    animal_shelter.enqueue("dog1", "dog")
    animal_shelter.enqueue("cat2", "cat")
    print(animal_shelter)
    print(animal_shelter.dequeue_cat())
    print(animal_shelter)
    animal_shelter.enqueue("cat3", "cat")
    print(animal_shelter)
    print(animal_shelter.dequeue_any())
    print(animal_shelter)
