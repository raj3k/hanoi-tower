class Board:
    def __init__(self):
        self.list_of_towers = []
        

    def list_towers(self):
        for tower in self.list_of_towers:
            print(tower.stack)

        

class Tower():
    def __init__(self, tower_num):
        self.tower_num = tower_num
        self.stack = []

    def add_to_tower(self, disk):
# Use list append method to add element
        if disk not in self.stack:
            self.stack.append(disk)
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):
        if not self.stack:
            return self.stack
        else:     
	        return self.stack[-1]

    def remove_from_tower(self):
        if len(self.stack) <= 0:
            print("Stack is empty")
        else:
            return self.stack.pop()


class Disk:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f"disk of size {self.size}"

