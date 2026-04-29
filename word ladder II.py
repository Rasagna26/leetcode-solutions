def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    par = {}
    level = {beginWord}
    found = False

    while level and not found:
        next_level = set()
        for word in level:
            wordSet.discard(word)

        for word in level:
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new = word[:i] + ch + word[i+1:]
                    if new in wordSet:
                        if new not in par:
                            par[new] = []
                        par[new].append(word)
                        next_level.add(new)
                        if new == endWord:
                            found = True

        level = next_level

    res = []

    def backtrack(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        if word not in par:
            return
        for p in par[word]:
            backtrack(p, path + [p])

    if found:
        backtrack(endWord, [endWord])

    return res
