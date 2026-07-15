'''
Approach:
1. How to start:
Realize anagrams share the same sorted letters → use that sorted string as a unique key.

2. The tool:
defaultdict(list) is a dictionary that auto‑creates a new empty list whenever you try to access a key that doesn’t exist yet.

3. How it works:
You loop through each word.
Compute its sorted signature.
Use dict[signature].append(word) – if the signature is new, it creates [] first, then appends; if it exists, it just appends.
No need to write if key not in dict checks.

4. End result:
The dictionary holds keys (signatures) and values (lists of anagrams). Return list(dict.values()) to get the grouped output.
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def_dict = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            def_dict[sorted_s].append(s)
        return list(def_dict.values())
    