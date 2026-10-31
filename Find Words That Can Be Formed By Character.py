from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        c = 0
        char_c = Counter(chars)

        for word in words:
            word_c = Counter(word)
            valid = True

            for ch in word_c:
                if word_c[ch] > char_c[ch]:
                    valid = False
                    break

            if valid:
                c += len(word)

        return c
