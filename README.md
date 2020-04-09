# min-max-heap

Since no max heap seems to exist for Python, here is a Min and Max Heap
implementation.

I just stood there, dumbfounded that there is [no Max Heap for Python anywhere on
the internet](https://stackoverflow.com/a/2501527). Seriously? In 2020? If you
can find one, open an Issue and I'll check it out.

### Performance

Absolutely no claims are made about the performance of this Min/Max Heap
implementation. I would just be glad that it exists at all ;)

That said, even the Python 3.8 standard library heap is implemented in [pure
Python](https://github.com/python/cpython/blob/3.8/Lib/heapq.py).

### Usage

```python
# Min Heap
h = MinHeap([4, 5, 2, 1, 9, 10])
print(h.pop(), '==', 1)
print(h.pop(), '==', 2)
print(h.pop(), '==', 4)

# Max Heap
h = MaxHeap([4, 5, 2, 1, 9, 10])
print(h.pop(), '==', 10)
print(h.pop(), '==', 9)
print(h.pop(), '==', 5)
```

### Implementation Details

Yes, yes, I know I just wraped the standard library `heapq`. That is, after all,
[the officially accepted](https://stackoverflow.com/a/2501527) max heap data
structure for Python.
