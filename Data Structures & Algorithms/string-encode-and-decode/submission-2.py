class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        right = len(s) - 1
        left = 0
        
        while left <= right:
            if s[left] == '#':
                length = int(s[i:left])
                res.append(s[left+1:left+1+length])

                i = left+1+length
                left = left+1+length
            left += 1
             

        return res
