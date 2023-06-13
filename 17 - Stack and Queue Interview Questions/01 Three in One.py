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

    def index_of_top(self,  stack_number):
        offset = stack_number * self.stack_size
        return offset + self.sizes[stack_number] -1


    def push(self, value,stack_number):
        if self.is_full(stack_number):
            return "Stack is full"
        else:
            self.sizes[stack_number] += 1
            self.stack[self.index_of_top(stack_number)] = value

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return "Stack is empty"
        else:
            value = self.stack[self.index_of_top(stack_number)]
            self.stack[self.index_of_top(stack_number)] = 0
            return value

    def peek(self, stack_number):
        if self.is_empty(stack_number):
            return "Stack is empty"
        else:
            return self.stack[self.index_of_top(stack_number)]

    def __str__(self):
        # value = self.stack.reverse()
        value = [str(values) for values in self.stack]
        return "\n".join(value)


stack = Stack(3)

stack.push(2,2)
stack.push(1,2)
stack.push(1, 0)
stack.push(2,0)
print(stack.peek(0))
print(stack)


