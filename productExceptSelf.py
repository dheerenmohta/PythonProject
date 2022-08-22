from typing import List


class Solution:

    def productExceptSelf(self: List[int]) -> List[int]:
        res = [1] * len(self)
        prefix = 1
        for i in range(len(self)):
            res[i] = prefix
            prefix *= self[i]

        postfix = 1
        for i in range(len(self) - 1, -1, -1):
            res[i] = postfix * res[i]
            postfix = postfix * self[i]
        print(res)


if __name__ == '__main__':
    print(Solution.productExceptSelf([2, 3, 4]))  # [12,8,6]
