def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the remaining unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input the array from the user
arr = [int(x) for x in input("Enter elements of the array separated by spaces: ").split()]

selection_sort(arr)
print("Sorted array is:", arr)
# def selection_sort(arr): This function takes an array arr as input and sorts it in ascending order
# using the selection sort algorithm. The selection sort algorithm works as follows:

# It iterates through the array from the first element to the second-to-last element.

# In each iteration, it finds the minimum element in the remaining unsorted portion of the array.
# To do this, it initializes min_index to the current iteration index (i) and then compares the elements
# from i + 1 to the end of the array. If it finds an element smaller than the current minimum, it updates 
# min_index to the index of the smaller element.

# After finding the minimum element in the unsorted portion, it swaps this minimum element with the first 
#     element in the unsorted portion. This effectively moves the smallest unsorted element to its correct 
#     position at the beginning of the sorted portion.

# The process continues until the entire array is sorted.

# Input the array from the user:

# The code prompts the user to input the elements of the array. The user is expected to enter numbers s
# eparated by spaces.
# The input is read using the input function, and the split() method is used to split the input string 
# into a list of numbers.
# Sorting the array:

# The selection_sort function is called with the user-provided array as the input.
# The function sorts the array in-place using the selection sort algorithm.
# Displaying the sorted array:

# Finally, the code prints the sorted array using print("Sorted array is:", arr).
# In summary, this code allows the user to input an array of numbers, then sorts the array using the 
# selection sort algorithm, and displays the sorted array. Selection sort repeatedly selects the minimum 
# element from the unsorted portion and moves it to its correct position in the sorted portion, resulting in a 
# sorted array in ascending order.