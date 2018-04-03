'''
Heap Module
'''


class BinaryHeap():
    def __init__(self):
        self.content = [0]
        self.currentSize = 0

    def __str__(self):
        return self.content.__str__()

    def __repr__(self):
        return self.content.__repr__()

    @property
    def size(self):
        return self.currentSize

    def insert(self, k):
        self.content.append(k)
        self.currentSize = len(self.content) - 1
        pos = self.currentSize
        while (pos // 2 >= 1):
            if self.content[pos // 2] > self.content[pos]:
                temp = self.content[pos // 2]
                self.content[pos // 2] = self.content[pos]
                self.content[pos] = temp
            pos = pos // 2


    def findMin(self):
        pass

    def delMin(self):
        result = self.content[1]
        last = self.content.pop()
        self.content[1] = last
        self.currentSize -= 1
        pos = 1
        while 2*pos <= self.currentSize:
            left = self.content[2*pos]
            try:
                right = self.content[2*pos + 1]
            except IndexError:
                right = None
            if (right is None) or (right > left):
                if self.content[pos] > self.content[2*pos]:
                    temp = self.content[2*pos]
                    self.content[2*pos] = self.content[pos]
                    self.content[pos] = temp
                pos = pos * 2
            else:
                if self.content[pos] > self.content[2*pos + 1]:
                    temp = self.content[2*pos + 1]
                    self.content[2*pos + 1] = self.content[pos]
                    self.content[pos] = temp
                pos = pos * 2 + 1
        return result
    def isEmpty():
        pass

    def buildHeap(array):
        pass

    def __eq__(self, other):
        return self.content ==  other.content
