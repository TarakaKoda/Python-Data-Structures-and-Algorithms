class List:
    '''
    Accessing/Traversing the list
    '''

    def accessing_and_traversing(self, list):
        for i in range(len(list)):
            list[i] = f"{list[i]}+"
        return f"After Traversing: {list}"


my_list = ["Milk", "Cheese", "Butter"]

if __name__ == "__main__":
    print(List().__doc__)
    print(f"Original list: {my_list}")
    print(List().accessing_and_traversing(my_list))
