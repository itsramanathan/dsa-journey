"""
NeetCode #2 — Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return True if any value appears at least twice
in the array, and False if every element is distinct.

Pattern: hash set for O(1) membership lookup.
Same DNA as Two Sum — trade O(n) space to drop time from O(n²) to O(n).
"""


def contains_duplicate_brute(nums):
    """
    Brute force: for each element, check if it appears anywhere later in the list.

    Time:  O(n²) — outer loop is O(n), `in nums[i+1:]` is O(n) per iteration.
    Space: O(n) — each slice nums[i+1:] allocates a new list.
                  (The double-loop variant without slicing is O(1) space.)
    """
    for i, num in enumerate(nums):
        if num in nums[i+1:]:
            return True
    return False


def contains_duplicate(nums):
    """
    Optimal: walk once, remember seen values in a set, return True on first repeat.

    Time:  O(n) — single pass, each `in` check and `add` on a set is O(1) average.
    Space: O(n) — worst case (no duplicates) the set holds all n elements.

    Best case: O(1) extra work after finding the first duplicate (early return).
    """
    # ────────────────────────────────────────────────
    # PASTE YOUR SOLUTION HERE
    # ────────────────────────────────────────────────
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_pythonic(nums):
    """
    Idiomatic Python one-liner: a set drops duplicates, so if its length differs
    from the original list, at least one duplicate existed.

    Time:  O(n) — set(nums) walks every element.
    Space: O(n) — the set holds up to n elements.

    Note: cannot short-circuit on early duplicates the way the loop version can,
    but the C-implemented set construction has a smaller constant factor, so it
    often wins on small inputs in practice.
    """
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    test_cases = [
        # (input, expected output, description)
        ([1, 2, 3, 1],                       True,  "duplicate at the end"),
        ([1, 2, 3, 4],                       False, "all distinct"),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],     True,  "many duplicates"),
        ([5, 6, 7, 5],                       True,
         "duplicate where value ≠ index — catches index/value confusion"),
        ([],                                 False, "empty array edge case"),
        ([42],                               False, "single element edge case"),
        ([-1, -2, -3, -1],                   True,  "negative numbers"),
    ]

    implementations = [
        contains_duplicate_brute,
        contains_duplicate,
        contains_duplicate_pythonic,
    ]

    for fn in implementations:
        for nums, expected, description in test_cases:
            result = fn(nums)
            assert result == expected, (
                f"{fn.__name__} failed on {description}: "
                f"input={nums}, expected={expected}, got={result}"
            )
        print(f"✅ {fn.__name__}: all {len(test_cases)} tests passed")

    print("\nAll implementations verified.")
