from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0);

        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
            for a in freq[i]:
                res.append(a);
                if len(res) == 2:
                    return res


if __name__ == '__main__':
    print(Solution.topKFrequent(Solution, [1, 1, 1, 1, 2, 2, 3],2))
