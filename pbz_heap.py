import heapq

__all__ = 'MinHeap', 'MaxHeap'

class MinHeap:
    def __init__(self, data):
        self.data = data if isinstance(data, list) else list(data)
        heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, item)

    def pop(self):
        return heapq.heappop(self.data)

    def __str__(self):
        return f'<{self.__class__.__name__} {self.data}>'

    def __repr__(self):
        return str(self)

    def __format__(self):
        return str(self)

    def __hash__(self):
        return hash(tuple(i for i in self.data))


class HeapPointer:
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        "Less-than and Greather-than are swapped for max heap functionality."
        return self.item > other.item

    def __gt__(self, other):
        "Less-than and Greather-than are swapped for max heap functionality."
        return self.item < other.item

    def __repr__(self):
        return str(self.item)

    def __str__(self):
        return str(self)

    def __format__(self):
        return str(self)

    def __hash__(self):
        return hash(self.item)


class MaxHeap(MinHeap):
    def __init__(self, data):
        MinHeap.__init__(self, [HeapPointer(i) for i in data])

    def push(self, item):
        MinHeap.push(self, HeapPointer(item))

    def pop(self):
        return MinHeap.pop(self).item


if __name__ == '__main__':
    h = MinHeap([4, 5, 2, 1, 9, 10])
    print(h.pop(), '==', 1)
    print(h.pop(), '==', 2)
    print(h.pop(), '==', 4)
    print(h)

    print('-' * 10)

    h = MaxHeap([4, 5, 2, 1, 9, 10])
    print(h.pop(), '==', 10)
    print(h.pop(), '==', 9)
    print(h.pop(), '==', 5)
    print(h)

    print('-' * 10)

    d = {h : 'hello world!'}

    print(d)
