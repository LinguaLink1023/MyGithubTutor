def quick_sort(nums):
    """快速排序算法

    Args:
        nums (_type_): 传入一个数组
    """    
    recursion_quick_sort(nums, 0, len(nums) - 1)
    return nums

def recursion_quick_sort(nums, start, end):
    if end > start:
        #find insertion_pos
        return 