# ## TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr=[]

    a = 0
    b = 0

    while a<len(arrA) and b<len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a+=1
        else:
            merged_arr.append(arrB[b])
            b+=1

    while a<len(arrA):
        merged_arr.append(arrA[a])
        a+=1
    while b<len(arrB):
        merged_arr.append(arrB[b])
        b+=1

    return merged_arr
    #####################################################################

    #  My First attempt:
    #  Resource: https://www.geeksforgeeks.org/merge-two-sorted-arrays/

    # def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # # ## Your code here
    # i = 0
    # j = 0
    # k = 0

    #  # ## Traverse both arrays
    # while i < len(arrA) and j < len(arrB):
    #     if arrA[i] < arrB[j]:
    #         merged_arr[k] = arrA[i]
    #         k = k + 1
    #         i = i + 1
    #     else:
    #         merged_arr[k] = arrB[j]
    #         k = k + 1
    #         j = j + 1
    # while i < len(arrA):
    #     merged_arr[k] = arrA[i]
    #     k = k + 1
    #     i = i + 1
    # while j < len(arrB):
    #     merged_arr[k] = arrB[j]
    #     k = k + 1
    #     j = j + 1

    #return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr):
        if len(arr)>1:
            left = merge_sort(arr[:len(arr)//2])
            right = merge_sort(arr[len(arr)//2:])
            arr = merge(left, right)
    
    return arr

###################################################################################

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    if(arr[mid] <= arr[start2]):
        return arr
    
    while (start <= mid and start2 <= end):
        if arr[start] <= arr[start2]:
            start += 1
        else:
             value = arr[start2]
             index = start2

             while (index != start):
                 arr[index] = arr[index-1]
                 index-=1
             arr[start] = value

             start+=1
             mid+=1
             start2+=1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if(l < r):
        m = (r + l)//2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)

        merge_in_place(arr, l, m, r)

    return arr

 # Resource: https://www.geeksforgeeks.org/in-place-merge-sort/

#  # Python program in-place Merge Sort 
  
# # Merges two subarrays of arr. 
# # First subarray is arr[l..m] 
# # Second subarray is arr[m+1..r] 
# # Inplace Implementation 
# def merge(arr, start, mid, end): 
#     start2 = mid + 1; 
  
#     # If the direct merge is already sorted 
#     if (arr[mid] <= arr[start2]): 
#         return; 
      
#     # Two pointers to maintain start 
#     # of both arrays to merge 
#     while (start <= mid and start2 <= end): 
  
#         # If element 1 is in right place 
#         if (arr[start] <= arr[start2]): 
#             start += 1; 
#         else: 
#             value = arr[start2]; 
#             index = start2; 
  
#             # Shift all the elements between element 1 
#             # element 2, right by 1. 
#             while (index != start): 
#                 arr[index] = arr[index - 1]; 
#                 index -= 1; 
              
#             arr[start] = value; 
  
#             # Update all the pointers 
#             start += 1; 
#             mid += 1; 
#             start2 += 1; 
          
# ''' 
# * l is for left index and r is right index of 
# the sub-array of arr to be sorted 
# '''
# def mergeSort(arr, l, r): 
#     if (l < r): 
  
#         # Same as (l + r) / 2, but avoids overflow 
#         # for large l and r 
#         m = l + (r - l) // 2; 
  
#         # Sort first and second halves 
#         mergeSort(arr, l, m); 
#         mergeSort(arr, m + 1, r); 
  
#         merge(arr, l, m, r); 
      
# ''' UTILITY FUNCTIONS '''
# ''' Function to pran array '''
# def printArray(A, size): 
  
#     for i in range(size): 
#         print(A[i], end=" "); 
#     print(); 
  
# ''' Driver program to test above functions '''
# if __name__ == '__main__': 
#     arr = [ 12, 11, 13, 5, 6, 7 ]; 
#     arr_size = len(arr); 
  
#     mergeSort(arr, 0, arr_size - 1); 
#     printArray(arr, arr_size); 
      
# # This code is contributed by 29AjayKumar 


###############################################################################





# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     # Your code here
    
#     return arr
