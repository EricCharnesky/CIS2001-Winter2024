class PriorityQueue:

    def __init__(self):
        self._data = []

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def _get_left_child_index(self, index):
        return (index * 2) + 1

    def _get_right_child_index(self, index):
        return (index * 2) + 2

    # O( log(n) )
    # moves up the heap until it's no longer less than it's parent
    def _upheap(self, index):
        # index 0 is the top and has no parent
        if index == 0:
            return
        parent_index = self._get_parent_index(index)
        if self._data[index] < self._data[parent_index]:
            temp = self._data[index]
            self._data[index] = self._data[parent_index]
            self._data[parent_index] = temp
            self._upheap(parent_index)

    # moves down the heap until it's no longer greater than it's children
    def _downheap(self, index):
        left_child_index = self._get_left_child_index(index)
        if left_child_index < len(self):
            smallest_child_index = left_child_index
            right_child_index = self._get_right_child_index(index)
            if right_child_index < len(self) and self._data[right_child_index] < self._data[left_child_index]:
                smallest_child_index = right_child_index

            if self._data[index] > self._data[smallest_child_index]:
                temp = self._data[index]
                self._data[index] = self._data[smallest_child_index]
                self._data[smallest_child_index] = temp
                self._downheap(smallest_child_index)

    # O( log(n) )
    def add(self, data):
        self._data.append(data)
        self._upheap(len(self._data) - 1)

    # O(1)
    def min(self):
        # could do custom error if we wanted
        return self._data[0]

    def remove_min(self):
        temp = self._data[0]
        self._data[0] = self._data.pop()
        self._downheap(0)
        return temp

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0
