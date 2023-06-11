class Queue:
    '''
 -------------------------------------------------------------------------------------------------------------------------------
                            List No Capacity Limit           List With Capacity Limit                   Linked List
 -------------------------------------------------------------------------------------------------------------------------------
    Operation         Time Complexity  Space Complexity   Time Complexity  Space Complexity   Time Complexity  Space Complexity
 -------------------------------------------------------------------------------------------------------------------------------
 Create a Queue            O(1)              O(1)                O(1)            O(N)              O(1)             O(1)
 Enqueue                   O(N)              O(1)                O(1)            O(1)              O(1)             O(1)
 Dequeue                   O(N)              O(1)                O(1)            O(1)              O(1)             O(1)
 Peek                      O(1)              O(1)                O(1)            O(1)              O(1)             O(1)
 is_empty                  O(1)              O(1)                O(1)            O(1)              O(1)             O(1)
 is_full                    -                 -                  O(1)            O(1)               -                -
 Delete Entire Queue       O(1)              O(1)                O(1)            O(1)              O(1)             O(1)
    '''


if __name__ == "__main__":
    print(Queue().__doc__)