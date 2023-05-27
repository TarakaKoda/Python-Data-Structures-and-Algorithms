class Lists:
    '''
    What is the correct command to shuffle the following list?

    A. fruit.shuffle()
    B. shuffle(fruit)
    C. random.shuffle(fruit)
    D. random.shuffleList(fruit)
    '''

    def fruits(self):
        fruit = ['apple', 'banana', 'papaya', 'cherry']
        print(fruit)

if __name__ == "__main__":
    print(Lists().__doc__)
    Lists().fruits()