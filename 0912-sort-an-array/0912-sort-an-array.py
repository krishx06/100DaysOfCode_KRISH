class Solution:
    def sortArray(self, lst: List[int]) -> List[int]:
        def heapify(heap_size, index):
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[index], lst[largest] = lst[largest], lst[index]
                heapify(heap_size, largest)
         
        for i in range(len(lst) //2-1, -1, -1):
            heapify(len(lst), i)
            
        for i in range(len(lst)-1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]
            heapify(i,0)
            
        return lst