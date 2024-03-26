def find_kth_largest_el(array, k):
    k = len(array) - k 
    array_sorted = array.copy()
    
    def quick_select(left, right):
        if left == right:
            return array_sorted[left]
        
        # pivot_index = random.randint(left, right)
        # pivot = array_sorted[pivot_index]
        
        pivot = array_sorted[right]
        cursor = left
        
        for i in range(left, right):
            if array_sorted[i] <= pivot:
                array_sorted[i], array_sorted[cursor] = array_sorted[cursor], array_sorted[i]
                cursor += 1
        
        array_sorted[cursor], array_sorted[right] = array_sorted[right], array_sorted[cursor]                
    
        if cursor > k :
            return quick_select(left, cursor - 1)
        elif cursor < k :
            return quick_select(cursor + 1, right)
        else:
            return array_sorted[k], array.index(array_sorted[k])  # Повертаємо значення та індекс к-го найбільшого елемента
        
    result = quick_select(0, len(array_sorted) - 1)
    return result[0], result[1]

array = [8, 0, 16, 67, 11, -1]
k = 4
result = find_kth_largest_el(array, k)
print(result)
