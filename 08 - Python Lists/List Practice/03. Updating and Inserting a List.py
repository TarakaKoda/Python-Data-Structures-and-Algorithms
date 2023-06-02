class List:
    '''
    Updating and Inserting a List
    '''

    def update_insert(self, list):
        print(f"Original List: {list}\n")
        list.insert(4,15)
        print(f"List after inserting: {list}")
        list.append(55)
        print(f"List after appending: {list}")

        new_list = [22,33,44]
        list.extend(new_list)

        return f"LIst after extending: {list}"


my_list = [1,2,3,5,6,7,8,9]

if __name__ == "__main__":
    print(List().__doc__)
    print(List().update_insert(my_list))