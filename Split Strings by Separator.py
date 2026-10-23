class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            arr = word.split(separator)
            for ch in arr:
                if ch != "":
                    ans.append(ch)
        return ans      
