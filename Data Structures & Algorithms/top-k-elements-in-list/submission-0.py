class Solution:
 def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequency of each number
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Step 2: Bucket sort by frequency
    # freq[i] = list of numbers that appear exactly i times
    freq = [[] for _ in range(len(nums) + 1)]
    for num, c in count.items():
        freq[c].append(num)

    # Step 3: Walk from highest frequency down, collecting numbers
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res