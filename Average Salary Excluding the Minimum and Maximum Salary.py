class Solution:
    def average(self, salary: list[int]) -> float:
        a=sum(salary)-(min(salary)+max(salary))
        return a/(len(salary)-2)
