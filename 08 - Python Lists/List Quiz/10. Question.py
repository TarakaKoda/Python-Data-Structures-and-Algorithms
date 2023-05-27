class Lists:
    '''
    What will be the output of the following code snippet?

    A. 22
    B. 21
    C. 0
    D. 43
    '''

    def fruit(self, fruit_list1):
        fruit_list2 = fruit_list1
        fruit_list3 = fruit_list1[:]

        fruit_list2[0] = 'Guava'
        fruit_list3[1] = 'Kiwi'

        sum = 0
        for ls in (fruit_list1, fruit_list2, fruit_list3):
            if ls[0] == 'Guava':
                sum += 1
            if ls[1] == 'Kiwi':
                sum += 20

        print(sum)

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']

if __name__ == "__main__":
    print(Lists().__doc__)
    # Lists().fruit(fruit_list1)