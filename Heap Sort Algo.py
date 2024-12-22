def heapify(ul, index, heap_size):
    maxi = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and ul[left_index] > ul[maxi]:
        maxi = left_index

    if right_index < heap_size and ul[right_index] > ul[maxi]:
        maxi = right_index

    if maxi != index:
        ul[maxi], ul[index] = ul[index], ul[maxi]
        heapify(ul, maxi, heap_size)

def heap_sort(ul):
    n = len(ul)
    for i in range(n // 2 - 1, -1, -1):
        heapify(ul, i, n)

    for i in range(n - 1, 0, -1):
        ul[0], ul[i] = ul[i], ul[0]
        heapify(ul, 0, i)
    return ul

l = input("Enter your numbers separated by a comma: ").strip()
ul = [int(i) for i in l.split(",")]
print(heap_sort(ul))