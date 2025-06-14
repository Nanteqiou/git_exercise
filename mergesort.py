def assignment(target_list, target_idx, reduced_list, reduced_idx):
    """Assigns value from reduced_list[reduced_idx] to target_list[target_idx]."""
    target_list[target_idx] = reduced_list[reduced_idx]


def merge_sort(list_to_sort):
    """
    Sorts a list using the merge sort algorithm.
    Args:
        lst (list): The list to sort.
    Returns:
        list: The sorted list.
    """
    main_length = len(list_to_sort)
    
    if (main_length > 1):
        mid = main_length // 2
        left_half = list_to_sort[:mid]
        right_half = list_to_sort[mid:]
        
        # Cut recursively lists to halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0   #left_half iterator
        j = 0   #right_half iterator 
        k = 0   #iterator for merging
        
        # Merge all halves
        left_length = len(left_half)
        right_length = len(right_half)
        
        while i < left_length and j < right_length:
            if left_half[i] <= right_half[j]:
                assignment(list_to_sort, k, left_half, i)
                i += 1
            else:
                assignment(list_to_sort, k, right_half, j)
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < left_length:
            list_to_sort[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            list_to_sort[k] = right_half[j]
            j += 1
            k += 1
    # In this case, we decided that the function returns a list object for better testing readability
    
    return list_to_sort

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

base_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
base_length = len(base_list)
base_positions = range(base_length)

sorted_list = merge_sort(base_list.copy())
 
sorted_length = (len(sorted_list))
sorted_positions = range(sorted_length)

fig, ax = plt.subplots(1,2, figsize=(12,6),sharey = True)

base_x = np.array(base_positions)
base_y = np.array(base_list)

ax[0].set_xlabel("Index")
ax[0].set_ylabel("Numbers")
ax[0].set_title("Plot of unsorted numbers")
ax[0].set_yticks(np.arange(20, 100, 10, dtype = int) )
ax[0].set_ylim(10,100)
[spine.set_visible(False) for spine in ax[0].spines.values()]

sns.barplot(x=base_x, y=base_y, ax = ax[0], color = "skyblue")

sorted_x = np.array(sorted_positions)
sorted_y = np.array(sorted_list)
ax[1].set_title("Plot of sorted numbers")
ax[1].set_xlabel("Index")
ax[1].set_ylabel("Numbers")
ax[1].set_yticks(np.arange(20, 100, 10, dtype = int))
ax[1].set_ylim(10, 100)
[spine.set_visible(False) for spine in ax[1].spines.values()]

sns.barplot(x=sorted_x, y=sorted_y, ax = ax[1], color ="yellow")

plt.show()



