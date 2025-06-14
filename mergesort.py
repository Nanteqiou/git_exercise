def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1
    return list_to_sort_by_merge


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

base_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
base_length = len(base_list)
base_positions = range(base_length)

sorted_list = mergeSort(base_list.copy())
 
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



