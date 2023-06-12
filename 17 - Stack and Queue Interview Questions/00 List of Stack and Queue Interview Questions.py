class Stack_and_Queue:
    '''
    01. Describe how you could use a single python list to implement three stacks
    02. How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
        push, pop and min should all operate in O(1)
    03. Imagine a (Literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would
        likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStack that mimics this.
        SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity,
        SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return
        the same values as it would if there were just a single stack)
        follow up:
        Implement a function popAt (int index) which performs a pop operation on a specific substack.
    04. Implement a queue using two stacks.
    05. Sort a stack with the smallest on top using only a single temporary stack.
    06. Implement a cat and dog queue for an animal shelter.
    '''

if __name__ == "__main__":
    print(Stack_and_Queue().__doc__)