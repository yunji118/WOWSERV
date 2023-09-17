class stack :
    def __init__(self) :
        self.items = []

    def push(self, item) : #1
        return self.items.append(item)

    def pop(self) : #2
        return self.items.pop()

    def length(self) : #3
        return len(self.items)

    def isEmpty(self) : #4
        if len(self.items) == 0 :
            return 1
        else :
            return 0

    def peek(self) : #5
        return self.items[-1]

N = int(input())
stack = stack()

for i in range (N) :
    o = int(input())
    if o == 1 :
        s = int(input())
        stack.push(s)
    elif o == 2 :
        if len(stack.items) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif o == 3 :
        print(stack.length())
    elif o == 4 :
        print(stack.isEmpty())
    elif o == 5 :
        if len(stack.items) == 0 :
            print(-1)
        else :
            print(stack.peek())