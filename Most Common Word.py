class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]):

        paragraph = paragraph.lower()

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.split()

        freq = {}

        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        maxi = 0
        ans = ""

        for key in freq:
            if freq[key] > maxi:
                maxi = freq[key]
                ans = key

        return ans
