def maxValidPairSum(nums, k):
    n = len(nums)
    suffMax = [0] * n
    suffMax[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        suffMax[i] = max(nums[i], suffMax[i + 1])
    maxAns = 0
    for i in range(n - k):
        maxAns = max(maxAns, nums[i] + suffMax[i + k])
    return maxAns

if __name__ == "__main__":
    nums = [23, 41, 11, 53, 100, 2, 57, 84, 290, 77]
    k = 3
    print(maxValidPairSum(nums, k))