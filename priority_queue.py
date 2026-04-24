# Priority Queue with lower integer values having higher priority
class PriorityQueue:
    def __init__(self):
        self._list = []

    def enqueue(self, obj, priority: int):
        for i, (_, other_priority) in enumerate(self._list):
            if other_priority > priority:
                # Inserts new object before another object if the other object has a lower priority
                self._list.insert(i, (obj, priority))
                break
        else:
            # If there are no objs with lower priority insert obj at the back of the list
            self._list.append((obj, priority))

    # Returns obj and it's priority
    def dequeue(self):
        return self._list.pop(0)

    def is_empty(self):
        return len(self._list) == 0

    # For debugging
    def __str__(self):
        s = "["
        for obj, priority in self._list:
            s += f"({obj}, {priority}), "
        s = s[:-2] + "]"
        return s
