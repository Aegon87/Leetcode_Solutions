class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # count = {}
        # freq = [[] for i in range(len(nums)+1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # for i, c in count.items():
        #     freq[c].append(i)

        # res = []
        # for i in range(len(freq)-1 , 0, -1):
        #     for j in freq[i]:
        #         res.append(j)
        #         if len(res) == k:
        #             return res


        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_ = sorted(count, key=count.get, reverse=True)

        return sorted_[:k]