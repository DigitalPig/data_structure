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
        if self.size == 0:
            raise IndexError('Popping item from an empty heap')
        else:
            self.size -= 1
            return self.delMin()

    def percholate_down(self, pos):
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


    def delMin(self):
        result = self.content[1]
        last = self.content.pop()
        self.content[1] = last
        self.currentSize -= 1
        pos = 1
        self.percholate_down(pos)
        return result

    def isEmpty(self):
        return self.currentSize == 0

    def buildHeap(self, array):
        self.content = [0] + array
        self.currentSize = len(array)
        pos = self.currentSize
        while pos > 1:
            pos = pos // 2
            self.percholate_down(pos)
        self.percholate_down(1)



    def __eq__(self, other):
        return self.content ==  other.content
