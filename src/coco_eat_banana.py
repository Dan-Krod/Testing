import math
import os
def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    result = right
    
    while left <= right:
        K = left + (right - left) // 2
        hours = 0
        for banana in piles:
            hours += math.ceil(banana / K)
            # hours += (banana - 1) // K + 1
                        
        if hours <= h:
            result = min(result, K)
            right = K - 1
        else:
            left = K + 1
            
    return result 

# Приклади:
# piles1 = [3, 8, 7, 11]
# H1 = 8
# print(min_eating_speed(piles1, H1))  # Результат: 4

piles2 = [30, 11, 23, 4, 20]
H2 = 5
print(min_eating_speed(piles2, H2))  # Результат: 30

# piles3 = [30, 11, 23, 4, 20]
# H3 = 6
# print(min_eating_speed(piles3, H3))  # Результат: 23
