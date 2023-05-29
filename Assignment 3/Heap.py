class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            raise IndexError("Heap is empty")
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        
        self.sift_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            raise IndexError("Heap is empty")
        self.swap(0, len(self.arr) - 1)
        self.arr.pop()
        self.sift_down(0)

    def sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.arr[index] >= self.arr[parent_index]:
                break
            self.swap(index, parent_index)
            index = parent_index

    def sift_down(self, index):
        size = len(self.arr)
        while index < size:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_child_index = index

            if (left_child_index < size
                    and self.arr[left_child_index] < self.arr[smallest_child_index]):
                smallest_child_index = left_child_index

            if (right_child_index < size
                    and self.arr[right_child_index] < self.arr[smallest_child_index]):
                smallest_child_index = right_child_index

            if smallest_child_index == index:
                break

            self.swap(index, smallest_child_index)
            index = smallest_child_index

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
