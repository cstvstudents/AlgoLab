#!/usr/bin/env python3

class StackException(Exception):
    pass

# ----------------------------------------

class Stack(object):
    def __init__(self, starting_values=[], max_size=None):
        self.state = []
        self.max_size = max_size
        
        if starting_values:
            if max_size:
                assert len(starting_values) < max_size, f"Too many starting values given max_size={max_size}"
            
            for x in starting_values:
                self.push(x)

    # ---------------------------

    def empty(self):
        """Returns true if the stack is currently empty, false otherwise"""
        return len(self.state) == 0

    def size(self):
        """Returns current size of stack"""
        return len(self.state) 

    # ---------------------------
    
    def push(self, value):
        """Pushes the given value on top of the stack.

        If the object was initialized with a given max_size, it also
        checks if we've reached the maximum size allowed. If we did,
        then we don't push the new item and we throw an exception."""

        if self.max_size and len(self.state) == self.max_size:
            raise StackException("push: stack has reached limit")
        
        self.state.append(value)

    # ---------------------------

    def pop(self):
        """Returns the element currently on top of the stack and pops it off the stack.
        If the stack is empty, None is returned."""

        ret = self.peek()

        if ret != None:
            self.state.pop()

        return ret

    def peek(self):
        """Returns the element currently on top of the stack but DOES NOT pops it off.
        If the stack is empty, None is returned."""

        length = len(self.state)
        
        if length == 0:
            return None

        return self.state[length - 1] 

    # ---------------------------

    def search(self, value):
        """Returns a 0-based index representing the first position in which value is found on the stack.
        If value is not found, -1 is returned instead."""

        for i, elem in enumerate(self.state):
            if elem == value:
                return i

        return -1

    # ---------------------------

    def __str__(self):
        result = ""
        
        result += f"Stack {hex(id(self))} "
        result += "{\n"
        for x in reversed(self.state):
            result += f"\t {x}\n" 
        result += "}"

        return result

# ----------------------------------------

def test_stack_1():
    """Test push, peek, size and search w/o size and initial values"""
    s = Stack()

    # push and peek
    for x in range(0, 15):
        s.push(x)
        assert s.peek() == x, f"[peek() ERROR]: Out={s.peek()}, Excepted={x}"

    # size
    assert s.size() == 15, f"[size() ERROR]: Out={s.size()}, Excepted=15"

    # search
    for i, x in enumerate(range(0, 15)):
        assert s.search(x) == i, f"[search() ERROR]: Out={s.search(x)}, Excepted={i}"

    # pop
    for x in reversed(range(0, 15)):
        popped_value = s.pop()
        assert popped_value == x, f"[pop() ERROR]: Out={popped_value}, Excepted={x}"

    # empty
    assert s.empty() == True, f"[pop() ERROR]: Out={s.empty()}, Excepted=True"

    return True

# def test_stack_2():
#     """Test push, peek, size and search wwith size and initial values"""
#     max_size = 50
#     starting_values = []

#     s = Stack(starting_values=starting_values, max_size=max_size)

#     # TODO: push

#     # TODO: size

#     # TODO: search

#     # TODO: peek and pop

#     # TODO: empty

#     return True

# ----------------------------------------
    
if __name__ == "__main__":
    if test_stack_1():
        print("Test stack 1 passed :D")
