import math
from SortingAlgorithm import SortingAlgorithm #import input data for testing the outcome and plotting  the results


class MergeSort(SortingAlgorithm):

    def Sort(self, list_to_sort):

        if len(list_to_sort) <= 1: #if the list is empty or consists of only one item, no sorting is neeeded -> return the input 
            return list_to_sort

        mid_index = math.floor(len(list_to_sort) / 2)

        left_list = self.Sort(list_to_sort[:mid_index]) # recursion applied via division
        right_list = self.Sort(list_to_sort[mid_index:])

        list_to_sort = self.Merge_List(left_list, right_list)
        return list_to_sort

    def Merge_List(self, left_list, right_list):
        left_list_length = len(left_list)
        right_list_length = len(right_list)
        merged_list = []
        left_index = 0
        right_index = 0

        while left_index < left_list_length and right_index < right_list_length:
            if left_list[left_index] <= right_list[right_index]:
                merged_list.append(left_list[left_index])  # use append to add a single item at the end of the list as at this moment only single elements are compared and placed
                left_index += 1
            else:
                merged_list.append(right_list[right_index]) 
                right_index += 1

        if left_index < left_list_length:
            merged_list.extend(left_list[left_index:]) # use extend as here we are adding the sublists which can contain more than one elements (sorted subsection)

        if right_index < right_list_length:
            merged_list.extend(right_list[right_index:])

        return merged_list


test_sort_algo = MergeSort()
test_sort_algo.Plot_Sort_Performance()

# Computational Complexity: 
# the division of the entire list in two (repetitively, until reaching single elements) requires computational complexity of log(n) (the base of the log is irrelevant as the curve would be very similar, however due to division by 2 in each step - most probably log with base 2)
# the merging of the items or the sublists together requires a computational complexity of n (linear curve)
# this leads to a final computational complexity of n*log(n). This would be the same for the average, worst and base case scenario as in all cases the split operation and the merging operation should be done, even if the list is sorted initially.

