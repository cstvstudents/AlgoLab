#!/usr/bin/env python3

class PriorityQueue(Exception):
    pass

# ----------------------------------------

# assume elements are passed as couples (elem, priority), where
# priority is an integer such that higher values mean higher priority.
#
class PriorityQueue(object):
    def __init__(self, starting_values=[], max_size=None):
        self.state = []
        self.max_size = max_size

        if starting_values:
            if max_size:
                assert len(starting_values) < max_size, f"Too many starting values given max_size={max_size}"
            
            for elem in starting_values:
                value, priority = elem
                self.insert(value, priority)

    # ---------------------------
    
    def empty(self):
        return len(self.state) == 0

    def size(self):
        return len(self.state)

    # ---------------------------

    def insert(self, value, priority):
        if self.max_size and len(self.state) == self.max_size:
            raise PriorityQueue("priority_queue: queue has reached limit")

        self.state.append((value, priority))

    # ---------------------------

    def pull(self):
        """Returns the elements with highest priority and removes it from the queue"""
        highest_elem = self.peek()

        if highest_elem != None:
            self.state.remove(highest_elem)

        return highest_elem

    def peek(self):
        """Returns the elements with highest priority without removing it from the queue"""

        if self.empty():
            return None
        
        highest_value, highest_priority = self.state[0]

        for elem in self.state[1:]:
            value, priority = elem

            if priority > highest_priority:
                highest_value = value
                highest_priority = priority

        return (highest_value, highest_priority)

    # ---------------------------

    def __str__(self):
        result = ""
        
        result += f"Priority queue {hex(id(self))} "
        result += "{\n"
        result += "\t VALUE, PRIORITY\n"
        for elem in reversed(self.state):
            value, priority = elem
            result += f"\t {value}, {priority}\n" 
        result += "}"

        return result

# ----------------------------------------

# TODO: implement these

def test_priority_queue_1(self):
    pass

def test_priority_queue_2(self):
    pass

# ----------------------------------------

if __name__ == "__main__":
    s = PriorityQueue()

    s.insert(10, 5)
    s.insert(2, 3)

    print(s)
    print(s.peek())
    print(s.pull())
    print(s)    
