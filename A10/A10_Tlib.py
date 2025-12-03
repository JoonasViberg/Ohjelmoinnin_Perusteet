from typing import List

def bubbleSort(PValues: List[int], PAsc: bool = True) -> None:
    n = len(PValues)
    
    for i in range(n - 1):
        # Optimization: Last i elements are already in the correct position
        for j in range(n - i - 1):
            
            should_swap = False
            
            # Ascending: swap if current > next
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    should_swap = True
            # Descending: swap if current < next
            else:
                if PValues[j] < PValues[j + 1]:
                    should_swap = True
                    
            if should_swap:
                # In-place swap
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                
    return None