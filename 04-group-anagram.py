from collections import defaultdict


def groupAnagrams_brute(strs):
    # Q1 output: list of lists
    # Q3 avoid double-classification: 'used' parallel list of booleans
    # Q4 loop: outer picks a starter, inner finds its anagram-mates

    # initialize bookkeeping
    groups = []
    used = [False] * len(strs)

    # outer loop: pick a starter for a new group
    for i in range(len(strs)):
        # if already classified, skip
        if used[i]:
            continue
        # otherwise, start a new group with strs[i] in it, mark as used
        group = [strs[i]]
        used[i] = True

        # inner loop: scan the rest for anagram-mates
        for j in range(i+1, len(strs)):
            # if j already classified, skip
            if used[j]:
                continue
            # if strs[j] is an anagram of strs[i], add to group, mark used
            if sorted(strs[j]) == sorted(strs[i]):
                group.append(strs[j])
                used[j] = True
        # group is complete, append it
        groups.append(group)

    # return all groups
    return groups


def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())


if __name__ == "__main__":
    print(groupAnagrams_brute(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print()
    print("Optimal:")
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
