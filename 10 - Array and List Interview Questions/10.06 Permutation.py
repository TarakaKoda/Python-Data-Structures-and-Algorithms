class Interview_question6:
    '''
    Permutations
    '''

    def isPermutation(self, str1, str2):
        if len(str1) != len(str2):
            return False
        else:
            if str1.sort() == str2.sort():
                return True
            else:
                return False


if __name__ == "__main__":
    print(Interview_question6().__doc__)
    print(Interview_question6().isPermutation([1, 2, 3], [3, 2, 1]))