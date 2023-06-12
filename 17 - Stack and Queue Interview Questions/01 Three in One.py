class Stack:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack = [0] * (self.number_of_stacks * stack_size)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def is_full(self, stack_number):
        if self.sizes[stack_number] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_number):
        if self.sizes[stack_number] == 0:
            return True
        else:
            return False



    def push(self, value,stack_number):
        if self.is_full(stack_number):
            return "Stack is full"
        else:

