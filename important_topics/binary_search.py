# O(log(n)) complexity in a sorted array —-
# Time Complexity is -- O(log(n))

# Binary search if exists						Binary search leftmost occurence
# def find(a_list, target):							def find(a_list, target):
#     low = 0											 low = 0
#     high = len(a_list)									 high = len(a_list)
#
#     while low < high:								   	 while low < high:
#         mid = (low+high)//2								        mid = (low+high)//2
#         if a_list[mid] == target:								 if a_list[mid] >= target:
#             return mid											 high = mid
#         elif a_list[mid] > target:								else:
#             high = mid											low = mid + 1
#         else:											return low
#             low = mid + 1
#
#     return None
