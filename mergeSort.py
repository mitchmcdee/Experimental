def mergeSort(a, left, right):
    # If we're only checking one element, its sorted
    if right-left == 1:
        return
    
    # Get halfway point
    half = (left+right)//2
  
    # Sort those two halves
    mergeSort(a, left, half)
    mergeSort(a, half, right)
    
    # Merged halves
    merge(a, left, half, right)

def merge(a, l, h, r):
    merged = []
    i = 0
    j = 0
        
    len1 = h-l
    len2 = r-h
    while i < len1 and j < len2:
        if a[l+i] <= a[h+j]:
            merged.append(a[l+i])
            i += 1
        else:
            merged.append(a[h+j])
            j += 1
            
    while i < len1:
        merged.append(a[l+i])
        i += 1
        
    while j < len2:
        merged.append(a[h+j])
        j += 1
        
    for i in range(l,r):
        a[i] = merged[i-l]
    
n = int(input())
unsorted = [int(input()) for _ in range(n)]
mergeSort(unsorted, 0, n)
[print(i) for i in unsorted]