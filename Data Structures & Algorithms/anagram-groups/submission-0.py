class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        for s in strs:
            w = " ".join(sorted(s))
            if w in g:
                g[w].append(s)
            else:
                g[w] = [s]
        return list(g.values())
