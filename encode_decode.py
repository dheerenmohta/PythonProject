from typing import List


class Solution:
    def encode(self, list: List[str]) -> str:
        newS = ""
        for s in list:
            newS += f"{len(s)}#{s}"
        print(newS)

    def decode(self, s: str) -> List[str]:

        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                length = int(s[i:j])
                print(length)
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length

        return res


if __name__ == '__main__':
    print(Solution.encode(Solution, ["Dheeren", "Mohta#"]))
    print(Solution.decode(Solution, "7#Dheeren6#Mohta#"))
