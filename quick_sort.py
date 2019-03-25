#coding=utf-8
#实现快速排序
def quick_sort(nums):
    if len(nums) < 2:
        return nums
    less = []
    greater = []
    base = nums.pop()
    for i in nums:
        if i < base:
            less.append(i)
        else:
            greater.append(i)
    return quick_sort(less) + [base] + quick_sort(greater)
def main():
    nums = [3,2,1,4,5,6,9,8]
    print(quick_sort(nums))
main()

