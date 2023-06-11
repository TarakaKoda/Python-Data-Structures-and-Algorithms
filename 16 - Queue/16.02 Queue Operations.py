class Queue:
    '''
    List of Queue Operations:
    1. create_queue()
    2. enqueue()
    3. dequeue()
    4. peek()
    5. isEmpty()
    6. isFull()
    7. delete_queue()

    QUEUE OPERATIONS:

    1. create_queue(): To create a Queue, we just need to initialize an empty list or en empty linked list inside a
                       queue class without any elements.


    2. enqueue(): As we have an empty queue we need to perform enqueue operations to add elements into queue. In the world of
               queue when we say enqueue it means insert method, similarly when we use dequeue it basically means removing an
               element.

       custom_queue = [] 
       custom_queue.enqueue(5) -> custom_queue = [5]
       custom_queue.enqueue(4) -> custom_queue = [5,4]
       custom_queue.enqueue(3) -> custom_queue = [5,4,3]
       custom_queue.enqueue(2) -> custom_queue = [5,4,3,2]
       custom_queue.enqueue(1) -> custom_queue = [5,4,3,2,1]
       
       After enqueue():  custom_queue = [5,4,3,2,1]

    3. dequeue(): As we already said in  the world of queue dequeue refers to removing of elements from the queue.
              When we use dequeue() it will remove and return the first inserted or the present first element in a queue.

       custom_queue = [5,4,3,2,1] 
       custom_queue.dequeue() -> custom_queue = [4,3,2,1] removes and returns 5
       custom_queue.dequeue() -> custom_queue = [3,2,1] removes and returns 4
       custom_queue.dequeue() -> custom_queue = [2,1] removes and returns 3
       custom_queue.dequeue() -> custom_queue = [1] removes and returns 2
       custom_queue.dequeue() -> custom_queue = [] removes and return 1
       custom_queue.dequeue() -> As is is an empty queue it will raise an error 

       After dequeue():  custom_queue = []

       Note: If we perform a dequeue operation on an empty queue it will raise an error saying the queue is empty.


    4. peek(): This method is similar to the dequeue method but the only difference is we only get access to the first element
               but it won't remove that element like dequeue. Basically it will return the first element without deleting it.
       
       custom_queue = [5,4,3,2,1] 
       custom_queue.peek() -> returns 5
       custom_queue.dequeue() -> custom_queue = [4,3,2,1] removes and returns 5
       custom_queue.peek() -> custom_queue = [4,3,3,1] returns 4
       custom_queue.dequeue() -> custom_queue = [3,2,1] removes and returns 4
       custom_queue.peek() -> custom_queue = [] returns 3



    5. is_empty(): This method is usually used inside another method to check if the queue is empty of not.
                   This method will return Boolean value (True/False). If any element exist in the queue it will return
                   False otherwise it will return True (In the case of empty queue)
        Example:
                custom_queue = [1,2,3,4]
                custom_queue.is_empty()
                # False

    6. is_full(): In some programming languages when we create a queue based on an array we need to specify the size of
                  array. That means the size of the queue is limited. But when it comes to python we don't need to specify
                  the size of list. In python if we specifically created a queue with size limited we need this method.

    7. delete(): The deletion of an entire queue we just need to set the list to an empty list. In this case all the queue
                 elements will be deleted.
    '''


if __name__ == "__main__":
    print(Queue().__doc__)