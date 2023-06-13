# Stack of Plates
class Stack_Plates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def push(self, value):
        if len(self.stacks) > 0 and (len(self.stacks[-1]) < self.capacity):
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stack_number):
        if len(self.stacks) > stack_number:
            if len(self.stacks[stack_number]) > 0:
                return self.stacks[stack_number].pop()
            else:
                return None

stack = Stack_Plates(3)

if __name__ == "__main__":
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    print(stack.pop_at(1))
    print(stack)