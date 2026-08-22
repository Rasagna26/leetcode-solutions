class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        d1 = {}
        d2 = {}

        for i in range(len(list1)):
            d1[list1[i]] = i

        for i in range(len(list2)):
            d2[list2[i]] = i

        mini = float('inf')
        ans = []

        for key in d1:

            if key in d2:
                total = d1[key] + d2[key]

                if total < mini:
                    mini = total
                    ans = [key]

                elif total == mini:
                    ans.append(key)

        return ans
