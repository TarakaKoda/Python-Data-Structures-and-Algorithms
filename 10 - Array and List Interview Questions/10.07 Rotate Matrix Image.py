class Interview_question7:
    '''
    Given an image represented by an N*N matrix write a program to rotate the image by 90 degrees
    '''

    def rotate_matrix(self, matrix):
        '''rotates a matrix 90 degrees clockwise'''
        n = len(matrix)
        for layer in range(n // 2):
            first, last = layer, n - layer - 1
            for i in range(first, last):
                # save top
                top = matrix[layer][i]

                # left -> top
                matrix[layer][i] = matrix[-i - 1][layer]

                # bottom -> left
                matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

                # right -> bottom
                matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

                # top -> right
                matrix[i][- layer - 1] = top
        return matrix

matrix = [[1, 2], [3, 4]]

if __name__ == "__main__":
    print(Interview_question7().__doc__)
    print(matrix)
    print(Interview_question7().rotate_matrix(matrix))