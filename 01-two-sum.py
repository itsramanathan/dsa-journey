"""
Problem: Two Sum (Easy)
URL: https://leetcode.com/problems/two-sum/
Date: 2026-04-27
"""


def two_sum_optimal(nums, target):
    prevmap = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if diff in prevmap:
            return [prevmap[diff], idx]
        prevmap[num] = idx
    return None


def two_sum_brute(nums, target):
    # Your code here
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# Tests
if __name__ == "__main__":
    print(two_sum_brute([2, 7, 11, 15], 9))   # expected: [0, 1]
    print(two_sum_brute([3, 2, 4], 6))        # expected: [1, 2]
    print(two_sum_brute([3, 3], 6))           # expected: [0, 1]

    test_cases = [
        # (nums, target, expected)
        ([2, 7, 11, 15], 9, [0, 1]),       # basic case, answer at start
        ([3, 2, 4], 6, [1, 2]),            # answer not at index 0
        ([3, 3], 6, [0, 1]),               # duplicates, num == complement
        ([1, 2, 3, 4, 5, 6, 7, 8], 15, [6, 7]),  # answer at the end
        ([-1, -2, -3, -4, -5], -8, [2, 4]),       # negative numbers
        ([0, 4, 3, 0], 0, [0, 3]),         # zero handling, duplicates of zero
        ([5, 75, 25], 100, [1, 2]),        # answer at indices > 0
    ]

    for nums, target, expected in test_cases:
        result = two_sum_optimal(nums, target)
        status = "✅" if result == expected else "❌"
        print(
            f"{status} two_sum_optimal({nums}, {target}) = {result} (expected {expected})")

    print("\nAll tests done.")
