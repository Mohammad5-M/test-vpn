from collections import Counter
def remove_duplicates(arr, n):
 
    temp = Counter(arr)
    return [*temp]
