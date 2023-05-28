class Interview_question5:
    '''
    Implement an algorithm to determine if a list has all unique characters using python list.
    '''

    def isUnique(self,lis):
        if len(lis) == 1:
            return True
        elif len(set(lis)) == len(lis):
            return True
        else:
            return False

my_List = [1,2,3,4,5,6,7]

if __name__ == "__main__":
    print(Interview_question5().__doc__)
    print(Interview_question5().isUnique(my_List))