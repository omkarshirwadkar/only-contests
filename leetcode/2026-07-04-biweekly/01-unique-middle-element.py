def isMiddleElementUnique(nums):
    return nums.count(nums[len(nums)//2]) == 1

if __name__ == "__main__":
    arr = [1,2,3,4,2,1,3]
    print(isMiddleElementUnique(arr))