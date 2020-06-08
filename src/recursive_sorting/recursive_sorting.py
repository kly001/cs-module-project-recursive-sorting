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

    #  My Code:
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


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr

###############################################################################

#  Resource: https://www.geeksforgeeks.org/merge-two-sorted-arrays/

# #Python program to merge 
# # two sorted arrays 
  
# # Merge arr1[0..n1-1] and  
# # arr2[0..n2-1] into  
# # arr3[0..n1+n2-1] 
# def mergeArrays(arr1, arr2, n1, n2): 
#     arr3 = [None] * (n1 + n2) 
#     i = 0
#     j = 0
#     k = 0
  
#     # Traverse both array 
#     while i < n1 and j < n2: 
      
#         # Check if current element  
#         # of first array is smaller  
#         # than current element of  
#         # second array. If yes,  
#         # store first array element  
#         # and increment first array 
#         # index. Otherwise do same  
#         # with second array 
#         if arr1[i] < arr2[j]: 
#             arr3[k] = arr1[i] 
#             k = k + 1
#             i = i + 1
#         else: 
#             arr3[k] = arr2[j] 
#             k = k + 1
#             j = j + 1
      
  
#     # Store remaining elements 
#     # of first array 
#     while i < n1: 
#         arr3[k] = arr1[i]; 
#         k = k + 1
#         i = i + 1
  
#     # Store remaining elements  
#     # of second array 
#     while j < n2: 
#         arr3[k] = arr2[j]; 
#         k = k + 1
#         j = j + 1
#     print("Array after merging") 
#     for i in range(n1 + n2): 
#         print(str(arr3[i]), end = " ") 
  
# # Driver code 
# arr1 = [1, 3, 5, 7] 
# n1 = len(arr1) 
  
# arr2 = [2, 4, 6, 8] 
# n2 = len(arr2) 
# mergeArrays(arr1, arr2, n1, n2); 
  
# # This code is contributed 
# # by ChitraNayal 


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
