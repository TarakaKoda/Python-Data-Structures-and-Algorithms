class Stack:
    '''
    List of Stack Operations:
    1. create_stack()
    2. push()
    3. pop()
    4. peek()
    5. isEmpty()
    6. isFull()
    7. deleteStack()

    STACK OPERATIONS:

    1. create_stack(): To create a Stack, we just need to initialize an empty list or en empty linked list inside a
                       stack class without any elements.


    2. push(): As we have an empty stack we need to perform push operations to add elements into stack. In the world of
               stack when we say push it means insert method, similarly when we use pop it basically means removing an
               element.


        custom_stack = []    custom_stack.push(5)        custom_stack.push(3)     custom_stack.push(2)

        Initial Stack               push(5)                    push(3)                  push(2)
        +---+                       +---+                      +---+                    +---+
        |   |                       |   |                      |   |                    |   |
        +---+                       +---+                      +---+                    +---+
        |   |                       |   |                      |   |                    | 2 |
        +---+                       +---+                      +---+                    +---+
        |   |                       |   |                      | 3 |                    | 3 |
        +---+                       +---+                      +---+                    +---+
        |   |                       | 5 |                      | 5 |                    | 5 |
        +---+                       +---+                      +---+                    +---+

       After push():  custom_stack = [5,3,2]

    3. pop(): As we already said in  the world of stack pop refers to removing of elements from the stack.
              When we use pop() it will remove and return the top most element in a stack.

        custom_stack = [5,3,2]    custom_stack.pop()        custom_stack.pop()     custom_stack.pop()

        Initial Stack           pop() -> return 2         pop() -> return 3        pop() -> return 5
        +---+                       +---+                      +---+                    +---+
        |   |                       |   |                      |   |                    |   |
        +---+                       +---+                      +---+                    +---+
        | 2 |                       |   |                      |   |                    |   |
        +---+                       +---+                      +---+                    +---+
        | 3 |                       | 3 |                      |   |                    |   |
        +---+                       +---+                      +---+                    +---+
        | 5 |                       | 5 |                      | 5 |                    |   |
        +---+                       +---+                      +---+                    +---+

       After pop():  custom_stack = []

       Note: If we perform a pop operation on an empty stack it will raise an error saying the stack is empty.


    4. peek(): This method is similar to the pop() method but the only difference is we only get access to the top element
               it won't remove that element like pop(). Basically it will return the top element without deleting it.

        custom_stack = [5,3,2]    custom_stack.peek()      custom_stack.pop()     custom_stack.peek()

        Initial Stack           pop() -> return 2         pop() -> return 2        peek() -> return 3
        +---+                       +---+                      +---+                    +---+
        |   |                       |   |                      |   |                    |   |
        +---+                       +---+                      +---+                    +---+
        | 2 |                       | 2 |                      |   |                    |   |
        +---+                       +---+                      +---+                    +---+
        | 3 |                       | 3 |                      | 3 |                    | 3 |
        +---+                       +---+                      +---+                    +---+
        | 5 |                       | 5 |                      | 5 |                    | 5 |
        +---+                       +---+                      +---+                    +---+

    5. is_empty(): This method is usually used inside another method to check if the stack is empty of not.
                   This method will return Boolean value (True/False). If any element exist in the stack it will return
                   False otherwise it will return True (In the case of empty stack)
        Example:
                custom_stack = [1,2,3,4]
                custom_stack.is_empty()
                # False

    6. is_full(): In some programming languages when we create a stack based on an array we need to specify the size of
                  array. That means the size of the Stack is limited. But when it comes to python we don't need to specify
                  the size of list. In python if we specifically created a stack with sie limited we need this method.

    7. delete(): The deletion of an entire stack we just need to set the list to an empty list. In this case all the stack
                 elements will be deleted.
    '''


if __name__ == "__main__":
    print(Stack().__doc__)