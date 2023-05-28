class Interview_question2:
    '''
    write a program to find all pairs of integer whose sum is equal to a given number?
    '''

    # def sumPairs(self, lis, n):
    #     lis.sort()
    #     high = len(lis) - 1
    #     low = 0
    #     while high > low and low < len(lis) and high > 0:
    #         if lis[high] + lis[low] == n:
    #             if (lis[high] != lis[low]):
    #                 print(lis[high], lis[low])
    #             low += 1
    #             high -= 1
    #         elif lis[high] + lis[low] > n:
    #             high -= 1
    #         elif lis[high] + lis[low] < n:
    #             low += 1

    def sumPairs(self, list, sum):
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                if (list[i] + list[j]) == sum:
                    print(list[i], list[j])

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


if __name__ == "__main__":
    print(Interview_question2().__doc__)
    Interview_question2().sumPairs(mylist, 100)