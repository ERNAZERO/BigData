# // Удалить из массива элемент, расположенный
# после каждого значения,
# равного минимальному элементу.
from typing import List

# spisok = [1, 212, 1, 432, 3223, 32, 231, 1, 9, 1, 12,21,1]
#
#
# def deleteNumberAfterMin(spisok):
#     min_value = spisok[0]
#     for i in spisok[1::]:
#         if i < min_value:
#             min_value = i
#     print("min value", min_value)
#     new_spisok=[]
#     for index, value in enumerate(spisok[:-1]):
#         if value != min_value:
#             new_spisok.append(spisok[index+1])
#     return new_spisok
#
#
# print(deleteNumberAfterMin(spisok))



import numpy as n

def removeDuplicates(nums: List[int]) -> int:
    # Length of the update array
    count = 0
    # Loop for all the elements in the array
    for i in range(len(nums)):
        # If the current element is equal to the next element, we skip
        if i < len(nums) - 2 and nums[i] == nums[i + 1]:
            continue
        # We will update the array in place
        nums[count] = nums[i]
        count += 1
    return count


nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5]

print (removeDuplicates(nums))



